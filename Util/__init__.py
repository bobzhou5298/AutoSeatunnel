# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:15, 星期三
import os
import pymysql
import re


# 读取配置文件内容
def read_file(file=None, name=None):
    str = ''
    mfile = open(file=file, mode='r', encoding='utf8', newline='\n')
    for item in mfile:
        if re.search(name, item):
            # dic = item.split('=')[1]
            # dic[name] = item.split('=')[1].replace('\n','').replace('\r','')
            # dic = item.replace('\n','').replace('\r','')
            if '=' in item and name in item:
                str += item.replace('\r', '').replace('\n', '') + ','
        continue
    # print(lst)
    return str


def get_dbinfo(config_file=None, name=None, db_type='mysql'):
    conn = read_file(config_file, name)
    dbinfo = dict()
    for item in conn.split(','):
        if item != '':
            if 'ip' in item:
                ip = item.split('=')[1]
                dbinfo['ip'] = ip
            if 'port' in item:
                port = int(item.split('=')[1])
                dbinfo['port'] = port
            if 'user' in item:
                user = item.split('=')[1]
                dbinfo['user'] = user
            if 'password' in item:
                password = item.split('=')[1]
                dbinfo['password'] = password
    dbinfo['url'] = "jdbc:" + db_type + "://" + ip + ":" + str(port) + "/"
    return dbinfo


def get_db_data(config_file=None, name=None, db_type='mysql'):
    dbinfo = get_dbinfo(config_file=config_file, name=name, db_type='mysql')
    print(dbinfo.get('ip'), dbinfo.get('port'), dbinfo.get('user'), dbinfo.get('password'))
    db = pymysql.connect(host=dbinfo.get('ip'), port=dbinfo.get('port'), user=dbinfo.get('user'),
                         password=dbinfo.get('password'), charset='utf8')
    cursor = db.cursor()
    # cursor.execute("select * from information_schema.`COLUMNS`")
    cursor.execute(
        "select TABLE_SCHEMA ,TABLE_NAME,concat(\'select \',group_concat(COLUMN_NAME,\' as \',COLUMN_NAME) ,\' from \',TABLE_NAME),group_concat(COLUMN_NAME SEPARATOR \';\') from information_schema.`COLUMNS` group by TABLE_SCHEMA ,TABLE_NAME")
    rs = cursor.fetchall()
    # print(type(rs),'数据库结果集类型')
    # for rows in rs:
    #     # print(rows)
    #     for item in rows:
    #         rs_dic['database'] = rows[0]
    #         rs_dic['table'] = rows[1]
    #         rs_dic['sql'] = rows[2]
    #         # print(item)
    #     sql_lst = sql_lst.update(rs_dic)
    return rs


def create_dir(path="path"):
    if os.path.exists(path):
        print(path, '文件夹存在')
    else:
        print(print(path, '文件夹不存在'))
        os.makedirs(path)
