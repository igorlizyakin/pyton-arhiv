#!/usr/bin/env python
import glob
import os
import datetime
import shutil
#Настройки:
#Путь к основному каталогу откуда надо копировать
pathtodata="w:/Base_1c"
#Название каталогов, которые надо копировать с их содержимым:
organiz = ["Folder_01",
           "Folder_02",
           "Folder_03",
           "Folder_04",
           "Folder_05",
           "Folder_06"
           ]
# делаем каталог для копий по текущему времени
# по умолчанию должен быть создан каталог e:/_backups/
dt = datetime.datetime.now()
currentdate = dt.strftime('%Y_%m_%d-%H%M')
os.mkdir('e:/_backups/'+currentdate)

for org in organiz:
    print(org+" копирование...")
    # скопируем все каталоги в созданный
    # копирование дерева  - откуда - куда
    shutil.copytree(''+pathtodata+'/'+org+'', 'e:/_backups/'+currentdate+'/'+org+'/')

# заархивируем все что скопировано
names = glob.glob('e:/_backups/'+currentdate+'/*')
for name in names:
    if os.path.isdir(name):
        # заархивировать все name используем winrar 4.01
        print (name+" архивирование каталога...")
        # ключ -df удаляет скопированные каталоги после архивирования
        os.system(r'c:/"Program Files"/"winrar"/rar.exe a -r -ep1 -df '+name+' '+name+' ')

# все сделал
print("все сделано")