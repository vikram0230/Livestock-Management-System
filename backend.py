import os
import sqlite3
from datetime import datetime, date
from _datetime import timedelta

# Create DB file if not present already in the same directory
if not (os.path.isfile('data.db')):

    """
        Tables initialised:
            - MasterTable
            - WeightTable
            - KidsIdTable
            - LivestockNetwork
            - Labour
            - Feed
            - HealthExpense
            - Misc
    """

    with open('data.db', 'w') as f:
        conn = sqlite3.connect('data.db')

        c = conn.cursor()

        createStmt_MasterDatabase = 'goat_no INTEGER PRIMARY KEY, breed TEXT, date_of_birth DATE, gender BOOLEAN, pregnant BOOLEAN, weight INT, date_of_delivery DATE, no_of_kids INT, no_of_male_kids INT, no_of_female_kids INT, mortality INT, v1 DATE, v2 DATE, v3 DATE, v4 DATE, v5 DATE, v6 DATE, sold_date DATE, sold_rate INT'
        c.execute('CREATE TABLE MasterTable(' + createStmt_MasterDatabase + ')')
        conn.commit()

        createStmt_KidsTable = 'mother_id INT, kid_id INT, gender BOOLEAN'
        c.execute('CREATE TABLE KidsTable(' + createStmt_KidsTable + ')')
        conn.commit()

        createStmt_LivestockNetworth = 's_no INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, breed TEXT, cost DOUBLE, total_weight INT, total_cost DOUBLE'
        c.execute('CREATE TABLE LivestockNetworth(' + createStmt_LivestockNetworth + ')')
        conn.commit()

        createStmt_Labour = 'category TEXT,salary INT, count INT, monthly_total INT'
        c.execute('CREATE TABLE Labour(' + createStmt_Labour + ')')
        conn.commit()

        createStmt_Feed = 'purchase_date DATE, item TEXT, weight INT, cost INT, total_cost INT'
        c.execute('CREATE TABLE Feed(' + createStmt_Feed + ')')
        conn.commit()

        createStmt_HealthExpense = 'purchase_date DATE, category TEXT, cost INT'
        c.execute('CREATE TABLE HealthExpense(' + createStmt_HealthExpense + ')')
        conn.commit()

        createStmt_Misc = 'purchase_date DATE, details TEXT, cost INT'
        c.execute('CREATE TABLE Misc(' + createStmt_Misc + ')')
        conn.commit()

        values = [
            1, 'some', date(2001, 12, 21), '0', '0', 10, 0, 0, 0, 1
        ]

        for i in range(0, 50):
            c.execute(
                "INSERT INTO MasterTable(goat_no, breed, date_of_birth, gender, pregnant, weight, no_of_kids, no_of_male_kids, no_of_female_kids, mortality) values(?,?,?,?,?,?,?,?,?,?)", values)
            values[0] += 1
            conn.commit()

conn = sqlite3.connect('data.db')

c = conn.cursor()


