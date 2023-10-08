# # 导入pymysql方法
# import pymysql
#
# # 连接数据库
# config = {'host': 'localhost',
#           'port': 3306,
#           'user': 'root',
#           'passwd': 'root',
#           'charset': 'utf8mb4',
#           'local_infile': 1
#           }
# conn = pymysql.connect(**config)
# cur = conn.cursor()
#
#
# # load_csv函数，参数分别为csv文件路径，表名称，数据库名称
# def load_csv(csv_file_path, csv_filename, table_name, database='evdata'):
#     # 打开csv文件
#     file = open(csv_file_path, 'r', encoding='utf-8')
#     # 读取csv文件第一行字段名，创建表
#     reader = file.readline()
#     b = reader.split(',')
#     colum = ''
#     for a in b:
#         colum = colum + a + ' varchar(255),'
#     colum = colum[:-1]
#     # 编写sql，create_sql负责创建表，data_sql负责导入数据
#     create_sql = 'create table if not exists ' + table_name + ' ' + '(' + colum + ')' + ' DEFAULT CHARSET=utf8'
#     data_sql = "LOAD DATA LOCAL INFILE '%s' INTO TABLE %s FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\r\\n' IGNORE 1 LINES" % (
#         csv_filename, table_name)
#
#     # 使用数据库
#     cur.execute('use %s' % database)
#     # 设置编码格式
#     cur.execute('SET NAMES utf8;')
#     cur.execute('SET character_set_connection=utf8;')
#     # 执行create_sql，创建表
#     cur.execute(create_sql)
#     # 执行data_sql，导入数据
#     cur.execute(data_sql)
#     conn.commit()
#     # 关闭连接
#     conn.close()
#     cur.close()
#
#
# if __name__ == '__main__':
#     load_csv("/Users/sarahyang/Desktop/English.csv", "English.csv", "English", "test")
# -*- coding:UTF-8 -*-

import pymysql
import pandas as pd
from sqlalchemy import create_engine

# 数据库信息
mysql_setting = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    # 数据库名称
    'db': 'test',
    'charset': 'utf8'
}
# 表名
# 如果不存在表，则自动创建
table_name = 'ieltsVocabulary'
# 文件路径
path = r'/Users/sarahyang/Desktop/list1_10new.csv'

data = pd.read_csv(path, encoding='utf-8')
# print(data)
engine = create_engine("mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}".format(**mysql_setting), max_overflow=5)
data.to_sql(table_name, engine, index=False, if_exists='replace', )
print('导入成功...')
# 关闭连接
engine.dispose()