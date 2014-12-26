#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import time
import tarfile
import zipfile

'''
mysqldump
Usage: mysqldump [OPTIONS] database [tables]
OR     mysqldump [OPTIONS] --databases [OPTIONS] DB1 [DB2 DB3...]
OR     mysqldump [OPTIONS] --all-databases [OPTIONS]
For more options, use mysqldump --help
'''
db_host="localhost"
db_user="root"
db_passwd="root"
db_name="bibi"
db_charset="utf8"
db_backup_name=r"/home/crm_%s.sql" %(time.strftime("%Y%m%d%H%M"))

zip_src = db_backup_name
zip_dest = zip_src + ".zip"

def zip_files():
    f = zipfile.ZipFile(zip_dest, 'w' ,zipfile.ZIP_DEFLATED) 
    f.write(zip_src)
    f.close() 
    
if __name__ == "__main__":
    print("begin to dump mysql database crm...");
    os.system("mysqldump -h%s -u%s -p%s %s --default_character-set=%s > %s" %(db_host, db_user, db_passwd, db_name, db_charset, db_backup_name))
    print("begin zip files...")
    zip_files()
    print("done, pyhon is great!")
