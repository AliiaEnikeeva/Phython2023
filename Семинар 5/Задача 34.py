'''
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.
Стихотворение Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

Пример:

Ввод:
пара-ра-рам рам-пам-папам па-ра-па-дам
Вывод:
Парам пам-пам
'''
def find_rhythm(text: str):
    phrases = text.split()   # разбили текст на фразы
    phrases_vow = []   # пустой список для фраз, очищенных от согласных
    for i in phrases:   # каждую фразу фильтруем от согласных
        phrases_vow.append(list(filter(lambda x: x in 'аеиоуэюя', list(i))))
    result_list = map(lambda x: len(x) == len(phrases_vow[0]), phrases_vow)
    return all(result_list)


song = 'пара-ра-рам рам-пам-папам па-ра-па-дам пиу пи пипипипип'
if find_rhythm(song):
    print('Парам пам-пам')
else:
    print('Пам парам')