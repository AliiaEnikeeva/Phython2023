'''1. Изобразите отношение households к population с
помощью точечного графика
2. Визуализировать longitude по отношения к
median_house_value, используя линейный график
3. Представить гистограмму по housing_median_age
4. Изобразить гистограмму по median_house_value с
оттенком housing_median_age'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file = 'california_housing_train.csv'

df = pd.read_csv(file)

#1. Изобразите отношение households к population спомощью точечного графика
# sns.scatterplot(data = df, x='households', y='population')
# plt.show() # отоброзить график

# 2. Визуализировать longitude по отношения к
# median_house_value, используя линейный график

# sns.relplot(data=df, x="longitude", y="median_house_value", kind="line")
# plt.show() # отоброзить график

#3. Представить гистограмму по housing_median_age
# sns.histplot(data=df, x="housing_median_age")
# plt.show() # отоброзить график

#4. Изобразить гистограмму по median_house_value с
#оттенком housing_median_age
sns.histplot(data=df, x="median_house_value", hue="housing_median_age", legend=False)
plt.show() # отоброзить график