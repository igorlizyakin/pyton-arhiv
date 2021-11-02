import argparse
import sys
import os.path
import csv
from datetime import datetime,timezone
import shutil
from os.path import exists

def parse_arg():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-d','--directory')


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

    def is_radable(path):
        return access(path, os.R_OK, 'Отсутствуют права на чтение')

    raise
archive_name = shutil.make_archive(archive_name, algo, abs_path_to_dir)
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
    