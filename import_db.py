__author__ = 'Yuer'

import xlrd
import MySQLdb

category = xlrd.open_workbook("data_import.xls")
sheet = category.sheet_by_name("industry")

# establish a mysql connection
database = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "self_service")

# get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

query = """INSERT INTO budget_allocation_industry (industryId,industryName,subIndustry) VALUES(%s, %s, %s)"""

for i in range(1, sheet.nrows):
    industryId = int(sheet.cell(i,0).value)
    industryName = sheet.cell(i, 1).value
    subIndustry = sheet.cell(i, 2).value

    # assign values from each row
    values = (industryId, industryName, subIndustry)
    print values
    cursor.execute(query, values)

cursor.close()
database.commit()
database.close()