# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:48, 星期三
from Config import Sink


class LocalFile(Sink):

    def __init__(self, path=None
                 , custom_filename='true'
                 , file_name_expression=None
                 , filename_time_format='yyyyMMdd'
                 , file_format_type='text'
                 , field_delimiter=';'
                 , row_delimiter='\\n'
                 , have_partition='false'
                 , partition_by=None
                 , partition_dir_expression=None
                 , is_partition_field_write_in_file='false'
                 , sink_columns=None
                 , is_enable_transaction='true'
                 , batch_size=1000000
                 , compress_codec=None
                 , max_rows_in_memory=None
                 , sheet_name=None
                 , source_table_name=None
                 , parallelism=1
                 ):
        super().__init__()
        self.path = path
        self.custom_filename = custom_filename
        self.file_name_expression = file_name_expression
        self.filename_time_format = filename_time_format
        self.file_format_type = file_format_type
        self.field_delimiter = field_delimiter
        self.row_delimiter = row_delimiter
        self.have_partition = have_partition
        self.partition_by = partition_by
        self.partition_dir_expression = partition_dir_expression
        self.is_partition_field_write_in_file = is_partition_field_write_in_file
        self.sink_columns = sink_columns
        self.is_enable_transaction = is_enable_transaction
        self.batch_size = batch_size
        self.compress_codec = compress_codec
        self.max_rows_in_memory = max_rows_in_memory
        self.sheet_name = sheet_name
        self.source_table_name = source_table_name
        self.parallelism = parallelism

    def set(self):
        dic = dict()
        for item in self.LocalFile:
            if item == 'path':
                dic[item] = self.path
            if item == 'custom_filename':
                dic[item] = self.custom_filename
            if item == 'file_name_expression':
                dic[item] = self.file_name_expression
            if item == 'filename_time_format':
                dic[item] = self.filename_time_format
            if item == 'file_format_type':
                dic[item] = self.file_format_type
            if item == 'field_delimiter':
                dic[item] = self.field_delimiter
            if item == 'row_delimiter':
                dic[item] = self.row_delimiter
            if item == 'have_partition':
                dic[item] = self.have_partition
            if item == 'partition_by':
                dic[item] = self.partition_by
            if item == 'partition_dir_expression':
                dic[item] = self.partition_dir_expression
            if item == 'is_partition_field_write_in_file':
                dic[item] = self.is_partition_field_write_in_file
            if item == 'sink_columns':
                dic[item] = self.sink_columns
            if item == 'is_enable_transaction':
                dic[item] = self.is_enable_transaction
            if item == 'batch_size':
                dic[item] = self.batch_size
            if item == 'compress_codec':
                dic[item] = self.compress_codec
            if item == 'max_rows_in_memory':
                dic[item] = self.max_rows_in_memory
            if item == 'sheet_name':
                dic[item] = self.sheet_name
            if item == 'source_table_name':
                dic[item] = self.source_table_name
            if item == 'parallelism':
                dic[item] = self.parallelism
        return dic
