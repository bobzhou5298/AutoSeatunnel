# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 14:42, 星期三

from Config import Source


class LocalFile(Source):

    def __init__(self, path=None
                 , file_format_type=None
                 , read_columns=None
                 , delimiter=";"
                 , parse_partition_from_path="true"
                 , date_format="yyyy-MM-dd"
                 , datetime_format="yyyy-MM-dd HH:mm:ss"
                 , time_format="HH:mm:ss"
                 , skip_header_row_number=None
                 , schema=None
                 , sheet_name=None
                 , file_filter_pattern=None
                 , result_table_name=None
                 , parallelism=1
                 ) -> None:
        super().__init__()
        self.path = path
        self.file_format_type = file_format_type
        self.read_columns = read_columns
        self.delimiter = delimiter
        self.parse_partition_from_path = parse_partition_from_path
        self.date_format = date_format
        self.datetime_format = datetime_format
        self.time_format = time_format
        self.skip_header_row_number = skip_header_row_number
        self.schema = schema
        self.sheet_name = sheet_name
        self.file_filter_pattern = file_filter_pattern
        self.result_table_name = result_table_name
        self.parallelism = parallelism

    def set(self):
        dic = dict()
        for item in self.LocalFile:
            if item == 'path':
                dic[item] = self.path
            if item == 'file_format_type':
                dic[item] = self.file_format_type
            if item == 'read_columns':
                dic[item] = self.read_columns
            if item == 'delimiter':
                dic[item] = self.delimiter
            if item == 'parse_partition_from_path':
                dic[item] = self.parse_partition_from_path
            if item == 'date_format':
                dic[item] = self.date_format
            if item == 'datetime_format':
                dic[item] = self.datetime_format
            if item == 'time_format':
                dic[item] = self.time_format
            if item == 'skip_header_row_number':
                dic[item] = self.skip_header_row_number
            if item == 'schema':
                dic[item] = self.schema
            if item == 'sheet_name':
                dic[item] = self.sheet_name
            if item == 'file_filter_pattern':
                dic[item] = self.file_filter_pattern
            if item == 'result_table_name':
                dic[item] = self.result_table_name
            if item == 'parallelism':
                dic[item] = self.parallelism
        return dic
