# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:20, 星期三


class SourceUage:
    connector = {}
    Common_Options = {
        'result_table_name: 结果表名': """"""
        , 'parallelism: 并行数 ，默认1    ': """"""
    }
    JDBC = {
        'url': """ jdbc连接，例如： jdbc:mysql://localhost/test"""
        , 'driver': """ jdbc驱动包名，例如：com.mysql.cj.jdbc.Driver"""
        , 'user': """ 用户名"""
        , 'password': """ 密码"""
        , 'query': """ 查询SQL"""
        , 'compatible_mode': """ 兼容模式，支持多种模式，例如：MySQL和Oracle"""
        , 'connection_check_timeout_sec': """ 连接检查超时时间，单位秒，数字型"""
        , 'partition_column': """ 分区字段"""
        , 'partition_upper_bound': """ 分区上线"""
        , 'partition_lower_bound': """ 分区下限"""
        , 'partition_num': """ 分区数量"""
        , 'fetch_size': """ 获取大小"""
        , 'common-options': """ 公共参数"""
    }
    AmazonDynamoDB = {}
    Apache_Iceberg = {}
    Apache_Pulsar = {}
    Cassandra = {}
    Clickhouse = {}
    CosFile = {}
    DB2 = {}
    Elasticsearch = {}
    FakeSource = {}
    FtpFile = {}
    Github = {}
    Gitlab = {}
    GoogleSheets = {}
    Greenplum = {}
    HdfsFile = {}
    Hive = {'table_name': """表名"""
        , 'metastore_uri': """元数据uri"""
        , 'kerberos_principal': """"""
        , 'kerberos_keytab_path': """"""
        , 'hdfs_site_path': """hdfs路径"""
        , 'hive_site_path': """hive路径"""
        , 'read_partitions': """读取分区数据"""
        , 'read_columns': """读取字段"""
        , 'abort_drop_partition_metadata': """"""}
    Http = {}
    Hudi = {}
    InfluxDB = {}
    IoTDB = {}
    Jira = {}
    Kafka = {}
    Klaviyo = {}
    Kudu = {}
    Lemlist = {}
    LocalFile = {'path': """文件路径"""
        , 'file_format_type': """文件格式"""
        , 'read_columns': """读取字段"""
        , 'delimiter': """字段分隔符"""
        , 'parse_partition_from_path': """分区"""
        , 'date_format': """日期格式"""
        , 'datetime_format': """日期时间格式"""
        , 'time_format': """时间格式"""
        , 'skip_header_row_number': """跳过首行记录"""
        , 'schema': """模式"""
        , 'sheet_name': """sheet页名字"""
        , 'file_filter_pattern': """文件过滤"""}
    Maxcompute = {}
    MongoDB = {
        'uri':"""url连接"""
        ,'database':"""数据库"""
        ,'collection':"""集合"""
        ,'schema':"""模式"""
        ,'match_query':"""查询"""
        ,'match_projection':""""""
        ,'partition_split_key':""""""
        ,'partition_split_size':""""""
        ,'cursor_no_timeout':""""""
        ,'fetch_size':""""""
        ,'max_time_min':""""""
        ,'flat_sync_string':""""""
    }
    MongoDB_CDC = {}
    My_Hours = {}
    MySQL = {}
    MySQL_CDC = {}
    Neo4j = {}
    Notion = {}
    OceanBase = {}
    OneSignal = {}
    OpenMldb = {}
    Oracle = {}
    OssFile = {}
    OssJindoFile = {}
    Paimon = {}
    Persistiq = {}
    Phoenix = {}
    PostgreSQL = {}
    Rabbitmq = {}
    Redis = {}
    RocketMQ = {}
    S3File = {}
    SftpFile = {}
    Snowflake = {}
    Socket = {}
    SqlServer_CDC = {}
    StarRocks = {}
    TDengine = {}
    Vertica = {}

    helps = {
        'AmazonDynamoDB': AmazonDynamoDB,
        'Apache_Iceberg': Apache_Iceberg,
        'Apache_Pulsar': Apache_Pulsar,
        'Cassandra': Cassandra,
        'Clickhouse': Clickhouse,
        'CosFile': CosFile,
        'DB2': DB2,
        'Elasticsearch': Elasticsearch,
        'FakeSource': FakeSource,
        'FtpFile': FtpFile,
        'Github': Github,
        'Gitlab': Gitlab,
        'GoogleSheets': GoogleSheets,
        'Greenplum': Greenplum,
        'HdfsFile': HdfsFile,
        'Hive': Hive,
        'Http': Http,
        'Hudi': Hudi,
        'InfluxDB': InfluxDB,
        'IoTDB': IoTDB,
        'JDBC': JDBC,
        'Jira': Jira,
        'Kafka': Kafka,
        'Klaviyo': Klaviyo,
        'Kudu': Kudu,
        'Lemlist': Lemlist,
        'LocalFile': LocalFile,
        'Maxcompute': Maxcompute,
        'MongoDB': MongoDB,
        'MongoDB_CDC': MongoDB_CDC,
        'My_Hours': My_Hours,
        'MySQL': MySQL,
        'MySQL_CDC': MySQL_CDC,
        'Neo4j': Neo4j,
        'Notion': Notion,
        'OceanBase': OceanBase,
        'OneSignal': OneSignal,
        'OpenMldb': OpenMldb,
        'Oracle': Oracle,
        'OssFile': OssFile,
        'OssJindoFile': OssJindoFile,
        'Paimon': Paimon,
        'Persistiq': Persistiq,
        'Phoenix': Phoenix,
        'PostgreSQL': PostgreSQL,
        'Rabbitmq': Rabbitmq,
        'Redis': Redis,
        'RocketMQ': RocketMQ,
        'S3File': S3File,
        'SftpFile': SftpFile,
        'Snowflake': Snowflake,
        'Socket': Socket,
        'Common_Options': Common_Options,
        'SqlServer_CDC': SqlServer_CDC,
        'StarRocks': StarRocks,
        'TDengine': TDengine,
        'Vertica': Vertica
    }
