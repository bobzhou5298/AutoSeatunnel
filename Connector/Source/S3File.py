# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 14:44, 星期三

from Config import Source


class S3File(Source):

    def __init__(self, path=None
                 , file_format_type=None
                 , bucket=None
                 , fs_s3a_endpoint=None
                 , fs_s3a_aws_credentials_provider='com.amazonaws.auth.InstanceProfileCredentialsProvider'
                 , read_columns=None
                 , access_key=None
                 , access_secret=None
                 , hadoop_s3_properties=None
                 , delimiter=';'
                 , parse_partition_from_path='true'
                 , date_format='yyyy-MM-dd'
                 , datetime_format='yyyy-MM-dd HH:mm:ss'
                 , time_format='HH:mm:ss'
                 , skip_header_row_number=0
                 , schema=None
                 , sheet_name=None
                 , result_table_name=None
                 , parallelism=1
                 ) -> None:
        super().__init__()
        self.path = path
        self.file_format_type = file_format_type
        self.bucket = bucket
        self.fs_s3a_endpoint = fs_s3a_endpoint
        self.fs_s3a_aws_credentials_provider = fs_s3a_aws_credentials_provider
        self.read_columns = read_columns
        self.access_key = access_key
        self.access_secret = access_secret
        self.hadoop_s3_properties = hadoop_s3_properties
        self.delimiter = delimiter
        self.parse_partition_from_path = parse_partition_from_path
        self.date_format = date_format
        self.datetime_format = datetime_format
        self.time_format = time_format
        self.skip_header_row_number = skip_header_row_number
        self.schema = schema
        self.sheet_name = sheet_name
        self.result_table_name = result_table_name
        self.parallelism = parallelism

    def set(self):
        dic = dict()
        for item in self.S3File:
            if item == 'path':
                dic[item] = self.path
            if item == 'file_format_type':
                dic[item] = self.file_format_type
            if item == 'bucket':
                dic[item] = self.bucket
            if item == 'fs.s3a.endpoint':
                dic[item] = self.fs_s3a_endpoint
            if item == 'fs.s3a.aws.credentials.provider':
                dic[item] = self.fs_s3a_aws_credentials_provider
            if item == 'read_columns':
                dic[item] = self.read_columns
            if item == 'access_key':
                dic[item] = self.access_key
            if item == 'access_secret':
                dic[item] = self.access_secret
            if item == 'hadoop_s3_properties':
                dic[item] = self.hadoop_s3_properties
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
            if item == 'result_table_name':
                dic[item] = self.result_table_name
            if item == 'parallelism':
                dic[item] = self.parallelism
        return dic
