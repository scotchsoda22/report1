import pandas as pd
import numpy as np


def stunden_base():
    print("Please provide a path to the Stunden_base file")
    file_path1 = input()[1:-1]
    Stunden_Base = pd.read_csv(file_path1, sep=';', engine='python')
    Stunden_Base = Stunden_Base[['DATEWORKED',
             'Z_MATERIAL',
             'ACTUAL',
             'AFK',
             'EMPLASTNAME',
             'DAILY_COMMENT',
             'EMP_SER_NUM',
             'SERVICE_MONTH']]
    Stunden_Base['DATEWORKED'] = Stunden_Base['DATEWORKED'].str.replace('.','/', regex=True)

    dummy_num = Stunden_Base[['EMP_SER_NUM']].drop_duplicates()
    dummy_num['dummy_num'] = np.arange(start=1, stop=len(dummy_num)+1, step=1)

    Stunden_Base = pd.merge(Stunden_Base, dummy_num,
                          on ='EMP_SER_NUM',
                          how ='left')
    return Stunden_Base

if __name__ == "__main__":
    print(stunden_base())