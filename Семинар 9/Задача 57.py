'''
1. Прочесть с помощью pandas файл
california_housing_test.csv, который находится в папке
sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы '''

import pandas as pd

df = pd.read_csv('california_housing_train.csv')
print(df.head())
print(df.shape)
print(df.dtypes)

# https://jupyter.org/  установить юпитер на комп

