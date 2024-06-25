# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:24, 星期三


class TransformUsage:
    Common_Options = {
        'result_table_name': """结果表"""
        , 'source_table_name': """源表"""
    }
    Copy = {
        'fields': """复制新字段"""
    }
    FieldMapper = {
        'field_mapper': """字段映射，即重命名"""
    }
    Filter = {
        'fields': """过滤字段，即删除无需输出字段"""
    }
    FilterRowKind = {}
    Replace = {
        'replace_field': """"""
        , 'pattern': """"""
        , 'replacement': """"""
        , 'is_regex': """"""
        , 'replace_first': """"""
    }
    Split = {
        'separator': """"""
        , 'split_field': """"""
        , 'output_fields': """"""
    }
    SQL = {
        'source_table_name': """源表"""
        , 'result_table_name': """结果表"""
        , 'query': """查询SQL"""
    }
    SQL_Functions = {}
    SQL_UDF = {}

    helps = {
        'Copy': Copy,
        'FieldMapper': FieldMapper,
        'Filter': Filter,
        'FilterRowKind': FilterRowKind,
        'Replace': Replace,
        'Split': Split,
        'SQL': SQL,
        'SQL_Functions': SQL_Functions,
        'SQL_UDF': SQL_UDF,
        'Common_Options': Common_Options
    }
