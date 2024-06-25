# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 14:39, 星期三

from Config import Source


class Hive(Source):

    def __init__(self, table_name=None
                 , metastore_uri=None
                 , kerberos_principal=None
                 , kerberos_keytab_path=None
                 , hdfs_site_path=None
                 , hive_site_path=None
                 , read_partitions=None
                 , read_columns=None
                 , abort_drop_partition_metadata="true"
                 , result_table_name=None
                 , parallelism=1
                 ):
        super().__init__()
        self.table_name = table_name
        self.metastore_uri = metastore_uri
        self.kerberos_principal = kerberos_principal
        self.kerberos_keytab_path = kerberos_keytab_path
        self.hdfs_site_path = hdfs_site_path
        self.hive_site_path = hive_site_path
        self.read_partitions = read_partitions
        self.read_columns = read_columns
        self.abort_drop_partition_metadata = abort_drop_partition_metadata
        self.result_table_name = result_table_name
        self.parallelism = parallelism

    def set(self):
        dic = dict()
        for item in self.Hive:
            if item == 'table_name':
                dic[item] = self.table_name
            if item == 'metastore_uri':
                dic[item] = self.metastore_uri
            if item == 'kerberos_principal':
                dic[item] = self.kerberos_principal
            if item == 'kerberos_keytab_path':
                dic[item] = self.kerberos_keytab_path
            if item == 'hdfs_site_path':
                dic[item] = self.hdfs_site_path
            if item == 'hive_site_path':
                dic[item] = self.hive_site_path
            if item == 'read_partitions':
                dic[item] = self.read_partitions
            if item == 'read_columns':
                dic[item] = self.read_columns
            if item == 'abort_drop_partition_metadata':
                dic[item] = self.abort_drop_partition_metadata
            if item == 'result_table_name':
                dic[item] = self.result_table_name
            if item == 'parallelism':
                dic[item] = self.parallelism
        return dic
