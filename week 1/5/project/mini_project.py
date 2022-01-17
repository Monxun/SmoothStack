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
from openpyxl.utils import get_column_letter
from datetime import datetime
import logging
import os
import streamlit as st
import pandas as pd
from services import files, workbooks, logger, months, years, check_file, log_data, show_data, get_current, get_summary


#####################################################
#NAVIGATION

# streamlit title for page
st.title('Spreadsheet Mini-Project')
pages = ['Select by File', 'Current Month', 'Log Files']
navigation = st.selectbox('Select a page', pages)

st.write('_' * 30)

st.header(navigation)

data_flag = False

if navigation != 'Log Files':

    if navigation == 'Select by File':

        #####################################################
        #SELECT FILE

        # workbook file selectbox 
        workbook_selector = st.selectbox('Select a file', workbooks)  # replace with streamlit selector 

        # verify file exists / error handling
        check_file(workbook_selector)

        # if file selected display text
        if workbook_selector:
            st.text(f'({workbook_selector} is selected.)')

        # initialize workbook
        wb = load_workbook(f'data/{workbook_selector}')

        # grab month and year from file selection
        month_year = [item for item in workbook_selector.replace('.', '_').split("_") if item.capitalize() in months or item in years]

        # display month / year
        st.text(f'Month: {month_year[0].capitalize()}')
        st.text(f'Year: {month_year[1]}')

        # format month year for datetime comparison
        month_year_format = f'{month_year[1]}-{months[month_year[0].capitalize()]}'

        # data flag

        data_flag = True

        st.write('_' * 30)
        st.subheader(f'Data for {month_year[0].capitalize()} - {month_year[1]}')


    if navigation == 'Current Month':

        #####################################################
        #CURRENT MONTH

        data_flag = False

        month, month_word, year = get_current()
        st.write(f'{month_word}, {year}')
        current_files = []

        for book in workbooks:
            if month or month_word and year in book.replace('.', '_').split("_"):
                print(book)
                current_files.append(book)
                # data_flag = True
                

        if current_files:
            # initialize workbook
            wb = load_workbook(f'data/{current_files[0]}')

        st.subheader(f'Data for {month_word} - {year}')


    if navigation == 'Select by File' or data_flag == True:

        #####################################################
        #DATA

        # grab worksheet
        sheets = ['Summary Rolling MoM', 'VOC Rolling MoM']
        worksheet_selector = st.selectbox('Select a sheet', sheets)
        ws = wb[worksheet_selector]

        if worksheet_selector == 'Summary Rolling MoM':
            st.subheader('Summary')

            # get row data and return dictionary
            row_data = get_summary(ws, month_year_format)

            # log data
            log_data(row_data)

            # show data
            show_data(row_data)


        if worksheet_selector == 'VOC Rolling MoM':
            st.subheader('VOC')

    else:
        st.subheader('NO MATCHING FILES')

else:

    #####################################################
    #LOG FILE

    st.write('(Logfile...)')




