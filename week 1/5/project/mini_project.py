"""
1. Please import csv (or) openpyxl & Logging packages for this problem.
2. Program should take any filename as per the format mentioned as input.
3. Input month value from the file name where  eg :january(expedia_report_monthly_january_2018.xlsx)
4. Based on the month and year input values value print the values in logfile using logger

This is from the first tab :

Eg for January :

Calls Offered: 16,915
Abandon after 30s : 2.32%
FCR : 86.50%
DSAT :  14.20%
CSAT : 78.30%

Similarly go to "VOC Rolling MoM" tab

Grab all the values related to Jan-18 and print.

In Net Promoter Score : Promoters > 200 : good Promoters <200 : bad
			Passives > 100 : good Passives <100 : bad
			Decractors > 100 : good Decrators <100 : bad

Rest all values remain the same.
"""

from openpyxl import load_workbook
import logging
import os
import streamlit as st

logging.basicConfig(filename='log.log',filemode='w',format='%(asctime)s - %(levelname)s %(message)s',datefmt='%H:%M:%S', encoding='utf-8', level=logging.DEBUG)

files = os.listdir('./data')
workbooks = [item for item in files if '.xlsx' in item]

months = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07',
          'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12', 'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07',
          'Aug': '08', 'Sep': '09', 'Oc': '10', 'Nov': '11', 'Dec': '12'}
years = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']

workbook_selector = 'expedia_report_monthly_january_2018.xlsx'

while True:
    try:
        file = f'data/{workbook_selector}'
        if os.path.exists(file):
            wb = load_workbook(file)
            break
    except FileNotFoundError:
        print("FileNotFound: not a valid file.")
    else:
        continue

for sheet in wb:
    print (sheet)

# grab worksheet

# iterate through rows and get data


# for row in ws.iter_rows(min_row=2, max_row=15):
#         row_id: datetime = row[0].value
#         if row_id.month == date.month and row_id.year == date.year:
#             log.info(f"{header[1].value.strip()}: {row[1].value:,}")
            
#             for i in range(2, 6):
#                 percentage = row[i].value * 100
#                 log.info(f"{header[i].value.strip()}: {percentage:.2f}%")
                
#             break

# the iter_row() is a generator
# so you gotta use list(worksheet_name.iter_row())