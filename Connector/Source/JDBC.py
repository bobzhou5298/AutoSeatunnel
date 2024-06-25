# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 14:37, 星期三
from Config import Source


class JDBC(Source):
    def __init__(self, url=None
                 , driver='com.mysql.jdbc.Driver'
                 , user='root'
                 , password='root'
                 , query='SELECT 1'
                 , compatible_mode='mysql'
                 , connection_check_timeout_sec=1800
                 , partition_column=None
                 , partition_upper_bound=None
                 , partition_lower_bound=None
                 , partition_num=None
                 , fetch_size=10000
                 , result_table_name=None
                 , parallelism=1
                 ):
        super().__init__()
        self.url = url
        self.driver = driver
        self.user = user
        self.password = password
        self.query = query
        self.compatible_mode = compatible_mode
        self.connection_check_timeout_sec = connection_check_timeout_sec
        self.partition_column = partition_column
        self.partition_upper_bound = partition_upper_bound
        self.partition_lower_bound = partition_lower_bound
        self.partition_num = partition_num
        self.fetch_size = fetch_size
        self.result_table_name = result_table_name
        self.parallelism = parallelism

    def set(self):
        dic = dict()
        for item in self.JDBC:
            if item == 'url':
                dic[item] = self.url
            if item == 'driver':
                dic[item] = self.driver
            if item == 'user':
                dic[item] = self.user
            if item == 'password':
                dic[item] = self.password
            if item == 'query':
                dic[item] = self.query
            if item == 'compatible_mode':
                dic[item] = self.compatible_mode
            if item == 'connection_check_timeout_sec':
                dic[item] = self.connection_check_timeout_sec
            if item == 'partition_column':
                dic[item] = self.partition_column
            if item == 'partition_upper_bound':
                dic[item] = self.partition_upper_bound
            if item == 'partition_lower_bound':
                dic[item] = self.partition_lower_bound
            if item == 'partition_num':
                dic[item] = self.partition_num
            if item == 'fetch_size':
                dic[item] = self.fetch_size
            if item == 'result_table_name':
                dic[item] = self.result_table_name
            if item == 'parallelism':
                dic[item] = self.parallelism
        return dic
