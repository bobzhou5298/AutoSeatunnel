# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:11, 星期三
from Config import Seatunnel
from Config.Transform import TransformArgs


def write_file(dic, outfile='./source.conf', transform_type='Common_Options'):
    print(transform_type, "{", file=outfile)
    for key, value in dic.items():
        if value is not None:
            if key in TransformArgs.transform_dic[transform_type]:
                print(key, '=', value, sep="", file=outfile)
            else:
                print(key, '="', value, '"', sep="", file=outfile)
        continue
    print("}", file=outfile)


def get_args(dic, transform_type='Copy'):
    print("***************************Transform转换", transform_type, "的配置情况如下：***************************")
    print(transform_type, "{")
    for key, value in dic.items():
        if value is not None:
            if key in TransformArgs.transform_dic[transform_type]:
                print(key, '=', value, sep="")
            else:
                print(key, '="', value, '"', sep="")
        continue
    print("}", '\n*********************************************************************************')


def set_transform(script_path=Seatunnel.script_path + '/test.config', transform=None, transform_type=None):
    file = open(script_path, 'a+')
    print("transform{", file=file)
    write_file(outfile=file, dic=transform, transform_type=transform_type)
    print("}", file=file)
    file.close()
    get_args(dic=transform, transform_type=transform_type)
