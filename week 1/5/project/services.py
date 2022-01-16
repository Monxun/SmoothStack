from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from itertools import islice
import pandas as pd
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


