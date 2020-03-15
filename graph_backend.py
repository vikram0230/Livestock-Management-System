import pandas as pd
from backend import DataBase
from datetime import datetime, datetime


def getData():
	db = DataBase()
	data = db.getGoatRecords()
	dataColumns = db.getColumnNames()
	df = pd.DataFrame(data,columns=dataColumns)

	breed = df['breed']
	gender = df['gender']

	kidCount = db.getKidCount()
	maleKidCount = 0
	femaleKidCount = 0

	if len(kidCount)>1:
		if kidCount[0][1] == 'm':
			maleKidCount = kidCount[0][0]
			femaleKidCount = kidCount[1][0]
		else:
			maleKidCount = kidCount[1][0]
			femaleKidCount = kidCount[0][0]
	elif len(kidCount)==1:
		if kidCount[0][1] == 'm':
			maleKidCount = kidCount[0][0]
		else:
			femaleKidCount = kidCount[0][0]
	else:
		maleKidCount = 0
		femaleKidCount = 0

	deadCount = db.getDeadCount()
	maleDeadCount = 0
	femaleDeadCount = 0

	if len(deadCount)>1:
		if deadCount[0][1] == 'm':
			maleDeadCount = deadCount[0][0]
			femaleDeadCount = deadCount[1][0]
		else:
			maleDeadCount = deadCount[1][0]
			femaleDeadCount = deadCount[0][0]
	elif len(deadCount)==1:
		if deadCount[0][1] == 'm':
			maleDeadCount = deadCount[0][0]
		else:
			femaleDeadCount = deadCount[0][0]
	else:
		maleDeadCount = 0
		femaleDeadCount = 0

	income = db.getTotalIncome()+db.getTotalSoldGoatsRate()
	expense = db.getTotalLabourCost()+db.getTotalFeedCost()+db.getTotalMiscExpenditure()

	db = None
	return breed, gender, maleKidCount, femaleKidCount, maleDeadCount, femaleDeadCount, income, expense



