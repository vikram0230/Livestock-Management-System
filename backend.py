import os
import sqlite3
from datetime import datetime, date
import pandas as pd
from dateutil.relativedelta import relativedelta
from math import ceil
import math
from pandas.core.frame import DataFrame

# Create DB file if not present already in the same directory
if not (os.path.isfile('data.db')):

    """
        Tables initialised:
            - MasterTable
            - WeightTable
            - KidsIdTable
            - LivestockNetworth
            - Labour
            - Feed
            - MiscExpense
            - Income
    """

    with open('data.db', 'w') as f:
        conn = sqlite3.connect('data.db')

        c = conn.cursor()

        createStmt_MasterDatabase = 'goat_no INTEGER PRIMARY KEY, breed TEXT, date_of_birth DATE, gender TEXT, pregnant TEXT, weight INT, date_of_delivery DATE, no_of_kids INT, no_of_male_kids INT, no_of_female_kids INT, mortality TEXT, v1 DATE, v2 DATE, v3 DATE, v4 DATE, v5 DATE, v6 DATE, v7 DATE, v8 DATE, sold_date DATE, sold_rate INT'
        c.execute('CREATE TABLE MasterTable(' + createStmt_MasterDatabase + ')')
        conn.commit()

        createStmt_KidsTable = 'mother_id INT, kid_id INT, gender TEXT'
        c.execute('CREATE TABLE KidsTable(' + createStmt_KidsTable + ')')
        conn.commit()

        createStmt_LivestockNetworth = 'category TEXT, breed TEXT, cost INT, total_weight INT, total_cost INT'
        c.execute('CREATE TABLE LivestockNetworth(' + createStmt_LivestockNetworth + ')')
        conn.commit()

        createStmt_Labour = 'category TEXT,salary INT, count INT, monthly_total INT'
        c.execute('CREATE TABLE Labour(' + createStmt_Labour + ')')
        conn.commit()

        createStmt_Feed = 'purchase_date DATE, item TEXT, weight INT, cost INT, total_cost INT'
        c.execute('CREATE TABLE Feed(' + createStmt_Feed + ')')
        conn.commit()

        createStmt_MiscExpense = 'purchase_date DATE, category TEXT, cost INT'
        c.execute('CREATE TABLE MiscExpense(' + createStmt_MiscExpense + ')')
        conn.commit()

        createStmt_Income = 'purchase_date DATE, details TEXT, cost INT'
        c.execute('CREATE TABLE Income(' + createStmt_Income + ')')
        conn.commit()

        values = {'goat_id':1, 'breed':'some', 'date_of_birth':date(2001, 12, 21), 'gender':'m', 'pregnant':'No', 'weight':10, 'no_of_kids':0, 'no_of_male_kids':0, 'no_of_female_kids':0, 'mortality':'Alive'}

        for i in range(0, 50):
            c.execute('INSERT INTO MasterTable (goat_no, breed, date_of_birth, gender, pregnant, weight, no_of_kids, no_of_male_kids, no_of_female_kids, mortality) VALUES(:goat_id, :breed, :date_of_birth, :gender, :pregnant, :weight, :no_of_kids, :no_of_male_kids, :no_of_female_kids, :mortality)', values)
            values['goat_id'] += 1
            # Creating a weight table for the goat passed
            createStmt_WeightTable = 'weight INT, date_checked DATE'
            c.execute('CREATE TABLE WeightTable' +
                    str(values['goat_id']) + '(' + createStmt_WeightTable + ')')
            conn.commit()

            c.execute('INSERT INTO WeightTable' + str(values['goat_id']) + ' VALUES(:weight, :date_checked)', {
                    'weight': values['weight'], 'date_checked': datetime.date(datetime.now())})

            conn.commit()

            # Get types of breeds present in LivestockNetworth      
            exists = False
            c.execute('SELECT breed, category FROM LivestockNetworth')
            result = c.fetchall()
            if len(result) != 0:
                exists = True

            # Checking if new goat is kid or adult
            c.execute('SELECT (julianday(:curdate) - julianday(:date_of_birth)) AS day WHERE day > 365 ', {'curdate': datetime.date(datetime.now()), 'date_of_birth': values['date_of_birth']})
            r = c.fetchall()
            age = 'Kid' if len(r) == 0 else 'Adult'
            # Determining the category of the new goat
            category = age + ' Male' if values['gender'] == 'm' else age + ' Female'

            if not exists:
                # Inserting the new record in LivestockNetworth
                c.execute('INSERT INTO LivestockNetworth(category, breed, cost, total_weight, total_cost) VALUES(:category, :breed, 0, :total_weight, 0)', {'category': category, 'breed': values['breed'], 'total_weight': values['weight']})
                conn.commit()
            else:
                for res in result:
                    # Checking whether it already exists
                    if res[0] == values['breed'] and res[1] == category:
                        # Getting total weight from the LivestockNetworth
                        c.execute('SELECT total_weight FROM LivestockNetworth WHERE breed=:breed AND category=:category', {'breed': res[0], 'category': res[1]})
                        total_weight = c.fetchall()[0][0] + values['weight']

                        # Update total weight in LivestockNetworth
                        c.execute('UPDATE LivestockNetworth SET total_weight=:total_weight', {'total_weight': total_weight})
                        conn.commit()
                    else:
                        # Inserting the new record in LivestockNetworth
                        c.execute('INSERT INTO LivestockNetworth(category, breed, cost, total_weight, total_cost) VALUES(:category, :breed, 0, :total_weight, 0)', {'category': category, 'breed': values['breed'], 'total_weight': values['weight']})
                        conn.commit()


