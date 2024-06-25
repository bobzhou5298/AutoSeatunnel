# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:53, 星期三
from Config import Transform


class FieldMapper(Transform):

    def __init__(self, field_mapper=None, result_table_name=None, source_table_name=None):
        self.field_mapper = field_mapper
        self.result_table_name = result_table_name
        self.source_table_name = source_table_name

    def set(self):
        dic = dict()
        for item in self.FieldMapper:
            if item == 'field_mapper':
                dic[item] = self.field_mapper
            if item == 'result_table_name':
                dic[item] = self.result_table_name
            if item == 'source_table_name':
                dic[item] = self.source_table_name
        return dic
