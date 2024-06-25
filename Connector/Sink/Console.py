# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:49, 星期三
from Config import Sink


class Console(Sink):

    def __init__(self
                 , source_table_name=None
                 , parallelism=1) -> None:
        super().__init__()
        self.source_table_name = source_table_name
        self.parallelism = parallelism

    def set(self):
        dic = dict()
        for item in self.Console:
            if item == 'source_table_name':
                dic[item] = self.source_table_name
            if item == 'parallelism':
                dic[item] = self.parallelism
        return dic
