# -*- coding: utf-8 -*-
# Date: 2020/9/19
import os
import configparser

#读取配置文件目录
cur_path = os.getcwd()
config_path = os.path.join(cur_path,'conf\config.ini')
print(cur_path)
print(config_path)

# 读取配置文件
conf = configparser.ConfigParser()
conf.read(config_path)

# 遍历配置文件中的参数信息
host = conf.get('database', 'host')
port = int(conf.get('database', 'port'))
user = conf.get('database', 'user')
passwd = conf.get('database', 'passwd')
database = conf.get('database', 'database')
charset = conf.get('database', 'charset')

sql = conf.get('sql', 'query')
