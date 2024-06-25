# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:18, 星期三
from Config.Seatunnel import Seatunnel


class Sink(Seatunnel):
    connector = ['AmazonDynamoDB', 'Assert', 'Cassandra', 'Clickhouse', 'ClickhouseFile', 'Console', 'CosFile',
                 'DataHub', 'DB2', 'DingTalk', 'Doris', 'Elasticsearch', 'Email', 'Enterprise_WeChat', 'Feishu',
                 'FtpFile', 'GoogleFirestore', 'Greenplum', 'Hbase', 'HdfsFile', 'Hive', 'Http', 'InfluxDB', 'IoTDB',
                 'JDBC', 'Kafka', 'Kudu', 'LocalFile', 'Maxcompute', 'MongoDB', 'MySQL', 'Neo4j', 'OceanBase', 'Oracle',
                 'OssFile', 'OssJindoFile', 'Paimon', 'Phoenix', 'PostgreSql', 'Rabbitmq', 'Redis', 'RocketMQ',
                 'S3File', 'S3Redshift', 'SelectDB_Cloud', 'Sentry', 'SftpFile', 'Common_Options', 'Slack', 'Snowflake',
                 'Socket', 'StarRocks', 'Tablestore', 'TDengine', 'Vertica', ]
    Common_Options = ['source_table_name', 'parallelism']
    LocalFile = ['custom_filename', 'is_enable_transaction', 'is_partition_field_write_in_file', 'have_partition',
                 'path', 'file_name_expression', 'filename_time_format', 'file_format_type',
                 'field_delimiter', 'row_delimiter', 'partition_by', 'partition_dir_expression',
                 'sink_columns', 'batch_size',
                 'compress_codec', 'Common_Options', 'max_rows_in_memory', 'sheet_name'] + Common_Options
    AmazonDynamoDB = [] + Common_Options
    Assert = [] + Common_Options
    Cassandra = [] + Common_Options
    Clickhouse = [] + Common_Options
    ClickhouseFile = [] + Common_Options
    Console = [] + Common_Options
    CosFile = [] + Common_Options
    DataHub = [] + Common_Options
    DB2 = [] + Common_Options
    DingTalk = [] + Common_Options
    Doris = [] + Common_Options
    Elasticsearch = [] + Common_Options
    Email = ['email_from_address','email_to_address','email_host','email_transport_protocol','email_smtp_auth','email_authorization_code','email_message_headline','email_message_content'] + Common_Options
    Enterprise_WeChat = ['url','mentioned_list','mentioned_mobile_list'] + Common_Options
    Feishu = [] + Common_Options
    FtpFile = [] + Common_Options
    GoogleFirestore = [] + Common_Options
    Greenplum = [] + Common_Options
    Hbase = [] + Common_Options
    HdfsFile = [] + Common_Options
    Hive = [] + Common_Options
    Http = [] + Common_Options
    InfluxDB = [] + Common_Options
    IoTDB = [] + Common_Options
    JDBC = [] + Common_Options
    Kafka = [] + Common_Options
    Kudu = [] + Common_Options
    Maxcompute = [] + Common_Options
    MongoDB = [] + Common_Options
    MySQL = [] + Common_Options
    Neo4j = [] + Common_Options
    OceanBase = [] + Common_Options
    Oracle = [] + Common_Options
    OssFile = [] + Common_Options
    OssJindoFile = [] + Common_Options
    Paimon = [] + Common_Options
    Phoenix = [] + Common_Options
    PostgreSql = [] + Common_Options
    Rabbitmq = [] + Common_Options
    Redis = [] + Common_Options
    RocketMQ = [] + Common_Options
    S3File = [] + Common_Options
    S3Redshift = [] + Common_Options
    SelectDB_Cloud = [] + Common_Options
    Sentry = [] + Common_Options
    SftpFile = [] + Common_Options
    Common_Options = [] + Common_Options
    Slack = [] + Common_Options
    Snowflake = [] + Common_Options
    Socket = [] + Common_Options
    StarRocks = [] + Common_Options
    Tablestore = [] + Common_Options
    TDengine = [] + Common_Options
    Vertica = [] + Common_Options

    sink_dic = {
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


class SinkArgs:
    Common_Options = ['parallelism']
    AmazonDynamoDB = [] + Common_Options
    Assert = [] + Common_Options
    Cassandra = [] + Common_Options
    Clickhouse = [] + Common_Options
    ClickhouseFile = [] + Common_Options
    Console = [] + Common_Options
    CosFile = [] + Common_Options
    DataHub = [] + Common_Options
    DB2 = [] + Common_Options
    DingTalk = [] + Common_Options
    Doris = [] + Common_Options
    Elasticsearch = [] + Common_Options
    Email = [] + Common_Options
    Enterprise_WeChat = ['mentioned_list','mentioned_mobile_list'] + Common_Options
    Feishu = [] + Common_Options
    FtpFile = [] + Common_Options
    GoogleFirestore = [] + Common_Options
    Greenplum = [] + Common_Options
    Hbase = [] + Common_Options
    HdfsFile = [] + Common_Options
    Hive = [] + Common_Options
    Http = [] + Common_Options
    InfluxDB = [] + Common_Options
    IoTDB = [] + Common_Options
    JDBC = [] + Common_Options
    Kafka = [] + Common_Options
    Kudu = [] + Common_Options
    LocalFile = ['batch_size', 'max_rows_in_memory', 'parallelism', 'sink_columns'] + Common_Options
    Maxcompute = [] + Common_Options
    MongoDB = [] + Common_Options
    MySQL = [] + Common_Options
    Neo4j = [] + Common_Options
    OceanBase = [] + Common_Options
    Oracle = [] + Common_Options
    OssFile = [] + Common_Options
    OssJindoFile = [] + Common_Options
    Paimon = [] + Common_Options
    Phoenix = [] + Common_Options
    PostgreSql = [] + Common_Options
    Rabbitmq = [] + Common_Options
    Redis = [] + Common_Options
    RocketMQ = [] + Common_Options
    S3File = [] + Common_Options
    S3Redshift = [] + Common_Options
    SelectDB_Cloud = [] + Common_Options
    Sentry = [] + Common_Options
    SftpFile = [] + Common_Options
    Slack = [] + Common_Options
    Snowflake = [] + Common_Options
    Socket = [] + Common_Options
    StarRocks = [] + Common_Options
    Tablestore = [] + Common_Options
    TDengine = [] + Common_Options
    Vertica = [] + Common_Options

    sink_dic = {
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
