import os
import sys
import psutil

do = ' '

while do != 0:
    do = input('''
    Введите номер нужной функции:
    [1] - Содержание текущей директории
    [2] - Номера выполняемых в системе процессов
    [3] - Количество ядер процессора
    [4] - Текущая директория
    [5] - Кодировка файловой системы
    [6] - Имя пользователя
    
    ''')
    if do == ('1'):
        print(os.listdir())   # Список файлов в текущей директории
    elif do == ('2'):
        print(psutil.pids())  # Список номеров запущенных в системе процессов PID
    elif do == ('3'):
        print(psutil.cpu_count()) # Кол-во ядер проца
    elif do == ('4'):
        print(os.getcwd()) # Текущая директория
    elif do == ('5'):
        print(sys.getfilesystemencoding()) # Кодировка файловой системы
    elif do == ('6'):
        print(os.getlogin()) # Имя текущего пользователя системы
    else:
        print('Некорректное значение!')
if do == 0:
    print('Пока!')


