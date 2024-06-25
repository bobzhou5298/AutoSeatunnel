# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:54, 星期三

from Config import Transform


class SQL(Transform):
    def __init__(self, query=None, result_table_name=None, source_table_name=None):
        self.query = query
        self.result_table_name = result_table_name
        self.source_table_name = source_table_name

    def set(self):
        dic = dict()
        for item in self.SQL:
            if item == 'query':
                dic[item] = self.query
            if item == 'result_table_name':
                dic[item] = self.result_table_name
            if item == 'source_table_name':
                dic[item] = self.source_table_name
        return dic
