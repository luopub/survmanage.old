# usage: if [ -z `python3 /survauthserver/docker/check_mysql_ready.py` ]; then echo error; else echo ok; fi
import os
import MySQLdb
host = os.environ.get('MYSQL_HOST') or 'mysqlauth'
port = (os.environ.get('MYSQL_PORT') and int(os.environ.get('MYSQL_PORT'))) or 3306
username = os.environ.get('MYSQL_USERNAME') or 'root'
password = os.environ.get('MYSQL_PASSWORD') or '12345678'
try:
    conn = MySQLdb.connect(host=host, port=port, user=username, password=password, database="mysql")
    cursor = conn.cursor()
    cursor.execute('select * from user;')
    print(len(cursor.fetchall()))
    conn.close()
except: 
    pass
