__author__ = 'Yuer'

import xlrd
import MySQLdb

category = xlrd.open_workbook("data_import.xls")
# sheet = category.sheet_by_name("industry")
sheet = category.sheet_by_name("pricemetrics")

# establish a mysql connection
database = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "self_service")

# get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# query = """INSERT INTO budget_allocation_industry (industryId,industryName,subIndustry) VALUES(%s, %s, %s)"""
query = """INSERT INTO budget_allocation_pricemetrics (priceMatrixId,allocation,budget,budgetPercentage,expectedClicks,
           costPerClick,expectedImpressions,costPerImpression,campaignGoal,industryId,channelId)
           VALUES(%s,%s, %s, %s,%s, %s, %s,%s, %s, %s ,%s)"""

def convert(func, val):
    try:
        return func(val)
    except ValueError:
        return None

types = [ int, int, int, float, int, float, int, int, str, int, int ]
for i in range(1, sheet.nrows):
    args = []
    # industryId = int(sheet.cell(i,0).value)
    # industryName = sheet.cell(i, 1).value
    # subIndustry = sheet.cell(i, 2).value
    for j in range(0, 11):
        args.append(convert(types[j], sheet.cell(i, j).value))
    # priceMatrixId = int(sheet.cell(i,0).value)
    # allocation = convert(int, sheet.cell(i, 1).value)
    # budget = convert(int, sheet.cell(i, 2).value)
    # budgetPercentage = convert(float,sheet.cell(i, 3).value)
    # expectedClicks = convert(int, sheet.cell(i, 4).value)
    # costPerClick = convert(float,sheet.cell(i, 5).value)
    # expectedImpressions = convert(int, sheet.cell(i, 6).value)
    # costPerImpression = convert(int, sheet.cell(i, 7).value)
    # campaignGoal = sheet.cell(i, 8).value
    # industryId = int(sheet.cell(i, 9).value)
    # channelId = int(sheet.cell(i, 10).value)

    # assign values from each row
    # values = (priceMatrixId, allocation, budget, budgetPercentage, expectedClicks, costPerClick, expectedImpressions, costPerImpression, campaignGoal, industryId, channelId)
    print args
    cursor.execute(query, args)

cursor.close()
database.commit()
database.close()