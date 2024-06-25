# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 14:45, 星期三
from Config import Source


class Kafka(Source):

    def __init__(self, topic=None
                 , bootstrap_servers=None
                 , pattern='false'
                 , consumer_group='SeaTunnel-Consumer-Group'
                 , commit_on_checkpoint='true'
                 , kafka_config=None
                 , schema=None
                 , format='json'
                 , format_error_handle_way='fail'
                 , field_delimiter=None
                 , start_mode='group_offsets'
                 , start_mode_offsets=None
                 , start_mode_timestamp=None
                 , partition_discovery_interval_millis=1
                 , result_table_name=None
                 , parallelism=1
                 ) -> None:
        super().__init__()
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers
        self.pattern = pattern
        self.consumer_group = consumer_group
        self.commit_on_checkpoint = commit_on_checkpoint
        self.kafka_config = kafka_config
        self.schema = schema
        self.format = format
        self.format_error_handle_way = format_error_handle_way
        self.field_delimiter = field_delimiter
        self.start_mode = start_mode
        self.start_mode_offsets = start_mode_offsets
        self.start_mode_timestamp = start_mode_timestamp
        self.partition_discovery_interval_millis = partition_discovery_interval_millis
        self.result_table_name = result_table_name
        self.parallelism = parallelism

    def set(self):
        dic = dict()
        for item in self.Kafka:
            if item == 'topic':
                dic[item] = self.topic
            if item == 'bootstrap.servers':
                dic[item] = self.bootstrap_servers
            if item == 'pattern':
                dic[item] = self.pattern
            if item == 'consumer.group':
                dic[item] = self.consumer_group
            if item == 'commit_on_checkpoint':
                dic[item] = self.commit_on_checkpoint
            if item == 'kafka.config':
                dic[item] = self.kafka_config
            if item == 'schema':
                dic[item] = self.schema
            if item == 'format':
                dic[item] = self.format
            if item == 'format_error_handle_way':
                dic[item] = self.format_error_handle_way
            if item == 'field_delimiter':
                dic[item] = self.field_delimiter
            if item == 'start_mode':
                dic[item] = self.start_mode
            if item == 'start_mode.offsets':
                dic[item] = self.start_mode_offsets
            if item == 'start_mode_timestamp':
                dic[item] = self.start_mode_timestamp
            if item == 'partition-discovery.interval-millis	':
                dic[item] = self.partition_discovery_interval_millis
            if item == 'result_table_name':
                dic[item] = self.result_table_name
            if item == 'parallelism':
                dic[item] = self.parallelism
        return dic
