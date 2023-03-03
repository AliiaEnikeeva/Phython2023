'''
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
'''
#  Фамилия, имя, отчество, номер телефона

def ask_user():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = int(input('Введите номер телефона: '))
    return last_name, first_name, phone_number # в таком виде возвращается кортеж


def save_to_file(data: tuple, file, mode='a'):
    data_str = ' '.join(map(str, data)) # через map все объекты в data приводим к строковому типу str
    print(data_str)
    # кодировка для windows 'cp-1251'
    with open(file, mode, encoding='utf-8') as fd: # 'а' метод дополнения новой информации
        fd.write(f'{data_str}\n')
 
def read_file(file):
    with open(file, 'r', encoding='utf-8') as fd: # 'а' метод дополнения новой информации
        lines = fd.readlines()
        print(lines)
        # ['test string\n', 'test string\n', 'Иванов Иван 555\n', 'Петров Петр 777\n']
        for line in lines:
            line.replace('\n', '') # функция замена чего-то (\n) на что-то ()
            line.strip()


if __name__ == '__main__':
    file_contacts = 'file.txt'
    #data = ask_user()
    # print(data)
    # save_to_file(data)
    read_file(file_contacts)