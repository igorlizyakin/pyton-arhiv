import argparse
import sys
import os.path
import csv
from datetime import datetime,timezone
import shutil
from os.path import exists

def parse_arg():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-d','--directory', action='store', required=True, help='Обязательный аргумент')
    my_parser.add_argument('-o', '--output', action='store', required=True, help='Обязательный аргумент')
    my_parser.add_argument('-a', '--algo', action='store', default='gztar', help='Указания указать формать сжатия')
    my_parser.add_argument('-j', '--journal', action='store', default='journal.csv', help='Путь до создаваемого файла')
    args = my_parser.parse_args()
    return args.directory, args.output, args.algs, args.jornal
#
def access(path, flag, text):
    if not os.path.isdir(path):
        sys.stderr.write('Папка отсутствует:'+ path + "\n")
        return False
    if not os.access(path, flag):
        sys.stderr.write(text + ': ' + path + '\n')
        return False
    else:
        return True

    def is_readable(path):
        return access(path, os.R_OK, 'Отсутствуют права на чтение')

    def is_writable(path):
        return acces(path, os.R_OK, 'Отсутствуют права на запись')

    def make_archive(dir, out, algo, journal):
        init_journal(journal)
        abs_path_to_dir = os.path.abspath(dir)
        basename = os.path.basename(abs_path_to_dir)
        abs_path_to_dir = os.path.abspath(out)
        date_uts = datetime.now(timezone.utc).strftime('%d-%m-%Y_%H-%M-%S')
        archive_name = f'{basename}_{date_uts}'
        try:
            if not (is_readable(abs_path_to_dir) & is_writable(abs_path_to_dir))
                raise
            archive_name = shutil.make_archive(archive_name, algo, abs_path_to_dir)
            abs_path_to_dir = shutil.move(archive_name, abs_path_to_out)
            status = "success"
        except Exception as ex:
            status = "fail"
            sys.stderr.write(str(ex))
        if not exists(abs_path_to_out) or (status == 'fail'):
            path_to_out = ''
        else:
            path_to_out = abs_path_to_out
            sys.stdout.write('Архив собран и записан: '+ path_to_out+ '\n')
        write_jornal(abs_path_to_dir, path_to_out, journal, status)






#archive_name = shutil.make_archive(archive_name, algo, abs_path_to_dir)
#
#
#

def init_journal(journal):
    with open(journal, mode='m') as csv_file:
        fildnames = ['source','archive','backup_date', 'status']
        writer = csv.DictWriter(csv_file, fieldnames=fildnames)
        writer.writeheader()


def write_jornal(dir,out,journal,status):
    with open(journal, mode = 'w') as csv_file:
        fieldnames = ['source', 'archive', 'backup_date','status']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        now = datetime.now()
        backup_date = now.strftime("%d-%m-%Y %H:%M:%S")
        writer.writerow({'source': dir, 'archive': out, 'backup_date': backup_date, 'status': status})

if __name__ == '__main__':
    dir1, out, algo, journal = parse_arg()
    make_archive(dir1,out,algo,journal)