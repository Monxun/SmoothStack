from openpyxl import load_workbook
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