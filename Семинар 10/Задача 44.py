'''В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
'''
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())

one_hot_data = pd.DataFrame({'robot': [1 if i == 'robot' else 0 for i in lst], 'human': [1 if j == 'human' else 0 for j in lst]})
print(one_hot_data)

pd.get_dummies(data['whoAmI'])