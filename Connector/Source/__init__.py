# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 14:09, 星期三
from Config import Seatunnel
from Config.Source import SourceArgs


def write_file(dic=None, outfile=Seatunnel.script_path + '/test.config', source_type='JDBC'):
    print(source_type, "{", file=outfile)
    print(dic)
    for key, value in dic.items():
        # print(key,value)
        if value is not None:
            if key in SourceArgs.source_dic[source_type]:
                print(key, '=', value, sep="", file=outfile)
            else:
                print(key, '="', value, '"', sep="", file=outfile)
        continue
    print("}", file=outfile)


def get_args(dic, source_type='JDBC'):
    print("***************************Source连接器", source_type, "的配置情况如下：***************************")
    print(source_type, "{")
    for key, value in dic.items():
        if value is not None:
            if key in SourceArgs.source_dic[source_type]:
                print(key, '=', value, sep="")
            else:
                print(key, '="', value, '"', sep="")
        continue
    print("}", '\n*********************************************************************************')


def set_source(script_path=Seatunnel.script_path + '/test.config', connector=None, source_type=None):
    file = open(script_path, 'a+')
    print("source{", file=file)
    write_file(outfile=file, dic=connector, source_type=source_type)
    print("}", file=file)
    file.close()
    get_args(dic=connector, source_type=source_type)