def genExcel():
    db = DataBase()
    goatdata = db.getGoatRecords()
    goatdataColumns = db.getColumnNames()
    goatdf = pd.DataFrame(goatdata,columns=goatdataColumns)
    goatdf.name = 'Master Table'

    kiddata = db.getKidRecords()
    kiddataColumns = db.getKidColumnNames()
    kiddf = pd.DataFrame(kiddata, columns = kiddataColumns)
    kiddf.name = 'Mother-Kid Table'

    livestockdata = db.getLivestockRecords()
    livestockdataColumns = db.getLivestockColumnNames()
    livestockdf = pd.DataFrame(livestockdata, columns = livestockdataColumns)
    livestockdf.name = 'LiveStock Networth'

    labourdata = db.getLabourRecords()
    labourdataColumns = db.getLabourColumnNames()
    labourdf = pd.DataFrame(labourdata,columns= labourdataColumns)
    labourdf.name = 'Labour Salary'

    feeddata = db.getFeedRecords()
    feeddataColumns = db.getFeedColumnNames()
    feeddf = pd.DataFrame(feeddata,columns= feeddataColumns)
    feeddf.name = 'Feed'

    miscdata = db.getMiscRecords()
    miscdataColumns = db.getMiscColumnNames()
    miscdf = pd.DataFrame(miscdata,columns= miscdataColumns)
    miscdf.name = 'Misc Expenses'

    incomedata = db.getIncomeRecords()
    incomedataColumns = db.getIncomeColumnNames()
    incomedf = pd.DataFrame(incomedata,columns= incomedataColumns)
    incomedf.name = 'Income'

    writer = pd.ExcelWriter('./Excel' + str(datetime.date(datetime.now())) + '.xlsx',engine='xlsxwriter')

    goatdf.to_excel(writer, sheet_name=goatdf.name)
    kiddf.to_excel(writer, sheet_name=kiddf.name)
    livestockdf.to_excel(writer, sheet_name=livestockdf.name)
    labourdf.to_excel(writer, sheet_name=labourdf.name)
    feeddf.to_excel(writer, sheet_name=feeddf.name)
    miscdf.to_excel(writer, sheet_name=miscdf.name)
    incomedf.to_excel(writer, sheet_name=incomedf.name)

    writer.save()
    db = None


def updateLiveStockNetworth(values):
    exists = False
    # Get types of breeds present in LivestockNetworth      
    c.execute('SELECT breed, category FROM LivestockNetworth GROUP BY breed, category')
    result = c.fetchall()
    if len(result) != 0:
        exists = True

    # Checking if new goat is kid or adult
    c.execute('SELECT (julianday(:curdate) - julianday(:date_of_birth)) AS day WHERE day > 365 ', {'curdate': datetime.date(datetime.now()), 'date_of_birth': values['date_of_birth']})
    r = c.fetchall()
    age = 'Kid' if len(r) == 0 else 'Adult'
    # Determining the category of the new goat
    category = age + ' Male' if values['gender'] == 'm' else age + ' Female'

    if not exists:
        # Inserting the new record in LivestockNetworth
        c.execute('INSERT INTO LivestockNetworth(category, breed, cost, total_weight, total_cost) VALUES(:category, :breed, 0, :total_weight, 0)', {'category': category, 'breed': values['breed'], 'total_weight': values['weight']})
        conn.commit()
    else:
        for res in result:
            # Checking whether it already exists
            if res[0] == values['breed'] and res[1] == category:
                # Getting total weight from the LivestockNetworth
                c.execute('SELECT total_weight FROM LivestockNetworth WHERE breed=:breed AND category=:category', {'breed': res[0], 'category': res[1]})
                total_weight = c.fetchall()[0][0] + values['weight']
                # Update total weight in LivestockNetworth
                c.execute('UPDATE LivestockNetworth SET total_weight=:total_weight WHERE breed=:breed AND category=:category', {'total_weight': total_weight, 'breed': res[0], 'category': res[1]})
                conn.commit()
        else:
            # Inserting the new record in LivestockNetworth
            c.execute('INSERT INTO LivestockNetworth(category, breed, cost, total_weight, total_cost) VALUES(:category, :breed, 0, :total_weight, 0)', {'category': category, 'breed': values['breed'], 'total_weight': values['weight']})
            conn.commit()

