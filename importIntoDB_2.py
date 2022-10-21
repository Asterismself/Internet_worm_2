# _*_ coding : UTF-8 _*_
# @Time : 2022/10/17 20:10
# @Author : GYH
# @File : ImportIntoDB
# @Project :
import pymysql
import json


DBUSER = 'root'
DBPASS = 'gyh17856973504'
DBHOST = 'localhost'
DBNAME = 'bilibili_Interests'
DBPORT = 3306
DBCHARSET = 'utf8'

uid = int(input('请输入up主的id：'))
flag = int(input('是否需要求关注列表交集(1表示需要，2表示不需要):'))
if uid == 11632773:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\bilibili_Interests\\11632773\\data_list.json', 'r', encoding='utf-8') as fp:
        data = fp.read()
        data = json.loads(data)
        # print(len(data))
elif uid == 375040863:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\bilibili_Interests\\375040863\\data_list.json', 'r', encoding='utf-8') as fp:
        data = fp.read()
        data = json.loads(data)
try:
    DB = pymysql.connect(user=DBUSER, password=DBPASS, host=DBHOST, database=DBNAME, port=DBPORT, charset=DBCHARSET)
    # print('数据库连接成功！')
    cur = DB.cursor()
    # 创建表格
    if uid == 11632773:
        cur.execute('DROP TABLE IF EXISTS 11632773_list')
        sql = 'CREATE TABLE 11632773_list(UID INT, UNAME char(20), LV INT, FANS_NUM INT)'
    elif uid == 375040863:
        cur.execute('DROP TABLE IF EXISTS 375040863_list')
        sql = 'CREATE TABLE 375040863_list(UID INT, UNAME char(20), LV INT, FANS_NUM INT)'
    cur.execute(sql)
    print('表格创建成功！')
    # 插入数据
    for i in range(0, len(data)):
        if uid == 11632773:
            sql = 'INSERT INTO 11632773_list(UID, UNAME, LV, FANS_NUM) VALUES(%s, %s, %s, %s)'
        elif uid == 375040863:
            sql = 'INSERT INTO 375040863_list(UID, UNAME, LV, FANS_NUM) VALUES(%s, %s, %s, %s)'
        values = (data[i]['UID'], data[i]['UNAME'], data[i]['level'], data[i]['FANS_NUM'])
        cur.execute(sql, values)
        DB.commit()
        print('数据插入成功！')
    if flag == 1:
        cur.execute('DROP TABLE IF EXISTS Intersection')
        sql = 'CREATE TABLE Intersection(UID INT, UNAME char(20), LV INT, FANS_NUM INT)'
        cur.execute(sql)
        print('交集表创建成功！')
        sql = 'INSERT INTO Intersection SELECT DISTINCT 11632773_list.UID, 11632773_list.UNAME, 11632773_list.LV, 11632773_list.FANS_NUM FROM 11632773_list JOIN 375040863_list ON 11632773_list.UID = 375040863_list.UID'
        cur.execute(sql)
        DB.commit()
        print('交集数据插入成功！')
except pymysql.Error as error:
    print('失败：' + str(error))
    DB.rollback()

