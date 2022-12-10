import collections
import os

import pandas as pd

from exceptions import ToManyXlsxFilesException


def get_assortment_wines() -> collections.defaultdict:
    """
    Из .xlsx файла считывает данные и преобразует в массив collections.defaultdict
    """
    files = os.listdir()
    xlsx_files = []
    for file in files:
        if '.xlsx' in file:
            xlsx_files.append(file)
    if len(xlsx_files) != 1:
        raise ToManyXlsxFilesException

    xlsx_file = xlsx_files[0]
    excel_data_df: pd.DataFrame = pd.read_excel(
        xlsx_file,
        sheet_name='Лист1',
        na_values=None,
        keep_default_na=False,
    )

    uniq_categories: list = excel_data_df['Категория'].unique()

    wine_categories = collections.defaultdict(
        list,
        {
            category: excel_data_df[excel_data_df['Категория'].isin([category])].to_dict(
                orient='records'
            )
            for category in uniq_categories
        },
    )
    return wine_categories
