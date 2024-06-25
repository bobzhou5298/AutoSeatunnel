# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:20, 星期三


class SinkUsage:
    connector = {}
    Common_Options = {
        'source_table_name: 原表名称': """ 文件输出路径"""
        , 'parallelism: 并行数，默认1': """ 是否自定义文件名"""
    }
    LocalFile = {
        'path': """ 文件输出路径"""
        , 'custom_filename': """ 是否自定义文件名"""
        , 'file_name_expression': """ 文件名表达式"""
        , 'filename_time_format': """ 文件名时间格式"""
        , 'file_format_type': """ 文件格式，支持text,csv,json,orc,parquet,excel"""
        , 'field_delimiter': """ 字段分隔符格式"""
        , 'row_delimiter': """ 换行符格式"""
        , 'have_partition': """ 是否分区"""
        , 'partition_by': """ 分区字段组"""
        , 'partition_dir_expression': """ 分区表达式"""
        , 'is_partition_field_write_in_file': """ 是否输出分区字段到文件"""
        , 'sink_columns': """ 输出字段"""
        , 'is_enable_transaction': """ 是否开启事务"""
        , 'batch_size': """ 文件最大行数"""
        , 'compress_codec': """ 文件压缩格式"""
        , 'common-options': """ 公共参数"""
        , 'max_rows_in_memory': """ excel文件最大内存行数"""
        , 'sheet_name': """ excel文件sheet名称"""
    }

    AmazonDynamoDB = {}
    Assert = {}
    Cassandra = {}
    Clickhouse = {}
    ClickhouseFile = {}
    Console = {}
    CosFile = {}
    DataHub = {}
    DB2 = {}
    DingTalk = {}
    Doris = {}
    Elasticsearch = {}
    Email = {}
    Enterprise_WeChat = {
        'url':"""webhook连接url"""
        ,'mentioned_list':"""通知人员列表"""
        ,'mentioned_mobile_list':"""通知人员手机号列表"""
    }
    Feishu = {}
    FtpFile = {}
    GoogleFirestore = {}
    Greenplum = {}
    Hbase = {}
    HdfsFile = {}
    Hive = {}
    Http = {}
    InfluxDB = {}
    IoTDB = {}
    JDBC = {}
    Kafka = {}
    Kudu = {}
    Maxcompute = {}
    MongoDB = {'uri': '''url连接'''
        , 'database': '''数据库'''
        , 'collection': '''集合'''
        , 'schema': '''模式'''
        , 'match_query': '''查询'''
        , 'match_projection': ''''''
        , 'partition_split_key': ''''''
        , 'partition_split_size': ''''''
        , 'cursor_no_timeout': ''''''
        , 'fetch_size': ''''''
        , 'max_time_min': ''''''
        , 'flat_sync_string': ''''''
               }
    MySQL = {}
    Neo4j = {}
    OceanBase = {}
    Oracle = {}
    OssFile = {}
    OssJindoFile = {}
    Paimon = {}
    Phoenix = {}
    PostgreSql = {}
    Rabbitmq = {}
    Redis = {}
    RocketMQ = {}
    S3File = {}
    S3Redshift = {}
    SelectDB_Cloud = {}
    Sentry = {}
    SftpFile = {}
    Slack = {}
    Snowflake = {}
    Socket = {}
    StarRocks = {}
    Tablestore = {}
    TDengine = {}
    Vertica = {}

    helps = {
        'AmazonDynamoDB': AmazonDynamoDB,
        'Assert': Assert,
        'Cassandra': Cassandra,
        'Clickhouse': Clickhouse,
        'ClickhouseFile': ClickhouseFile,
        'Console': Console,
        'CosFile': CosFile,
        'DataHub': DataHub,
        'DB2': DB2,
        'DingTalk': DingTalk,
        'Doris': Doris,
        'Elasticsearch': Elasticsearch,
        'Email': Email,
        'Enterprise_WeChat': Enterprise_WeChat,
        'Feishu': Feishu,
        'FtpFile': FtpFile,
        'GoogleFirestore': GoogleFirestore,
        'Greenplum': Greenplum,
        'Hbase': Hbase,
        'HdfsFile': HdfsFile,
        'Hive': Hive,
        'Http': Http,
        'InfluxDB': InfluxDB,
        'IoTDB': IoTDB,
        'JDBC': JDBC,
        'Kafka': Kafka,
        'Kudu': Kudu,
        'LocalFile': LocalFile,
        'Maxcompute': Maxcompute,
        'MongoDB': MongoDB,
        'MySQL': MySQL,
        'Neo4j': Neo4j,
        'OceanBase': OceanBase,
        'Oracle': Oracle,
        'OssFile': OssFile,
        'OssJindoFile': OssJindoFile,
        'Paimon': Paimon,
        'Phoenix': Phoenix,
        'PostgreSql': PostgreSql,
        'Rabbitmq': Rabbitmq,
        'Redis': Redis,
        'RocketMQ': RocketMQ,
        'S3File': S3File,
        'S3Redshift': S3Redshift,
        'SelectDB_Cloud': SelectDB_Cloud,
        'Sentry': Sentry,
        'SftpFile': SftpFile,
        'Common_Options': Common_Options,
        'Slack': Slack,
        'Snowflake': Snowflake,
        'Socket': Socket,
        'StarRocks': StarRocks,
        'Tablestore': Tablestore,
        'TDengine': TDengine,
        'Vertica': Vertica
    }
