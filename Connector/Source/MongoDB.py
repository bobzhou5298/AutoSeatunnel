# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 14:43, 星期三
from Config import Source


class MongoDB(Source):

    def __init__(self, uri=None
                 , database=None
                 , collection=None
                 , schema=None
                 , match_query=None
                 , match_projection=None
                 , partition_split_key=None
                 , partition_split_size=None
                 , cursor_no_timeout=None
                 , fetch_size=None
                 , max_time_min=None
                 , flat_sync_string=None
                 , result_table_name=None
                 , parallelism=1
                 ) -> None:
        super().__init__()
        self.uri = uri
        self.database = database
        self.collection = collection
        self.schema = schema
        self.match_query = match_query
        self.match_projection = match_projection
        self.partition_split_key = partition_split_key
        self.partition_split_size = partition_split_size
        self.cursor_no_timeout = cursor_no_timeout
        self.fetch_size = fetch_size
        self.max_time_min = max_time_min
        self.flat_sync_string = flat_sync_string
        self.result_table_name = result_table_name
        self.parallelism = parallelism

    def set(self):
        dic = dict()
        for item in self.MongoDB:
            if item == 'uri':
                dic[item] = self.uri
            if item == 'database':
                dic[item] = self.database
            if item == 'collection':
                dic[item] = self.collection
            if item == 'schema':
                dic[item] = self.schema
            if item == 'match.query':
                dic[item] = self.match_query
            if item == 'match.projection':
                dic[item] = self.match_projection
            if item == 'partition.split-key':
                dic[item] = self.partition_split_key
            if item == 'partition.split-size':
                dic[item] = self.partition_split_size
            if item == 'cursor.no-timeout':
                dic[item] = self.cursor_no_timeout
            if item == 'fetch.size':
                dic[item] = self.fetch_size
            if item == 'max.time-min':
                dic[item] = self.max_time_min
            if item == 'flat.sync-string':
                dic[item] = self.flat_sync_string
            if item == 'result_table_name':
                dic[item] = self.result_table_name
            if item == 'parallelism':
                dic[item] = self.parallelism
        return dic
