import pymysql

def connmysql():
    db = pymysql.connect(host='118.89.159.211',
                              user='hive',
                              password='hive',
                              port=3306,
                              db='spiderman',
                              charset='utf8')
    cursor = db.cursor()
    cursor.execute('SELECT VERSION()')
    print('MySQL VERSION():', cursor.fetchone()[0])
    return db

def createtable(db):
    cursor = db.cursor()
    # sql = 'CREATE TABLE IF NOT EXISTS Sinanews(' \
    #       'title VARCHAR(255) NOT NULL , Contents TEXT NOT NULL , Editor VARCHAR (255)  NOT NULL,' \
    #       'Source VARCHAR (255)  NOT NULL, time DATETIME  NOT NULL, Comment INT  NOT NULL, PRIMARY KEY(title))'

    sql = 'CREATE TABLE IF NOT EXISTS Sinanew(' \
          'title VARCHAR(255), Contents TEXT, Editor VARCHAR(255),' \
          'Source VARCHAR(255), time VARCHAR(255), Comment INT, PRIMARY KEY(title))'

    try:
        if cursor.execute(sql):
            print('Successful')
    except:
        print('Field')


def inserdata(data, db, table):
    # print(data)
    cursor = db.cursor()
    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'\
        .format(table=table, keys=keys, values=values)
    try:
        if cursor.execute(sql, tuple(data.values())):
            db.commit()
            return 1
    except:
        db.rollback()
        return 0

def delectall(db, table):
    cursor = db.cursor()
    sql = 'DELETE FROM {table}'.format(table=table)
    try:
        cursor.execute(sql)
        db.commit()
        print('Delect Sucessful')
    except:
        print('Delect Faield')
        db.rollback()

if __name__ == '__main__':
    # 测试
    data = {
        'id': '20120019',
        'name': 'a辣',
        'age': 21
    }
    db = connmysql()
    # 插入
    # inserdata(data, db, 'students')
    # 创建
    # createtable()
    # 删除
    # delectall(db, 'Sinanew')
    db.close()

