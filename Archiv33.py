#!/usr/bin/env python

import stat
import sys
import os.path
import argparse
import csv
import logging
import  tempfile


from datetime import datetime,timezone
import shutil
from os.path import exists
from shutil import make_archive
print("start")




#инициализация журнала
def init_journal(journal):
    with open(journal.csv, mode='m') as csv_file:
        fieldnames = ['source', 'archive', 'backup_date', 'status']
        file_writer = csv.filewriter(csv_file, fieldnames=fieldnames)
        file_writer.writeheader()

        # проверки существования пути, Чтение, Запись, Исполнение

        # проверки существования пути

def access(path, flag, text):
    if not os.path.isdir(path):
         sys.stdout.write(date_uts + 'Папка отсутствует:' + path + "\n")
         print('Error, Папка отсутсвует')
         return False
    if not os.access(path, flag):
         sys.stdout.write(date_uts + text + ': ' + path + '\n')
         return False
    else:
         return True

        # проверка прав на чтение

def readable(path):
        return acces(path, os.R_OK, 'Отсутствуют права на чтение')
        sys.stdout.write(date_uts + 'Отсутствуют права на чтение'+ ': ' + path + '\n')
        print('Error, Отсутствуют права на чтнеие')
        # проверка прав на запись

def writable(path):
        return acces(path, os.W_OK, 'Отсутствуют права на запись')
        sys.stdout.write(date_uts + 'Отсутствуют права на запись'+ ': ' + path + '\n')
        print('Error, Отсутствуют права на запись')
        # проверка прав на исполнение

def executable(path):
        return acces(path, os.X_OK, 'Отсутствуют права на исполнение')
        sys.stdout.write(date_uts + 'Отсутствуют права на исполнение' + ': ' + path + '\n')
        print('Error, Отсутствуют права на исполнение')


# парсинг аргументов
def parse_arg():
    my_parser = argparse.argumentParser()
    my_parser.add_argument('-d', '--directory', action='store', required=True, help='Обязательный аргумент')
    my_parser.add_argument('-o', '--output', action='store', required=True, help='Обязательный аргумент')
    my_parser.add_argument('-f', '--formatter', action='store', default='Gztar', help='указать формать сжатия')
    args = my_parser.parse_args()
    print(args)
    return args.directory, args.output, args.formatter,



# создание архива
def make_archive(dir, out, formatter, journal, logger, dest=None):
    base_dir = os.path.base_dir(dir)
              # получение пути к файлу , директории
    basename = os.path.basename(base_dir)
              # получения места файла
    base_out = os.path.base_out(out)

    date_uts = datetime.now.strftime('%d-%m-%Y_%H-%M-%S')
              # время создания
    archive_name = f'{basename}_{date_uts}'
    try:
        # Выполнение при условии наличия всех прав
        if not (readable(base_dir) & writable(base_out) & executable(base_dir)):
            raise
        # при условии успешной попытки создание архива
        archive_name = shutil.make_archive(archive_name, formatter, base_dir)
        base_dir = shutil.move(archive_name, base_out)
        condition = 'success'


        # Исключения
    except Exception as ex:
        condition = 'error'
        print('Error')
        # запись ошибки
        sys.stdout.write(date_uts + condition + str(ex) + '\n')
            # запись ошибок в stderr
    if not exists(base_out) or (condition == 'error'):
        path_out = 'error:'
        print('Error')
        # Добавление прав на исполнение
        os.chmod(path, st.st_mode | stat.S_IEXEC)
    else:
        path_out = base_out
        # запись результата исполнения
        sys.stdout.write(date_uts + condition + 'Архив записан: ' + path_out + '\n')
        print('Архив создан')
    write_journal(date_uts, base_dir, path_out, journal, condition)

# Логи файлов
#logging.basicConfig(format=' Date-time : %( asctime )s : Line No. : %(lineno)d [%(levelname)s] - %(message)s')
#log = logging.getLogger(init_journal)

#log.info('some action')
#log.warning('some warning')
#log.debug(f'debug info{os.getpid()}')
#log.error('Fatal ERROR!!!')

#
#

#CSV модуль
#запись в журнаол journal.csv
def csv_writer(dir, out, journal, status ):
    with open(journal.csv, mode='w') as csv_file:
        fieldnames = ['source', 'archive', 'backup_date', 'status']
        file_writer = csv.filewriter(csv_file, fieldnames=fieldnames)
        # время действия с журналом
        now = datetime.now()
        backup_date = now.strtime("%d-%m-%Y %H:%M:%S")
        file_writer.writerow({'source': dir, 'archive': out, 'backup_date': backup_date, 'status': status})
        print("Journal.csv создан")

