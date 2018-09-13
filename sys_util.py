import os
import sys
import psutil

while True:
    command = input('''
    Введите номер нужной функции:
    [1] - Содержание текущей директории
    [2] - Номера выполняемых в системе процессов
    [3] - Количество ядер процессора
    [4] - Текущая директория
    [5] - Кодировка файловой системы
    [6] - Имя пользователя
    
    Для выхода [0]
    
    ''')
    if command == ('1'):
        print(os.listdir())   # Список файлов в текущей директории
    elif command == ('2'):
        print(psutil.pids())  # Список номеров запущенных в системе процессов PID
    elif command == ('3'):
        print(psutil.cpu_count()) # Кол-во ядер проца
    elif command == ('4'):
        print(os.getcwd()) # Текущая директория
    elif command == ('5'):
        print(sys.getfilesystemencoding()) # Кодировка файловой системы
    elif command == ('6'):
        print(os.getlogin()) # Имя текущего пользователя системы
    elif command == ('0'):
        break
    else:
        print('Некорректное значение!')
print('Пока!')
    



