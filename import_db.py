__author__ = 'Yuer'

import xlrd
import MySQLdb

category = xlrd.open_workbook("data_import.xls")
sheet_industry = category.sheet_by_name("industry")
sheet_channel = category.sheet_by_name("channel")
sheet_metrics = category.sheet_by_name("pricemetrics")

# establish a mysql connection
# database = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "self_service")
database = MySQLdb.connect(host = "ads-in-china.com", user = "self_service", passwd = "cmbjxccwtn", db = "self_service")
# get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

query_industry = """INSERT INTO budget_allocation_industry (industryId,industryName,subIndustry) VALUES(%s, %s, %s)"""
query_channel = """INSERT INTO budget_allocation_channel (channelId, channelName, channelUrl, channelDescription, minMediaBuy) VALUES(%s, %s, %s, %s, %s)"""
query_metrics = """INSERT INTO budget_allocation_pricemetrics (priceMatrixId,allocation,budget,budgetPercentage,expectedClicks,
           costPerClick,expectedImpressions,costPerImpression,campaignGoal,industryId,channelId)
           VALUES(%s,%s, %s, %s,%s, %s, %s,%s, %s, %s ,%s)"""

def convert(func, val):
    try:
        return func(val)
    except ValueError:
        return None

# import industry data to db
for i in range(1, sheet_industry.nrows):
    industryId = int(sheet_industry.cell(i,0).value)
    industryName = sheet_industry.cell(i, 1).value
    subIndustry = sheet_industry.cell(i, 2).value
    # assign values from each row
    values_industry = (industryId, industryName, subIndustry)

    print values_industry
    cursor.execute(query_industry, values_industry)

# import channel data to db
for i in range(1, sheet_channel.nrows):
    channelId = int(sheet_channel.cell(i,0).value)
    channelName = sheet_channel.cell(i, 1).value
    channelUrl = sheet_channel.cell(i, 2).value
    channelDescription = sheet_channel.cell(i, 3).value
    minMediaBuy = sheet_channel.cell(i, 4).value
    if minMediaBuy == '':
        minMediaBuy = None
    # assign values from each row
    values_channel = (channelId, channelName, channelUrl, channelDescription, minMediaBuy)

    print values_channel
    cursor.execute(query_channel, values_channel)

# import pricemetrics data to db
types = [ int, int, int, float, int, float, int, int, str, int, int ]
for i in range(1, sheet_metrics.nrows):
    args_metrics = []
    for j in range(0, 11):
        args_metrics.append(convert(types[j], sheet_metrics.cell(i, j).value))

    print args_metrics
    cursor.execute(query_metrics, args_metrics)

cursor.close()
database.commit()
database.close()