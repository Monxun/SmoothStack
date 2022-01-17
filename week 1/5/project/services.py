from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from itertools import islice
import pandas as pd
import streamlit as st
import logging
import os

def check_file(file):
    while True:
        try:
            file = f'data/{file}'
            if os.path.exists(file):
                logging.info(f"{file} exists")
                break
        except FileNotFoundError:
            print("FileNotFound: not a valid file.")
        else:
            continue

def get_current_month():
    pass

def get_summary(ws, month_year_format):
    row = None
    for item in ws['A']:
        if month_year_format in str(item.value):
            row = item.row
            st.write(f'(Row: {row})')
    test = [ro for ro in ws.iter_rows(min_row=row, max_row=row, values_only=True)]
    new_test = [item for item in test[0][1:] if item != None]

    # create dictionary from row data
    row_data = {}
    row_data['30s_abandonment'] = f"Abandon after 30s: {round(new_test[1]*100,2)}%"
    row_data['fcr'] = f"FCR : {new_test[2]*100}0%"
    row_data['dsat'] = f"DSAT : {new_test[3]*100}0%"
    row_data['csat'] = f"CSAT : {new_test[4]*100}0%"

    return row_data
    

def log_data(row_data):
    print(row_data)
    for item in row_data:
        print(item, row_data[item])
        # logging.info(item.value)


def show_data(row_data):
    for item in row_data:
        st.write(row_data[item])