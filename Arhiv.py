#!/usr/bin/env python
import shutil
import os
import time
import tempfile
import pprint
shutil.copytree('./Arhive.py')
pprint.pprint(os.listdir(./Arhive.py))
root_directory='newdir'
shutil.make_archive("newdirabcd","gztar",root_directory)

tempdir = tempfile.gettempdir() #папка для временного файла
dir_with_my_file = os.path.join(tempdir, 'filedir')
os.mkdir(dir_with_my_file, exist_ok=True) #файл случайного контента
with open(os.path.join(dir_with_my_file,"fake_text.txt"),"wb") as my_file: my_file.write(os.urandom(int(1024*1024*1.5))) #файл со случайном контентом на 1.5 м
def make_archive(source, dest=Note):
    base = os.path.basename(source)
    destination = f"{base}.zip" if not dest else dest
    name = base.split('.')[0]
    format_ = "zip"
    archive_from = os.path.dirname(source)
    archive_to = os.path.basename(source.strip(os.sep))
    shutil.make_archive(name,format_,archive_from,archive_to)
    shutil.move(f"{name}.{format_}",destination)
    make_archive(dir_with_my_file, "./archive.zip")

    import csv
    with open('бэкапы.csv', mode='w') as csv_file:
        fieldnames = ['file_name','backup_date','file_size']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'file_name': 'game_data.dump','backup_date':'2021-10-28','file_size':'1024'})
        writer.writerow({'file_name': 'game_data.dump', 'backup_date': '2021-10-29', 'file_size': '1027'})

import logging, os
logging.basicConfig(format=' Date-Time : %(asctime)s : Line No. : %(lineno)d [%(livelname)s]- %(message)s', leve)
log = logging.getLogger(_name_)

log.info("some action")
log.warning("some warning")
log.debug(f"debug info {os.getpid()}")
log.error("FATAL ARROR!!!")
#what_to_reserve = ['/home/jake/Study','/home/jack/photo']
#where_to_save = '/home/jake/Backups'
#today = where_to_save+os.sep+time.strftime('%Y%m%d')
#now = time.strftime('%H%M%S')
#comment = input('Введите комментарий')
#if len(comment) == 0:
 #   target = today+os.sep+now+'.zip'
#else:
 #   target = today+os.sep+now+'_'+comment.replace('','')+'.zip'
  #  if not os.path.exists(today)
   #     os.mkdir(today)
    #    print('Каталог успешно создан',today)
     #   zip_command = "zip-gr{0}{1}".format(target,''.join(what_to_reserve))
      #  if os.system(zip_command)==0:
       #     print("Резервная копия успешно создана в",target)
        #else:
         #   print("Ошибка!")
