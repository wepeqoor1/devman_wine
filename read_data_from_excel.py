import collections

import pandas as pd


def get_assortment_wines(filepath) -> collections.defaultdict:
    """
    Из .xlsx файла считывает данные и преобразует в массив collections.defaultdict
    """

    excel_data_df: pd.DataFrame = pd.read_excel(
        filepath,
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
