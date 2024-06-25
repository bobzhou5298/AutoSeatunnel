# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:51, 星期三
from Config import Sink


class Enterprise_WeChat(Sink):

    def __init__(self, url=None
                 , mentioned_list=None
                 , mentioned_mobile_list=None
                 , source_table_name=None
                 , parallelism=1) -> None:
        super().__init__()
        self.url = url
        self.mentioned_list = mentioned_list
        self.mentioned_mobile_list = mentioned_mobile_list
        self.source_table_name = source_table_name
        self.parallelism = parallelism

    def set(self):
        dic = dict()
        for item in self.Enterprise_WeChat:
            if item == 'url':
                dic[item] = self.url
            if item == 'mentioned_list':
                dic[item] = self.mentioned_list
            if item == 'mentioned_mobile_list':
                dic[item] = self.mentioned_mobile_list
            if item == 'source_table_name':
                dic[item] = self.source_table_name
            if item == 'parallelism':
                dic[item] = self.parallelism
        return dic
