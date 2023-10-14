import os
from enum import Enum

mysql_setting = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    # 数据库名称
    'db': 'test',
    'charset': 'utf8'
}

soup_context = [["basic", "word-exp"], ["webPhrase", "mcols-layout"], ["blng_sents_part dict-module", "mcols-layout"]]
# soup_context = [["trans-list", "col2"]]
# 查询出所有需要的字段
sql_all_field = """
    select English, Chinese, score, id, frequency, table_name
    from AllEnglishKnowledge
    where id ={} 
    """

sql_update_score_and_frequency = """
    update  AllEnglishKnowledge 
    set score ={}-1 , frequency={}+1 
    where id ={}
    """

sql_update_delete = """
    update  AllEnglishKnowledge 
    set score ={}+1 , frequency={}+1,is_delete=1 
    where id ={}
    """

sql_all_id_and_score = """
    select id, score
    from AllEnglishKnowledge
    where score = 100
      and ABS(TIMESTAMPDIFF(minute, create_time, update_time)) <= 10
      # and table_name = 'sentence'
      and is_delete = 0
      """
