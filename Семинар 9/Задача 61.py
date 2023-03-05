'''
1. Определить какое максимальное и минимальное
значение median_house_value
2. Показать максимальное median_house_value, где
median_income = 3.1250
3. Узнать какая максимальная population в зоне
минимального значения median_house_value'''


import pandas as pd
df = pd.read_csv('california_housing_train.csv')
# print(df['median_house_value'].max())
# print(df['median_house_value'].min())
# print(df[df['median_income'] == 3.1250]['median_house_value'].max())
print(df[df['median_house_value'] < df['median_house_value'].quantile(.25)]['population'].max())
