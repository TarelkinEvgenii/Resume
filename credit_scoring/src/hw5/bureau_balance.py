import os
import sys

import numpy as np
import pandas as pd

sys.path.append(r'C:\Users\user\Desktop\SHIFT\credit_scoring')

from src.app.utils.find_importance import find_importance


def main(path_to_file: str, path_to_save: str) -> None:
    """Функция для нахождения важных строк в файле фич bureau_balance."""
    np.seterr(divide='ignore', invalid='ignore')
    alpha = 0.05

    train = pd.read_csv(os.path.join(path_to_file, 'application_train.csv'))
    train = train[['SK_ID_CURR', 'TARGET']]
    bureau = pd.read_csv(os.path.join(path_to_file, 'bureau.csv'))
    bureau = pd.merge(bureau, train, how='inner', on='SK_ID_CURR')
    bureau = bureau[['SK_ID_CURR', 'TARGET', 'SK_ID_BUREAU']]

    bureau_balance = pd.read_csv(os.path.join(path_to_file, 'bureau_balance.csv'))
    bureau_balance = pd.merge(bureau_balance, bureau, how='inner', on='SK_ID_BUREAU')
    bureau_balance.reset_index(inplace=True, drop=True)
    bureau_balance_copy = bureau_balance.copy(deep=True)

    columns_for_tests = list(bureau_balance_copy.columns)
    columns_for_tests.remove('SK_ID_CURR')
    columns_for_tests.remove('TARGET')
    columns_for_tests.remove('SK_ID_BUREAU')
    important_columns = find_importance(
        bureau_balance_copy,
        columns_for_tests,
        alpha=alpha,
        tagret_name='TARGET',
    )
    important_columns.insert(0, 'TARGET')
    important_columns.insert(0, 'SK_ID_CURR')
    important_columns.insert(0, 'SK_ID_BUREAU')
    bureau_balance = bureau_balance[important_columns]
    bureau_balance.to_csv(
        os.path.join(path_to_save, 'important_bureau_balance_train.csv'),
        index=False,
    )


if __name__ == '__main__':
    path_to_file = r'C:\\Users\\user\\Desktop\\SHIFT\\credit_scoring\\data\\'
    path_to_save = r'C:\\Users\\user\\Desktop\\SHIFT\\credit_scoring\\data\\'
    main(path_to_file, path_to_save)