class DataBase:
    def __init__(self):
        pass

    def getGoatRecords(self):
        c.execute('SELECT * FROM MasterTable')
        return c.fetchall()

    def getNumberOfRecords(self):
        c.execute('SELECT COUNT(*) FROM MasterTable')
        return (c.fetchall())

    def getColumnNames(self):
        c.execute('SELECT * FROM MasterTable')
        names = [description[0] for description in c.description]
        return names

    def insertGoatRecord(self, values, mother_id):
        if mother_id == 'null':
            c.execute('INSERT INTO MasterTable (goat_no, breed, date_of_birth, gender, pregnant, weight, v1, v2, v3, v4, v5, v6) VALUES(:goat_id, :breed, :date_of_birth, :gender, :pregnant, :weight, :v1, :v2, :v3, :v4, :v5, :v6)', values)
        else:
            c.execute('INSERT INTO MasterTable (goat_no, breed, date_of_birth, gender, pregnant, weight) VALUES(:goat_id, :breed, :date_of_birth, :gender, :pregnant, :weight)', values)
            # update mother id to have the kid id
            c.execute('INSERT INTO KidsTable VALUES(:mother_id, :kid_id, :gender)', {'mother_id': mother_id, 'kid_id': values['goat_id'], 'gender': values['gender']})
        
            # Updating number of kids
            c.execute('SELECT no_of_kids, no_of_male_kids, no_of_female_kids FROM MasterTable WHERE goat_no=:goat_id', {'goat_id': mother_id})
            res = c.fetchall()
            res = list(res[0])
            res[0] += 1
        
            c.execute('UPDATE MasterTable SET no_of_kids=:no_of_kids WHERE goat_no=:mother_id', {'no_of_kids': res[0], 'mother_id': mother_id})
            
            if values['gender'] == 0:
                res[1] += 1
                c.execute('UPDATE MasterTable SET no_of_male_kids=:no_of_male_kids WHERE goat_no=:mother_id', {'no_of_male_kids': res[1], 'mother_id': mother_id})
            elif values['gender'] == 1:
                res[2] += 1
                c.execute('UPDATE MasterTable SET no_of_female_kids=:no_of_female_kids WHERE goat_no=:mother_id', {'no_of_female_kids': res[2], 'mother_id': mother_id})


        conn.commit()

        # Updating mortality
        c.execute('UPDATE MasterTable SET mortality=1 WHERE goat_no=:goat_id', {'goat_id': values['goat_id']})
        conn.commit()

        # Creating a weight table for the goat passed
        createStmt_WeightTable = 'weight INT, date_checked DATE'
        c.execute('CREATE TABLE WeightTable' +
                  str(values['goat_id']) + '(' + createStmt_WeightTable + ')')

        conn.commit()

        c.execute('INSERT INTO WeightTable' + str(values['goat_id']) + ' VALUES(:weight, :date_checked)', {
                  'weight': values['weight'], 'date_checked': datetime.date(datetime.now())})

        conn.commit()

        print('Inserted successfully')

    def getMaleKidID(self, mother_id):
        c.execute('SELECT kid_id FROM KidsTable WHERE mother_id = ' + mother_id + ' AND gender = 0')
        res = c.fetchall()
        return res

    def getFemaleKidID(self, mother_id):
        c.execute('SELECT kid_id FROM KidsTable WHERE mother_id = ' + mother_id + ' AND gender = 1')
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
        
        date_of_delivery = str(datetime.date(datetime.now()) + timedelta(days=150))
        if goatValues['pregnant'] == 1:
            c.execute('UPDATE MasterTable SET pregnant=:pregnant, date_of_delivery=:date_of_delivery WHERE goat_no=:goat_id', {'pregnant': goatValues['pregnant'], 'date_of_delivery': date_of_delivery, 'goat_id': goatValues['goat_id']})
        
        conn.commit()

        if isWeightUpdated:
            c.execute('INSERT INTO WeightTable' + str(goatValues['goat_id']) + ' values(:weight, :date_checked)', {'weight': goatValues['weight'], 'date_checked': str(datetime.date(datetime.now()))})
            conn.commit()

        conn.commit()

        print('Updated successfully')

    def updateVaccination(self, vacc_no, goat_id):
        time = {'v': str(datetime.date(datetime.now())), 'goat_id': goat_id}
        if vacc_no == 1:
            c.execute('UPDATE MasterTable SET v1=:v WHERE goat_no=:goat_id', time)
        if vacc_no == 2:
            c.execute('UPDATE MasterTable SET v2=:v WHERE goat_no=:goat_id', time)
        if vacc_no == 3:
            c.execute('UPDATE MasterTable SET v3=:v WHERE goat_no=:goat_id', time)
        if vacc_no == 4:
            c.execute('UPDATE MasterTable SET v4=:v WHERE goat_no=:goat_id', time)
        if vacc_no == 5:
            c.execute('UPDATE MasterTable SET v5=:v WHERE goat_no=:goat_id', time)
        if vacc_no == 6:
            c.execute('UPDATE MasterTable SET v6=:v WHERE goat_no=:goat_id', time)
        conn.commit()

    # Alerts table
    def getGoatsToBeVaccinated(self, vacc_no):
        c.execute('SELECT goat_no, v' + str(vacc_no) + ' FROM MasterTable WHERE v' + str(vacc_no) + ' > ' + str(datetime.date(datetime.now())))
        res = c.fetchall()
        dates = list()
        for rec in res:
            newd = datetime.strptime(rec[1], '%Y-%m-%d').date() + timedelta(days=30)
            g_no = rec[0]
            dates.append([g_no, str(newd)])
        dates.sort(key=lambda x: x[1], reverse=True)
        return dates

    def getVaccinationDates(self, goat_no):
        c.execute('SELECT v1, v2, v3, v4, v5, v6 FROM MasterTable WHERE goat_no=:goat_id', {'goat_id': goat_no})
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


    # For View goat
    def getKidsTableData(self, goat_no):
        c.execute('SELECT * FROM KidsTable WHERE mother_id=:goat_id', {'goat_id': goat_no})
        res = c.fetchall()
        return res

    # For Finance Window

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
        return res[0][0]
    
    def deleteLabourRecord(self, labourValues):
        c.execute('DELETE FROM Labour WHERE category=:category AND salary=:salary AND count=:count')
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
        return res[0][0]

    def deleteFeedRecord(self, feedValues):
        c.execute('DELETE FROM Feed WHERE purchase_date=:purchase_date AND item=:item AND weight=:weight AND cost=:cost', feedValues)
        conn.commit()

    # HealthExpense Table
    def insertHealthExpenditure(self, healthExpenseValue):
        c.execute('INSERT INTO HealthExpense(category, cost) VALUES(:category, :cost)', healthExpenseValue)
        c.execute('UPDATE HealthExpense SET purchase_date=:purchase_date WHERE category=:category AND cost=:cost', {'purchase_date': datetime.date(datetime.now()), 'category': healthExpenseValue['category'], 'cost': healthExpenseValue['cost']})
        conn.commit()

    def getTotalHealthExpenditure(self):
        c.execute('SELECT SUM(cost) FROM HealthExpense')
        res = c.fetchall()
        return res[0][0]

    def getHealthExpenditureData(self):
        c.execute('SELECT * FROM HealthExpense')
        res = c.fetchall()
        return res

    def deleteHealthExpenditureRecord(self, healthExpenseValues):
        c.execute('DELETE FROM HealthExpense WHERE purchase_date=:purchase_date AND category=:category AND cost=:cost', healthExpenseValues)
        conn.commit()


    # Misc Table
    def insertMisc(self, miscValues):
        c.execute('INSERT INTO Misc(details, cost) VALUES(:details, :cost)', miscValues)
        c.execute('UPDATE Misc SET purchase_date=:purchase_date WHERE details=:details AND cost=:cost', {'purchase_date': datetime.date(datetime.now()), 'details': miscValues['details'], 'cost': miscValues['cost']})
        conn.commit()
    
    def getTotalMiscCost(self):
        c.execute('SELECT SUM(cost) FROM Misc')
        res = c.fetchall()
        return res[0][0]

    def getMiscData(self):
        c.execute('SELECT * FROM Misc')
        res = c.fetchall()
        return res

    def deleteMiscRecord(self, miscValues):
        c.execute('DELETE FROM Misc WHERE purchase_date=:purchase_date AND details=:details AND cost=:cost', miscValues)
        conn.commit()

    # Networth Table
    def getNetworthData(self):
        # c.execute('SELECT goat_no, breed, SUM(weight) FROM MasterTable GROUP BY(breed) HAVING gender=0 AND breed IN (SELECT breed FROM MasterTable WHERE :curdate - date_of_birth > 1)', {'curdate': datetime.date(datetime.now())})
        # print(c.fetchall())
        # c.execute('SELECT goat_no, breed, SUM(weight) FROM MasterTable GROUP BY(breed) HAVING gender=1 AND breed IN (SELECT breed FROM MasterTable WHERE :curdate - date_of_birth > 1)', {'curdate': datetime.date(datetime.now())})
        # print(c.fetchall())
        # c.execute('SELECT goat_no, breed, SUM(weight) FROM MasterTable GROUP BY(breed) HAVING gender=0 AND breed IN (SELECT breed FROM MasterTable WHERE :curdate - date_of_birth < 1)', {'curdate': datetime.date(datetime.now())})
        # print(c.fetchall())
        # c.execute('SELECT goat_no, breed, SUM(weight) FROM MasterTable GROUP BY(breed) HAVING gender=1 AND breed IN (SELECT breed FROM MasterTable WHERE :curdate - date_of_birth < 1)', {'curdate': datetime.date(datetime.now())})
        # print(c.fetchall())

        # ------------------------------------------------------------------------------------------------#
        # To use this function, create an instance of this class in another dummy file and execute this function to see the results easily #
        # ------------------------------------------------------------------------------------------------#
        # julianday(:curdate) - julianday(date_of_birth) returns the number of days between the two dates #
        # ------------------------------------------------------------------------------------------------#
        # Code works for kid and adult male, kid female goats. It DOES NOT work for adult female goat #
        # ------------------------------------------------------------------------------------------------#
        c.execute('SELECT breed, sum(weight), gender FROM MasterTable GROUP BY breed, gender HAVING (julianday(:curdate) - julianday(date_of_birth)) > 365 AND gender = 1 OR gender = 0', {'curdate': datetime.date(datetime.now())})
        print(c.fetchall())
        c.execute('SELECT breed, sum(weight), gender FROM MasterTable GROUP BY breed, gender HAVING (julianday(:curdate) - julianday(date_of_birth)) < 365', {'curdate': datetime.date(datetime.now())})
        print(c.fetchall())