# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:10, 星期三

from Config import Seatunnel
from Config.Sink import SinkArgs


def write_file(dic, outfile=Seatunnel.script_path + '/test.config', sink_type='LocalFile'):
    print(sink_type, "{", file=outfile)
    for key, value in dic.items():
        if value is not None:
            if key in SinkArgs.sink_dic[sink_type]:
                if key == 'sink_columns':
                    print(key, '=', str(value).replace("'", '"'), sep="", file=outfile)
                else:
                    print(key, '=', value, sep="", file=outfile)
            else:
                print(key, '="', value, '"', sep="", file=outfile)
        continue
    print("}", file=outfile)


def get_args(dic, sink_type='LocalFile'):
    print("***************************sink连接器", sink_type, "的配置情况如下：***************************")
    print(sink_type, "{")
    for key, value in dic.items():
        if value is not None:
            if key in SinkArgs.sink_dic[sink_type]:
                if key == 'sink_columns':
                    print(key, '=', str(value).replace("'", '"'), sep="")
                else:
                    print(key, '=', value, sep="")
            else:
                print(key, '="', value, '"', sep="")
        continue
    print("}", '\n*********************************************************************************')


def set_sink(script_path=Seatunnel.script_path + '/test.config', connector=None, sink_type=None):
    file = open(script_path, 'a+')
    print("sink{", file=file)
    write_file(outfile=file, dic=connector, sink_type=sink_type)
    print("}", file=file)
    file.close()
    get_args(dic=connector, sink_type=sink_type)
