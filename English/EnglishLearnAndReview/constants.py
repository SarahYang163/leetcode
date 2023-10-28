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

# soup_context = [["basic", "word-exp"], ["webPhrase", "mcols-layout"], ["blng_sents_part dict-module", "mcols-layout"]]
soup_context = [["basic", "word-exp"], ["webPhrase", "mcols-layout"], ["blng_sents_part dict-module", "mcols-layout"],
                ["phone_con", "phonetic"]]
# 查询出所有需要的字段
sql_all_field = """
    select English, Chinese, score, id, frequency, table_name
    from AllEnglishKnowledge
    where id ={} 
    """

sql_update_score_and_frequency_minus = """
    update  AllEnglishKnowledge 
    set score ={}-1 , frequency={}+1 
    where id ={}
    """
sql_update_score_and_frequency_add = """
    update  AllEnglishKnowledge 
    set score ={}+1 , frequency={}+1 
    where id ={}
    """
sql_update_delete = """
    update  AllEnglishKnowledge 
    set score ={}+1 , frequency={}+1,is_delete=1 
    where id ={}
    """
sql_update_important = """
    update  AllEnglishKnowledge 
    set score ={}-10 , frequency={}+1 
    where id ={}
    """
sql_update_delete_unused = """
    update  AllEnglishKnowledge 
    set score ={}+1 , frequency={}+1,unused=1 
    where id ={}
    """
sql_update_unimportant = """
    update  AllEnglishKnowledge 
    set score ={}+10 , frequency={}+1
    where id ={}
    """
sql_all_id_and_score = """
    select id, score
    from AllEnglishKnowledge
    where  is_delete = 0
    and unused=0
    and table_name !='simple-sentence'
    and table_name !='sentence'
    # and score>100
    and score <101
    order by rand()
    limit 1000
    offset 2000
    """
sql_itls = """
    select id,question,answers
    from ieltsCentense
    order by rand(id)
    limit 10
    """
