#coding=utf-8
import pymysql

#通过pymysql的connect()方法声明了一个MySQL连接对象
#需要传入MySQL运行的host的IP,此处由于MySQL在本地运行，所以传入的是localhost
#如果MySQL在远程运行，则传入其公网的IP地址
db = pymysql.connect(host='localhost',user='root',password='root',port=3306)
#连接成功之后，需要调用cursor()方法获得MySQL的操作游标，利用游标来执行SQL语句
cursor = db.cursor()

#执行SQL语句，获得当前MySQL的版本
cursor.execute('SELECT VERSION()')
#fetchone()方法获得第一条数据，也就是得到版本号
data = cursor.fetchone()
#print('Database version:',data)

#执行创建数据库的SQL语句，数据库名字是spiders ,默认编码是utf-8
#因为这条语句不是查询语句，所以直接执行后就成功创建了一个数据库spiders
#cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
db.close()
#连接数据库
def  dbconn():
    db = pymysql.connect(host='118.89.159.211',
                         user='hive',
                         password='hive',
                         port=3306,
                         db='crawer',
                         charset='utf8')

#创建表
def CreatTable():
    #获得MySQL的操作游标
    cursor = db.cursor()
    #sql = 'CREATE TABLE IF NOT EXISTS students(id VARCHAR(255) NOT NULL ,name VARCHAR(255) NOT NULL,age INT  NOT NULL,PRIMARY KEY (id))'

    sql = 'CREATE TABLE IF NOT EXISTS news_sina(title VARCHAR(255) NOT NULL ,newssource VARCHAR(255) ,time DATETIME ,article text,editor VARCHAR(255) ,comments INT ,PRIMARY KEY (title))'

    #利用游标来执行SQL语句
    cursor.execute(sql)
    db.close()

#向数据库中插入数据(普通的插入)
'''id = '20120001'
user = 'Bob'
age = 20
db = pymysql.connect(host='localhost',user='root',password='root',port=3306,db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id,name,age) values(%s,%s,%s )'
try:
    cursor.execute(sql,(id,user,age))
    db.commit()
except:
    db.rollback()
db.close()'''

#通用的插入方法（SQL语句会根据字典动态构造，元组也动态构造）
def insert(data):
    db = pymysql.connect(host='118.89.159.211',
                         user='hive',
                         password='hive',
                         port=3306,
                         db='spiders',
                         charset='utf8')
    cursor = db.cursor()
    table = 'news_sina'
    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table = table,keys=keys,values = values) #INSERT INTO students(id,name,age) VALUES (%s,%s,%s)
    try:
        if cursor.execute(sql, tuple(data.values())):
            db.commit()
            return 1
    except:
        db.rollback()
        return 0
    db.close()
#更新数据
'''db = pymysql.connect(host='localhost',user='root',password='root',port=3306,db='spiders')
#获得MySQL的操作游标
cursor = db.cursor()
sql = 'UPDATE students SET age = %s WHERE name = %s'
try:
    cursor.execute(sql,(25,'Bob'))
    db.commit()
except:
    db.rollback()
db.close()'''

#如果数据存在则更新，如果数据不存在则插入，支持灵活的字典传值
def update(data):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         port=3306,
                         db='spiders',
                         charset='utf8')
    #获得MySQL的操作游标
    cursor = db.cursor()
    table ='students'
    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys, values=values)#INSERT INTO students(id,name,age) VALUES (%s,%s,%s) ON DUPLICATE KEY UPDATE
    update = ','.join(["{key} = %s".format(key=key) for key in data])  # id = %s,name = %s,age = %s
    sql += update
    try:
        if cursor.execute(sql, tuple(data.values())*2):
            print('Successful')
            db.commit()
            return 1
    except:
        print('Failed')
        db.rollback()
        return 0
    db.close()

#删除数据
def delete():
    db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
    #获得MySQL的操作游标
    cursor = db.cursor()
    table = 'students'
    condition = 'age > 20'

    sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

#查询数据
'''db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
#获得MySQL的操作游标
cursor = db.cursor()
sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount) #获取查询结果的条数
    one = cursor.fetchone()        #fetchone()方法可以获取结果的第一条数据，返回结果是元组形式，元组的顺序跟字段一一对应
    print('One:',one)
    results = cursor.fetchall()   #fetchall()方法，可以得到结果的所有数据
    print('Results:',results)
    print('Results Type:',type(results))
    for row in results:
        print(row)
except:
    print('Error')'''


#推荐逐条取数据
def select():
    tag={}
    db = pymysql.connect(host='118.89.159.211',
                         user='hive',
                         password='hive',
                         port=3306,
                         db='crawer',
                         charset='utf8')

    #获得MySQL的操作游标
    cursor = db.cursor()
    table = 'Website_info'
    condition = '"新浪国内新闻"'
    sql = 'SELECT * FROM {table} WHERE Website_name = {condition}'.format(table=table, condition=condition)
    print(sql)
    try:
        cursor.execute(sql)
        print('Count:', cursor.rowcount)
        row = cursor.fetchone()

        #print('Row:', row)
        tag['title'] = row[8]
        tag['newssource'] = row[12]
        tag['time'] = row[10]
        tag['article'] = row[11]
        tag['editor'] = row[9]
        print(tag)
    #comments = row[]
        return tag
    except:
        print('Error')
    db.close()

if __name__ == '__main__':
    result = select()
    print(result['editor'])


