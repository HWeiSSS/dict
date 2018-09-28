import pymysql
import re

db = pymysql.connect(host='localhost',
                    user='root',password='123456',
                    database='dict',charset='utf8')

cursor = db.cursor()

f = open('dict.txt')
for i in f:
    l = re.findall(r'\S+',i) 
    word = l[0]
    interpret = ' '.join(l[1:])
    sql_insert = 'insert into word values(%s,%s);'

    try:
        cursor.execute(sql_insert,[word,interpret])
        db.commit()
    except:
        db.rollback()

f.close()
