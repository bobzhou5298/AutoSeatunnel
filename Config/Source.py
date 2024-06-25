# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:18, 星期三
from Config.Seatunnel import Seatunnel


class Source(Seatunnel):
    connector = [
        'AmazonDynamoDB',
        'Apache_Iceberg',
        'Apache_Pulsar',
        'Cassandra',
        'Clickhouse',
        'CosFile',
        'DB2',
        'Elasticsearch',
        'FakeSource',
        'FtpFile',
        'Github',
        'Gitlab',
        'GoogleSheets',
        'Greenplum',
        'HdfsFile',
        'Hive',
        'Http',
        'Hudi',
        'InfluxDB',
        'IoTDB',
        'JDBC',
        'Jira',
        'Kafka',
        'Klaviyo',
        'Kudu',
        'Lemlist',
        'LocalFile',
        'Maxcompute',
        'MongoDB',
        'MongoDB_CDC',
        'My_Hours',
        'MySQL',
        'MySQL_CDC',
        'Neo4j',
        'Notion',
        'OceanBase',
        'OneSignal',
        'OpenMldb',
        'Oracle',
        'OssFile',
        'OssJindoFile',
        'Paimon',
        'Persistiq',
        'Phoenix',
        'PostgreSQL',
        'Rabbitmq',
        'Redis',
        'RocketMQ',
        'S3File',
        'SftpFile',
        'Snowflake',
        'Socket',
        'Common_Options',
        'SqlServer_CDC',
        'StarRocks',
        'TDengine',
        'Vertica'

    ]
    connector_desc = {'JDBC': 'JDBC连接器', 'common_options': '公共参数'}
    Common_Options = ['result_table_name', 'parallelism']
    JDBC = ['url', 'driver', 'user', 'password', 'query', 'compatible_mode', 'connection_check_timeout_sec',
            'partition_column', 'partition_upper_bound', 'partition_lower_bound', 'partition_num',
            'fetch_size'] + Common_Options
    AmazonDynamoDB = [] + Common_Options
    Apache_Iceberg = [] + Common_Options
    Apache_Pulsar = [] + Common_Options
    Cassandra = [] + Common_Options
    Clickhouse = [] + Common_Options
    CosFile = [] + Common_Options
    DB2 = [] + Common_Options
    Elasticsearch = [] + Common_Options
    FakeSource = [] + Common_Options
    FtpFile = [] + Common_Options
    Github = [] + Common_Options
    Gitlab = [] + Common_Options
    GoogleSheets = [] + Common_Options
    Greenplum = [] + Common_Options
    HdfsFile = [] + Common_Options
    Hive = ['table_name', 'metastore_uri', 'kerberos_principal', 'kerberos_keytab_path', 'hdfs_site_path',
            'hive_site_path', 'read_partitions', 'read_columns', 'abort_drop_partition_metadata'] + Common_Options
    Http = [] + Common_Options
    Hudi = [] + Common_Options
    InfluxDB = [] + Common_Options
    IoTDB = [] + Common_Options
    Jira = [] + Common_Options
    Kafka = ['topic','bootstrap.servers','pattern','consumer.group','commit_on_checkpoint','kafka.config','schema','format','format_error_handle_way','field_delimiter','start_mode','start_mode.offsets','start_mode.timestamp','partition-discovery.interval-millis'] + Common_Options
    Klaviyo = [] + Common_Options
    Kudu = [] + Common_Options
    Lemlist = [] + Common_Options
    LocalFile = ['path', 'file_format_type', 'read_columns', 'delimiter', 'parse_partition_from_path', 'date_format',
                 'datetime_format', 'time_format', 'skip_header_row_number', 'schema', 'sheet_name',
                 'file_filter_pattern'] + Common_Options
    Maxcompute = [] + Common_Options
    MongoDB = ['uri', 'database', 'collection', 'schema', 'match.query', 'match.projection', 'partition.split-key',
               'partition.split-size', 'cursor.no-timeout', 'fetch.size', 'max.time-min',
               'flat.sync-string'] + Common_Options
    MongoDB_CDC = [] + Common_Options
    My_Hours = [] + Common_Options
    MySQL = [] + Common_Options
    MySQL_CDC = [] + Common_Options
    Neo4j = [] + Common_Options
    Notion = [] + Common_Options
    OceanBase = [] + Common_Options
    OneSignal = [] + Common_Options
    OpenMldb = [] + Common_Options
    Oracle = [] + Common_Options
    OssFile = [] + Common_Options
    OssJindoFile = [] + Common_Options
    Paimon = [] + Common_Options
    Persistiq = [] + Common_Options
    Phoenix = [] + Common_Options
    PostgreSQL = [] + Common_Options
    Rabbitmq = [] + Common_Options
    Redis = [] + Common_Options
    RocketMQ = [] + Common_Options
    S3File = ['path','file_format_type','bucket','fs.s3a.endpoint','fs.s3a.aws.credentials.provider','read_columns','access_key','access_secret','hadoop_s3_properties','delimiter','parse_partition_from_path','date_format','datetime_format','time_format','skip_header_row_number','schema','sheet_name'] + Common_Options
    SftpFile = [] + Common_Options
    Snowflake = [] + Common_Options
    Socket = [] + Common_Options
    SqlServer_CDC = [] + Common_Options
    StarRocks = [] + Common_Options
    TDengine = [] + Common_Options
    Vertica = [] + Common_Options

    source_dic = {
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


class SourceArgs:
    Common_Options = ['parallelism']
    JDBC = ['connection_check_timeout_sec', 'partition_upper_bound', 'partition_lower_bound', 'partition_num',
            'fetch_size'] + Common_Options
    AmazonDynamoDB = [] + Common_Options
    Apache_Iceberg = [] + Common_Options
    Apache_Pulsar = [] + Common_Options
    Cassandra = [] + Common_Options
    Clickhouse = [] + Common_Options
    CosFile = [] + Common_Options
    DB2 = [] + Common_Options
    Elasticsearch = [] + Common_Options
    FakeSource = [] + Common_Options
    FtpFile = [] + Common_Options
    Github = [] + Common_Options
    Gitlab = [] + Common_Options
    GoogleSheets = [] + Common_Options
    Greenplum = [] + Common_Options
    HdfsFile = [] + Common_Options
    Hive = ['read_partitions', 'read_columns'] + Common_Options
    Http = [] + Common_Options
    Hudi = [] + Common_Options
    InfluxDB = [] + Common_Options
    IoTDB = [] + Common_Options
    Jira = [] + Common_Options
    Kafka = ['kafka.config','start_mode.offsets','start_mode.timestamp','partition-discovery.interval-millis'] + Common_Options
    Klaviyo = [] + Common_Options
    Kudu = [] + Common_Options
    Lemlist = [] + Common_Options
    LocalFile = ['read_columns', 'skip_header_row_number'] + Common_Options
    Maxcompute = [] + Common_Options
    MongoDB = ['partition.split-size', 'fetch.size', 'max.time-min'] + Common_Options
    MongoDB_CDC = [] + Common_Options
    My_Hours = [] + Common_Options
    MySQL = [] + Common_Options
    MySQL_CDC = [] + Common_Options
    Neo4j = [] + Common_Options
    Notion = [] + Common_Options
    OceanBase = [] + Common_Options
    OneSignal = [] + Common_Options
    OpenMldb = [] + Common_Options
    Oracle = [] + Common_Options
    OssFile = [] + Common_Options
    OssJindoFile = [] + Common_Options
    Paimon = [] + Common_Options
    Persistiq = [] + Common_Options
    Phoenix = [] + Common_Options
    PostgreSQL = [] + Common_Options
    Rabbitmq = [] + Common_Options
    Redis = [] + Common_Options
    RocketMQ = [] + Common_Options
    S3File = ['read_columns','skip_header_row_number'] + Common_Options
    SftpFile = [] + Common_Options
    Snowflake = [] + Common_Options
    Socket = [] + Common_Options
    Common_Options = [] + Common_Options
    SqlServer_CDC = [] + Common_Options
    StarRocks = [] + Common_Options
    TDengine = [] + Common_Options
    Vertica = [] + Common_Options

    source_dic = {
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
