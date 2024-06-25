# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:18, 星期三
from Config.Seatunnel import Seatunnel


class Transform(Seatunnel):
    transform = ['FieldMapper', 'Filter', 'FilterRowKind', 'Replace', 'Split', 'SQL', 'SQL_Functions', 'SQL_UDF',
                 'Common_Options']
    Common_Options = ['result_table_name', 'source_table_name']
    Copy = ['fields'] + Common_Options
    FieldMapper = ['field_mapper'] + Common_Options
    Filter = ['fields'] + Common_Options
    FilterRowKind = [] + Common_Options
    Replace = ['replace_field', 'pattern', 'replacement', 'is_regex', 'replace_first'] + Common_Options
    Split = ['separator', 'split_field', 'output_fields'] + Common_Options
    SQL = ['source_table_name', 'result_table_name', 'query'] + Common_Options
    SQL_Functions = [] + Common_Options
    SQL_UDF = [] + Common_Options

    transform_dic = {
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


class TransformArgs:
    Common_Options = []
    Copy = ['fields'] + Common_Options
    FieldMapper = ['field_mapper'] + Common_Options
    Filter = ['fields'] + Common_Options
    FilterRowKind = [] + Common_Options
    Replace = [] + Common_Options
    Split = ['output_fields'] + Common_Options
    SQL = [] + Common_Options
    SQL_Functions = [] + Common_Options
    SQL_UDF = [] + Common_Options

    transform_dic = {
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