conn = sqlite3.connect('data.db')

c = conn.cursor()

if datetime.date(datetime.now()) == date(date.today().year, 4, 1):
    c.execute('DELETE FROM Labour')
    c.execute('DELETE FROM Feed')
    c.execute('DELETE FROM MiscExpense')
    c.execute('DELETE FROM Income')
    c.execute('DELETE FROM MasterTable WHERE sold_rate!=\'None\' OR mortality=\'Dead\'')
    c.execute('DELETE FROM LivestockNetworth')

    c.execute('SELECT goat_no, breed, date_of_birth, weight, gender FROM MasterTable')
    result = c.fetchall()
    for res in result:
        values = {'goat_id': res[0], 'breed': res[1], 'date_of_birth': res[2], 'weight': res[3], 'gender': res[4]}
        updateLiveStockNetworth(values)

    genExcel()

class DataBase:
    def __init__(self):
        pass

    def getGoatRecords(self):
        c.execute('SELECT * FROM MasterTable')
        res = c.fetchall()
        for i in range(len(res)):
            res[i] = list(res[i])
            if res[i][2] == res[i][11]:
                res[i][11] = None
                res[i][12] = None
                res[i][13] = None
                res[i][14] = None
                res[i][15] = None
                res[i][16] = None
                res[i][17] = None
                res[i][18] = None
        return res

    def getNumberOfRecords(self):
        c.execute('SELECT COUNT(*) FROM MasterTable')
        return (c.fetchall())

    def getColumnNames(self):
        names = ['goat_no', 'breed', 'date_of_birth', 'gender', 'pregnant', 'weight', 'date_of_delivery', 'no_of_kids', 'no_of_male_kids', 'no_of_female_kids', 'mortality', 'Anthrax', 'Haemorrhagic Septicemia', 'Enterotoxaemia', 'Black Quarter', 'P.P.R.', 'Foot and Mouth Disease', 'Goat Pox', 'C.C.P.P', 'sold_date', 'sold_rate']
        return names

    def insertGoatRecord(self, values, mother_id):
        try:
            if mother_id == 'null':
                c.execute('INSERT INTO MasterTable (goat_no, breed, date_of_birth, gender, pregnant, weight, v1, v2, v3, v4, v5, v6, v7, v8) VALUES(:goat_id, :breed, :date_of_birth, :gender, :pregnant, :weight, :v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8)', values)
            else:
                c.execute('INSERT INTO MasterTable (goat_no, breed, date_of_birth, gender, pregnant, weight, v1, v2, v3, v4, v5, v6, v7, v8) VALUES(:goat_id, :breed, :date_of_birth, :gender, :pregnant, :weight, :curdate, :curdate, :curdate, :curdate, :curdate, :curdate, :curdate, :curdate)', values)
                # update mother id to have the kid id
                c.execute('INSERT INTO KidsTable VALUES(:mother_id, :kid_id, :gender)', {'mother_id': mother_id, 'kid_id': values['goat_id'], 'gender': values['gender']})
            
                # Updating number of kids
                c.execute('SELECT no_of_kids, no_of_male_kids, no_of_female_kids FROM MasterTable WHERE goat_no=:goat_id', {'goat_id': mother_id})
                res = c.fetchall()
                res = list(res[0]) if len(res) != 0 else [0, 0, 0]
                res[0] += 1
            
                c.execute('UPDATE MasterTable SET no_of_kids=:no_of_kids WHERE goat_no=:mother_id', {'no_of_kids': res[0], 'mother_id': mother_id})
                
                if values['gender'] == 'm':
                    res[1] += 1
                    c.execute('UPDATE MasterTable SET no_of_male_kids=:no_of_male_kids WHERE goat_no=:mother_id', {'no_of_male_kids': res[1], 'mother_id': mother_id})
                elif values['gender'] == 'f':
                    res[2] += 1
                    c.execute('UPDATE MasterTable SET no_of_female_kids=:no_of_female_kids WHERE goat_no=:mother_id', {'no_of_female_kids': res[2], 'mother_id': mother_id})

            # Updating mortality
            c.execute('UPDATE MasterTable SET mortality=\'Alive\' WHERE goat_no=:goat_id', {'goat_id': values['goat_id']})

            # Creating a weight table for the goat passed
            createStmt_WeightTable = 'weight INT, date_checked DATE'
            c.execute('CREATE TABLE WeightTable' +
                    str(values['goat_id']) + '(' + createStmt_WeightTable + ')')


            c.execute('INSERT INTO WeightTable' + str(values['goat_id']) + ' VALUES(:weight, :date_checked)', {
                    'weight': values['weight'], 'date_checked': datetime.date(datetime.now())})

            self.updateLiveStockNetworth(values)
        except:
            return Exception
        else:
            conn.commit()

        print('Inserted successfully')

    def updateLiveStockNetworth(self, values):

        exists = False
        # Get types of breeds present in LivestockNetworth      
        c.execute('SELECT breed, category FROM LivestockNetworth GROUP BY breed, category')
        result = c.fetchall()
        if len(result) != 0:
            exists = True

        # Checking if new goat is kid or adult
        c.execute('SELECT (julianday(:curdate) - julianday(:date_of_birth)) AS day WHERE day > 365 ', {'curdate': datetime.date(datetime.now()), 'date_of_birth': values['date_of_birth']})
        r = c.fetchall()
        age = 'Kid' if len(r) == 0 else 'Adult'
        # Determining the category of the new goat
        category = age + ' Male' if values['gender'] == 'm' else age + ' Female'

        if not exists:
            # Inserting the new record in LivestockNetworth
            c.execute('INSERT INTO LivestockNetworth(category, breed, cost, total_weight, total_cost) VALUES(:category, :breed, 0, :total_weight, 0)', {'category': category, 'breed': values['breed'], 'total_weight': values['weight']})
            conn.commit()
        else:
            for res in result:
                # Checking whether it already exists
                if res[0] == values['breed'] and res[1] == category:
                    # Getting total weight from the LivestockNetworth
                    c.execute('SELECT total_weight FROM LivestockNetworth WHERE breed=:breed AND category=:category', {'breed': res[0], 'category': res[1]})
                    total_weight = c.fetchall()[0][0] + values['weight']
                    # Update total weight in LivestockNetworth
                    c.execute('UPDATE LivestockNetworth SET total_weight=:total_weight WHERE breed=:breed AND category=:category', {'total_weight': total_weight, 'breed': res[0], 'category': res[1]})
                    conn.commit()
                    break
            else:
                # Inserting the new record in LivestockNetworth
                c.execute('INSERT INTO LivestockNetworth(category, breed, cost, total_weight, total_cost) VALUES(:category, :breed, 0, :total_weight, 0)', {'category': category, 'breed': values['breed'], 'total_weight': values['weight']})
                conn.commit()

    def getMaleKidID(self, mother_id):
        c.execute('SELECT kid_id FROM KidsTable WHERE mother_id = ' + mother_id + ' AND gender = \'m\'')
        res = c.fetchall()
        return res

    def getFemaleKidID(self, mother_id):
        c.execute('SELECT kid_id FROM KidsTable WHERE mother_id = ' + mother_id + ' AND gender = \'f\'')
        res = c.fetchall()
        return res

    def getMotherId(self, goat_no):
        c.execute('SELECT mother_id FROM KidsTable WHERE kid_id=:goat_id', {'goat_id': goat_no})
        res = c.fetchall()
        return res[0][0]

    # For Update Goat
    def updateGoatRecord(self, goatValues, isSold, isWeightUpdated):

        c.execute('UPDATE MasterTable SET mortality=:mortality, breed=:breed, date_of_birth=:dob WHERE goat_no=:goat_id', goatValues)
        conn.commit()

        if isSold:
            c.execute('UPDATE MasterTable SET sold_date=:sold_date, sold_rate=:sold_rate WHERE goat_no=:goat_id', goatValues)

        if isWeightUpdated:
            c.execute('UPDATE MasterTable SET weight=:weight WHERE goat_no=:goat_id', goatValues)
        
        if goatValues['pregnant'] == 'Yes':
            date_of_delivery = str(datetime.date(datetime.now()) + relativedelta(months=+5))
            c.execute('UPDATE MasterTable SET pregnant=:pregnant, date_of_delivery=:date_of_delivery WHERE goat_no=:goat_id', {'pregnant': goatValues['pregnant'], 'date_of_delivery': date_of_delivery, 'goat_id': goatValues['goat_id']})
        
        conn.commit()

        if isWeightUpdated:
            c.execute('INSERT INTO WeightTable' + str(goatValues['goat_id']) + ' values(:weight, :date_checked)', {'weight': goatValues['weight'], 'date_checked': str(datetime.date(datetime.now()))})
            conn.commit()

        conn.commit()

        print('Updated successfully')

    def updateVaccination(self, vacc_no, goat_id):
        if vacc_no == 1:
            c.execute('UPDATE MasterTable SET v1=? WHERE goat_no=?', (None, goat_id))
        if vacc_no == 2:
            c.execute('UPDATE MasterTable SET v2=? WHERE goat_no=?', (None, goat_id))
        if vacc_no == 3:
            c.execute('UPDATE MasterTable SET v3=? WHERE goat_no=?', (None, goat_id))
        if vacc_no == 4:
            c.execute('UPDATE MasterTable SET v4=? WHERE goat_no=?', (None, goat_id))
        if vacc_no == 5:
            c.execute('UPDATE MasterTable SET v5=? WHERE goat_no=?', (None, goat_id))
        if vacc_no == 6:
            c.execute('UPDATE MasterTable SET v6=? WHERE goat_no=?', (None, goat_id))
        if vacc_no == 7:
            c.execute('UPDATE MasterTable SET v7=? WHERE goat_no=?', (None, goat_id))
        if vacc_no == 8:
            c.execute('UPDATE MasterTable SET v8=? WHERE goat_no=?', (None, goat_id))
        conn.commit()

    # Alerts table
    def getGoatsToBeVaccinated(self, vacc_no):
        # TODO v3
        '''
            v1 - Anthrax
                    - Kid: 6 Months
                    - Adult: 1 Year
            v2 - Haemorrhagic Septicemia 
                    - Kid: 6 Months
                    - Adult: 1 Year
            v3 - Enterotoxaemia
                    - Kid: 4 Months
                    - Adult: 1 Year and 1 Year + 15 days
            v4 - Black Quarter 
                    - Kid: 6 Months
                    - Adult: 1 Year
            v5 - P.P.R.
                    - Kid: 3 Months
                    - Adult: 3 Year
            v6 - Foot & mouth disease
                    - Kid: 4 Months
                    - Adult: 6 Months
            v7 - Goat Pox
                    - Kid: 3 Months
                    - Adult: 1 Year
            v8 - C.C.P.P
                    - Kid: 3 Months
                    - Adult: 1 Year
        '''

        dates = list()

        if vacc_no == 1 or vacc_no == 2 or vacc_no == 4:
            # First checking for children
            c.execute('SELECT goat_no, v' + str(vacc_no) + ', date_of_birth FROM MasterTable WHERE (julianday(:curdate) - julianday(date_of_birth) <= 365)', {'curdate': datetime.date(datetime.now())})
            res = c.fetchall()
            for rec in res:
                if rec[1] != None:
                    newd = datetime.strptime(rec[1], '%Y-%m-%d').date() + relativedelta(months=+6)
                else:
                    newd = datetime.strptime(rec[2], '%Y-%m-%d').date() + relativedelta(months=+6)
                g_no = rec[0]
                # if datetime.today().month == newd.month and datetime.today().year == newd.year:
                dates.append([g_no, str(newd)])

            # checking for adults
            c.execute('SELECT goat_no, v' + str(vacc_no) + ', date_of_birth FROM MasterTable WHERE (julianday(:curdate) - julianday(date_of_birth) > 365)', {'curdate': datetime.date(datetime.now())})
            res = c.fetchall()
            for rec in res:
                if rec[1] != None:
                    newd = datetime.strptime(rec[1], '%Y-%m-%d').date() + relativedelta(years=1) 
                else:
                    dob = datetime.strptime(rec[2], '%Y-%m-%d').date()
                    toBeAdded = date.today() - dob
                    toBeAdded = toBeAdded.days
                    toBeAdded = ceil(toBeAdded / 365)
                    newd = dob + relativedelta(years=toBeAdded)
                g_no = rec[0]
                # if datetime.today().month == newd.month and datetime.today().year == newd.year:
                dates.append([g_no, str(newd)])
            dates.sort(key=lambda x: x[1])

        elif vacc_no == 3:
            # First checking for children
            c.execute('SELECT goat_no, v' + str(vacc_no) + ', date_of_birth FROM MasterTable WHERE (julianday(:curdate) - julianday(date_of_birth) <= 365)', {'curdate': datetime.date(datetime.now())})
            res = c.fetchall()
            for rec in res:
                if rec[1] != None:
                    newd = datetime.strptime(rec[1], '%Y-%m-%d').date() + relativedelta(months=+4)
                else:
                    newd = datetime.strptime(rec[2], '%Y-%m-%d').date() + relativedelta(months=+4)
                g_no = rec[0]
                # if datetime.today().month == newd.month and datetime.today().year == newd.year:
                dates.append([g_no, str(newd)])

            # checking for adults
            c.execute('SELECT goat_no, v' + str(vacc_no) + ', date_of_birth FROM MasterTable WHERE (julianday(:curdate) - julianday(date_of_birth) > 365)', {'curdate': datetime.date(datetime.now())})
            res = c.fetchall()
            for rec in res:
                if rec[1] != None:
                    newd1 = datetime.strptime(rec[1], '%Y-%m-%d').date() + relativedelta(years=1)
                else:
                    dob = datetime.strptime(rec[2], '%Y-%m-%d').date()
                    toBeAdded = date.today() - dob
                    toBeAdded = toBeAdded.days
                    toBeAdded = ceil(toBeAdded / 365)
                    newd1 = dob + relativedelta(years=toBeAdded)
                newd2 = newd1 + relativedelta(days=15)
                g_no = rec[0]
                # if datetime.today().month == newd.month and datetime.today().year == newd.year:
                dates.append([g_no, str(newd1)])
                dates.append([g_no, str(newd2)])
            dates.sort(key=lambda x: x[1])

        elif vacc_no == 5:
            # First checking for children
            c.execute('SELECT goat_no, v' + str(vacc_no) + ', date_of_birth FROM MasterTable WHERE (julianday(:curdate) - julianday(date_of_birth) <= 365)', {'curdate': datetime.date(datetime.now())})
            res = c.fetchall()
            for rec in res:
                if rec[1] != None:
                    newd = datetime.strptime(rec[1], '%Y-%m-%d').date() + relativedelta(months=+3)
                else:
                    newd = datetime.strptime(rec[2], '%Y-%m-%d').date() + relativedelta(months=+3)
                g_no = rec[0]
                # if datetime.today().month == newd.month and datetime.today().year == newd.year:
                dates.append([g_no, str(newd)])

            # checking for adults
            c.execute('SELECT goat_no, v' + str(vacc_no) + ', date_of_birth FROM MasterTable WHERE (julianday(:curdate) - julianday(date_of_birth) > 365)', {'curdate': datetime.date(datetime.now())})
            res = c.fetchall()
            for rec in res:
                if rec[1] != None:
                    newd = datetime.strptime(rec[1], '%Y-%m-%d').date() + relativedelta(years=3) 
                else:
                    dob = datetime.strptime(rec[2], '%Y-%m-%d').date()
                    toBeAdded = date.today() - dob
                    toBeAdded = toBeAdded.days
                    toBeAdded = ceil(toBeAdded / 365)
                    newd = dob + relativedelta(years=toBeAdded)
                g_no = rec[0]
                # if datetime.today().month == newd.month and datetime.today().year == newd.year:
                dates.append([g_no, str(newd)])
            dates.sort(key=lambda x: x[1])

        elif vacc_no == 6:
            # First checking for children
            c.execute('SELECT goat_no, v' + str(vacc_no) + ', date_of_birth FROM MasterTable WHERE (julianday(:curdate) - julianday(date_of_birth) <= 365)', {'curdate': datetime.date(datetime.now())})
            res = c.fetchall()
            for rec in res:
                if rec[1] != None:
                    newd = datetime.strptime(rec[1], '%Y-%m-%d').date() + relativedelta(months=+4)
                else:
                    newd = datetime.strptime(rec[2], '%Y-%m-%d').date() + relativedelta(months=+4)
                g_no = rec[0]
                # if datetime.today().month == newd.month and datetime.today().year == newd.year:
                dates.append([g_no, str(newd)])

            # checking for adults
            c.execute('SELECT goat_no, v' + str(vacc_no) + ', date_of_birth FROM MasterTable WHERE (julianday(:curdate) - julianday(date_of_birth) > 365)', {'curdate': datetime.date(datetime.now())})
            res = c.fetchall()
            for rec in res:
                if rec[1] != None:
                    newd = datetime.strptime(rec[1], '%Y-%m-%d').date() + relativedelta(years=3) 
                else:
                    dob = datetime.strptime(rec[2], '%Y-%m-%d').date()
                    toBeAdded = date.today() - dob
                    toBeAdded = toBeAdded.days
                    toBeAdded = toBeAdded / 365
                    if 0.5 > math.modf(toBeAdded)[0]:
                        toBeAdded = math.modf(toBeAdded)[1] + 0.5
                        toBeAdded *= 12
                    else:
                        toBeAdded = math.modf(toBeAdded)[1] + 1
                        toBeAdded *= 12
                    newd = dob + relativedelta(months=toBeAdded)
                g_no = rec[0]
                # if datetime.today().month == newd.month and datetime.today().year == newd.year:
                dates.append([g_no, str(newd)])
            dates.sort(key=lambda x: x[1])

        elif vacc_no == 7 or vacc_no == 8:
            c.execute('SELECT goat_no, v' + str(vacc_no) + ', date_of_birth FROM MasterTable WHERE (julianday(:curdate) - julianday(date_of_birth) <= 365)', {'curdate': datetime.date(datetime.now())})
            res = c.fetchall()
            for rec in res:
                if rec[1] != None:
                    newd = datetime.strptime(rec[1], '%Y-%m-%d').date() + relativedelta(months=+3)
                else:
                    newd = datetime.strptime(rec[2], '%Y-%m-%d').date() + relativedelta(months=+3)
                g_no = rec[0]
                # if datetime.today().month == newd.month and datetime.today().year == newd.year:
                dates.append([g_no, str(newd)])

            # checking for adults
            c.execute('SELECT goat_no, v' + str(vacc_no) + ', date_of_birth FROM MasterTable WHERE (julianday(:curdate) - julianday(date_of_birth) > 365)', {'curdate': datetime.date(datetime.now())})
            res = c.fetchall()
            for rec in res:
                if rec[1] != None:
                    newd = datetime.strptime(rec[1], '%Y-%m-%d').date() + relativedelta(years=1) 
                else:
                    dob = datetime.strptime(rec[2], '%Y-%m-%d').date()
                    toBeAdded = date.today() - dob
                    toBeAdded = toBeAdded.days
                    toBeAdded = ceil(toBeAdded / 365)
                    newd = dob + relativedelta(years=toBeAdded)
                g_no = rec[0]
                # if datetime.today().month == newd.month and datetime.today().year == newd.year:
                dates.append([g_no, str(newd)])
            dates.sort(key=lambda x: x[1])

        return dates

    def getVaccinationDates(self, goat_no):
        c.execute('SELECT v1, v2, v3, v4, v5, v6, v7, v8 FROM MasterTable WHERE goat_no=:goat_id', {'goat_id': goat_no})
        res = c.fetchall()
        return res[0]

    def getDeliveryDates(self):
        c.execute('SELECT goat_no, date_of_delivery FROM MasterTable')
        res = c.fetchall()
        dates = list()
        for rec in res:
            if rec[1] != None:
                dates.append(rec)
        dates.sort(key=lambda x: x[1], reverse=True)
        return dates

    def getBreedReadyGoats(self):
        c.execute('SELECT goat_no, breed FROM MasterTable WHERE (julianday(:curdate) - julianday(date_of_birth) > 365)AND ((julianday(:curdate) - julianday(date_of_delivery) > 90)OR(pregnant=\'No\')) AND(gender=\'f\')' , {'curdate': datetime.date(datetime.now())})
        res = c.fetchall()
        return res

    def vaccinateGoats(self, vacc_no):
        dates = self.getGoatsToBeVaccinated(vacc_no)
        if dates != None:
            for i in range(len(dates)):
                if datetime.strptime(dates[i][1], '%Y-%m-%d').date() <= datetime.date(datetime.now()):
                    c.execute('UPDATE MasterTable SET v' + str(vacc_no) + '=:curdate WHERE goat_no=:goat_id', {'curdate': str(datetime.date(datetime.now())), 'goat_id': dates[i][0]})
            conn.commit()

    # For View goat
    def getKidsTableData(self, goat_no):
        c.execute('SELECT * FROM KidsTable WHERE mother_id=:goat_id', {'goat_id': goat_no})
        res = c.fetchall()
        return res


    # For Finance Window

    # LivestockNetworth Table
    def insertLiveStockNetworth(self, networthValues):
        c.execute('UPDATE LivestockNetworth SET cost=:cost WHERE category=:category AND breed=:breed AND total_weight=:total_weight', networthValues)
        total_cost = networthValues['cost'] * networthValues['total_weight']
        networthValues['total_cost'] = total_cost
        c.execute('UPDATE LivestockNetworth SET total_cost=:total_cost WHERE category=:category AND breed=:breed AND total_weight=:total_weight AND cost=:cost', networthValues)
        conn.commit()

    def getTotalLivestockNetworth(self):
        c.execute('SELECT SUM(total_cost) FROM LivestockNetworth')
        res = c.fetchall()
        if res[0][0] != None:
            return res[0][0]
        else:
            return 0
    
    def getLivestockNetworthData(self):
        c.execute('SELECT * FROM LivestockNetworth')
        res = c.fetchall()
        return res

    # Labour Table
    def insertLabour(self, labourValues):
        no_of_days = 30
        c.execute('INSERT INTO Labour(category, salary, count) VALUES(:category, :salary, :count)', labourValues)
        monthly_total = int(labourValues['count']) * int(labourValues['salary']) * no_of_days
        c.execute('UPDATE Labour SET monthly_total=:monthly_total WHERE category=:category AND salary=:salary AND count=:count', {'monthly_total': monthly_total, 'category': labourValues['category'], 'salary': labourValues['salary'], 'count': labourValues['count']})
        conn.commit()

    def getLabourData(self):
        c.execute('SELECT * FROM Labour')
        res = c.fetchall()
        return res
    
    def getTotalLabourCost(self):
        c.execute('SELECT SUM(monthly_total) FROM Labour')
        res = c.fetchall()
        if res[0][0] != None:
            return res[0][0]
        else:
            return 0
    
    def deleteLabourRecord(self, labourValues):
        c.execute('DELETE FROM Labour WHERE category=:category AND salary=:salary AND count=:count', labourValues)
        conn.commit()

    # Feed Table
    def insertFeed(self, feedValues):
        total_cost = int(feedValues['cost']) * int(feedValues['weight'])
        c.execute('INSERT INTO Feed(item, weight, cost) VALUES(:item, :weight, :cost)',feedValues)
        c.execute('UPDATE Feed SET total_cost=:total_cost, purchase_date=:purchase_date WHERE item=:item AND weight=:weight AND cost=:cost', {'total_cost': total_cost, 'item': feedValues['item'], 'purchase_date': datetime.date(datetime.now()), 'cost': feedValues['cost'], 'weight': feedValues['weight']})
        conn.commit()

    def getFeedData(self):
        c.execute('SELECT * FROM Feed')
        res = c.fetchall()
        return res

    def getTotalFeedCost(self):
        c.execute('SELECT SUM(total_cost) FROM Feed')
        res = c.fetchall()
        if res[0][0] != None:
            return res[0][0]
        else:
            return 0

    def deleteFeedRecord(self, feedValues):
        c.execute('DELETE FROM Feed WHERE purchase_date=:purchase_date AND item=:item AND weight=:weight AND cost=:cost', feedValues)
        conn.commit()

    # MiscExpense Table
    def insertMiscExpenditure(self, miscExpenseValue):
        c.execute('INSERT INTO MiscExpense(category, cost) VALUES(:category, :cost)', miscExpenseValue)
        c.execute('UPDATE MiscExpense SET purchase_date=:purchase_date WHERE category=:category AND cost=:cost', {'purchase_date': datetime.date(datetime.now()), 'category': miscExpenseValue['category'], 'cost': miscExpenseValue['cost']})
        conn.commit()

    def getTotalMiscExpenditure(self):
        c.execute('SELECT SUM(cost) FROM MiscExpense')
        res = c.fetchall()
        if res[0][0] != None:
            return res[0][0]
        else:
            return 0

    def getMiscExpenditureData(self):
        c.execute('SELECT * FROM MiscExpense')
        res = c.fetchall()
        return res

    def deleteMiscExpenditureRecord(self, miscExpenseValues):
        c.execute('DELETE FROM MiscExpense WHERE purchase_date=:purchase_date AND category=:category AND cost=:cost', miscExpenseValues)
        conn.commit()


    # Income Table
    def insertIncome(self, incomeValues):
        c.execute('INSERT INTO Income(details, cost) VALUES(:details, :cost)', incomeValues)
        c.execute('UPDATE Income SET purchase_date=:purchase_date WHERE details=:details AND cost=:cost', {'purchase_date': datetime.date(datetime.now()), 'details': incomeValues['details'], 'cost': incomeValues['cost']})
        conn.commit()
    
    def getTotalIncome(self):
        c.execute('SELECT SUM(cost) FROM Income')
        res = c.fetchall()
        if res[0][0] != None:
            return res[0][0]
        else:
            return 0

    def getIncomeData(self):
        c.execute('SELECT * FROM Income')
        res = c.fetchall()
        return res

    def deleteIncomeRecord(self, incomeValues):
        c.execute('DELETE FROM Income WHERE purchase_date=:purchase_date AND details=:details AND cost=:cost', incomeValues)
        conn.commit()

    # Graph 
    def getWeightRecords(self, goat_id):
        c.execute('SELECT * FROM WeightTable' +str(goat_id))
        return c.fetchall()

    def getWeightColumnNames(self, goat_id):
        c.execute('SELECT * FROM WeightTable'+str(goat_id))
        names = [description[0] for description in c.description]
        return names

    def getKidCount(self):
        c.execute('SELECT count(goat_no),gender FROM MasterTable where (julianday(:dob) - julianday(date_of_birth) ) <= 365 GROUP BY gender', {'dob': datetime.date(datetime.now())})
        return c.fetchall()

    def getDeadCount(self):
        c.execute('SELECT count(goat_no),gender FROM MasterTable where mortality=\'Dead\' GROUP BY gender')
        return c.fetchall()

    def getTotalSoldGoatsRate(self):
        c.execute('SELECT SUM(sold_rate) FROM MasterTable WHERE sold_rate != \'None\'')
        res = c.fetchall()
        res = res[0][0] if res[0][0] != None else 0
        return res

    # Excel
    def getKidRecords(self):
        c.execute('SELECT * FROM KidsTable')
        return c.fetchall()

    def getKidColumnNames(self):
        c.execute('SELECT * FROM KidsTable')
        names = [description[0] for description in c.description]
        return names

    def getLivestockRecords(self):
        c.execute('SELECT * FROM LivestockNetworth')
        return c.fetchall()

    def getLivestockColumnNames(self):
        c.execute('SELECT * FROM LivestockNetworth')
        names = [description[0] for description in c.description]
        return names

    def getLabourRecords(self):
        c.execute('SELECT * FROM Labour')
        return c.fetchall()

    def getLabourColumnNames(self):
        c.execute('SELECT * FROM Labour')
        names = [description[0] for description in c.description]
        return names

    def getFeedRecords(self):
        c.execute('SELECT * FROM Feed')
        return c.fetchall()

    def getFeedColumnNames(self):
        c.execute('SELECT * FROM Feed')
        names = [description[0] for description in c.description]
        return names

    def getMiscRecords(self):
        c.execute('SELECT * FROM MiscExpense')
        return c.fetchall()

    def getMiscColumnNames(self):
        c.execute('SELECT * FROM MiscExpense')
        names = [description[0] for description in c.description]
        return names

    def getIncomeRecords(self):
        c.execute('SELECT * FROM Income')
        return c.fetchall()

    def getIncomeColumnNames(self):
        c.execute('SELECT * FROM Income')
        names = [description[0] for description in c.description]
        return names