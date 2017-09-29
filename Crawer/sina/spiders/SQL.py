import pymysql

# 初始化数据库信息
db = pymysql.connect(host='118.89.159.211',
                     user='hive',
                     password='hive',
                     port=3306,
                     database='spiderman',
                     charset='utf8')

# 初始化光标
cursor = db.cursor()


class Sql:

    @classmethod
    def inserdata(cls, data):
        table = 'test'
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        # 构造SQL语句其实是插入语句
        # ON DUPLICATE KEY UPDATE，如果主键已经存在，那就执行更新
        sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys,
                                                                                              values=values)  # UPDATE 后面要加空格
        update = ','.join(["{key} = %s".format(key=key)
                           for key in data])  # join结果id = %s, name = %s, time = %s
        sql += update

        try:
            if cursor.execute(sql, tuple(data.values()) * 2):
                print('Successful')
                db.commit()
        except:
            print("Failed")
            db.rollback()
