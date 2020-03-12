import pandas as pd
from backend import DataBase

db = DataBase()
data = db.getGoatRecords()
dataColumns = db.getColumnNames()
df = pd.DataFrame(data,columns=dataColumns)

birth = df['no_of_kids'].sum()
death = 0
for i in df['mortality']:
	if(i==0):
		death+=1

breed1 = 0
for i in df['breed']:
	if i == 'some':
		breed1+=1
breed2 = 0
for i in df['breed']:
	if i == 'somethi':
		breed2+=1
gender = df['gender']
male = 0
female = 0
for i in gender:
	if (i == 0):
		male+=1
	elif (i == 1):
		female+=1

def getfemale():
	return female
def getmale():
	return male
def getbreed1():
	return breed1
def getbreed2():
	return breed2
def getBirth():
	return birth
def getDeath():
	return death

# print(gender)