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
# Everytime running this program need to change "table_name" and "path"
# 表名,如果不存在表，则自动创建
table_name = 'English'
# 文件路径
path = r'/Users/sarahyang/Desktop/5500Words.csv'

data = pd.read_csv(path, encoding='utf-8')
engine = create_engine("mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}".format(**mysql_setting), max_overflow=5)
data.to_sql(table_name, engine, index=False, if_exists='replace', )
print('导入成功...')
# 关闭连接
engine.dispose()
