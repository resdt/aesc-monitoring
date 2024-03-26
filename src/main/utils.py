import os
import shutil as sht
import pandas as pd

import src.main.PATH as path


TMP_FOLD = path.TMP_FOLD


def df_date_sort(df, column, date_format):
    df[column] = pd.to_datetime(df[column], format=date_format)
    df.sort_values(column, inplace=True)
    df[column] = df[column].dt.strftime(date_format)


def clean_dir(dir_to_clean=TMP_FOLD):
    if os.path.isdir(dir_to_clean):
        sht.rmtree(dir_to_clean)
