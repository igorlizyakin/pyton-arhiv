#!/usr/bin/env python

import stat
import sys
import os.path
import argparse
import csv
import logging
import shutil
import  tempfile


from datetime import datetime,timezone
import shutil
from os.path import exists

if __name__ == '__main__':
    #dir1, out, formatter, journal = parse_arg()
    #make_archive(dir1, out, formatter, journal)

#инициализация журнала
def init_journal(journal):
    with open(journal.csv, mode='m') as csv_file:
        fieldnames = ['source', 'archive', 'backup_date', 'status']
        file_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        file_writer.writeheader()

# парсинг аргументов
def parse_arg():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-d', '--directory', action='store', required=True, help='Обязательный аргумент')
    my_parser.add_argument('-o', '--output', action='store', required=True, help='Обязательный аргумент')
    my_parser.add_argument('-f', '--formatter', action='store', default='Gztar', help='указать формать сжатия')
    my_parser.add_argument('-j', '--journal', action='store', default='journal.csv', help='Путь до создаваемого файла')
    args = my_parser.parse_args()
    print(args)
    return args.directory, args.output, args.formatter, args.jornal



#проверка существования пути
def access(path, flag, text):
    if not os.path.isdir(path):
        sys.stderr.write('Папка отсутствует:'+ path + "\n")
        return False
    if not os.access(path, flag):
        sys.stderr.write(text + ': ' + path + '\n')
        return False
    else:
        return True
# проверка прав на чтение
def readable(path):
    return acces(path, os.R_OK, 'Отсутствуют права на чтение')
# проверка прав на запись
def writable(path):
    return acces(path, os.W_OK, 'Отсутствуют права на запись')
# проверка прав на исполнение
def executable(path):
    return acces(path, os.X_OK, 'Отсутствуют права на исполнение')



# создание архива
def make_archive(dir, out, formatter, journal, logger, dest=None):
    init_journal(journal)
    abs_path_to_dir = os.path.abspath(dir)
              # получение пути к файлу , директории
    basename = os.path.basename(abs_path_to_dir)
              # получения места файла
    abs_path_to_out = os.path.abspath(out)
    date_uts = datetime.now(timezone.utc).strftime('%d-%m-%Y_%H-%M-%S')
              # время создания
    archive_name = f'{basename}_{date_uts}'
    try:
        if not (readable(abs_path_to_dir) & writable(abs_path_to_out) & executable(abs_path_to_dir)):
                raise
        archive_name = shutil.make_archive(archive_name, formatter, abs_path_to_dir)
        abs_path_to_dir = shutil.move(archive_name, abs_path_to_out)
        os.chmod(path, st.st_mode | stat.S_IEXEC)
            # делаем исполнение
            status = "success"
        except Exception as ex:
            status = "fail"
            sys.stderr.write(str(ex))
            #запись ошибок в stderr
        if not exists(abs_path_to_out) or (status == 'fail'):
            path_to_out = ''
        else:
            path_to_out = abs_path_to_out
            sys.stdout.write('Архив записан: ' + path_to_out + '\n')
        write_journal(abs_path_to_dir, path_to_out, journal, status)

# Логи файлов
logging.basicConfig(format=' Date-time : %(asctime)s : Line No. : %(lineno)d [%(levelname)s] - %(message)s'), leve
log = logging.getLogger(__make_archive__)

log.info('some action')
log.warning('some warning')
log.debug(f'debug info{os.getpid()}')
log.error('Fatal ERROR!!!')




#
#

#CSV модуль
#запись в журнаол journal.csv
def csv_writer(dir,out,journal,status, ):
    with open(journal.csv, mode='w') as csv_file:
        fieldnames = ['source', 'archive', 'backup_date', 'status']
        file_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        now = datetime.now()
        backup_date = now.strftime("%d-%m-%Y %H:%M:%S")
        file_writer.writerow({'source': dir, 'archive': out, 'backup_date': backup_date, 'status': status})

