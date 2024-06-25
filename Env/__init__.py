# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:14, 星期三
from Config import Seatunnel,Env


def write_file(dic, outfile=Seatunnel.script_path + '/test.config', env_type='env'):
    print(env_type, "{", file=outfile)
    for key, value in dic.items():
        if value is not None:
            if key in Env.EnvArgs.env:
                if key in 'parallelism':
                    key = 'execution.parallelism'
                    print(key.replace("_", "."), '=', value, sep="", file=outfile)
            else:
                print(key.replace("_", "."), '="', value, '"', sep="", file=outfile)
        continue
    print("}", file=outfile)


def get_args(dic, env_type='env'):
    print("***************************", env_type, "的配置情况如下：***************************")
    print(env_type, "{")
    for key, value in dic.items():
        if value is not None:
            if key in Env.EnvArgs.env:
                if key in 'parallelism':
                    key = 'execution.parallelism'
                    print(key.replace("_", "."), '=', value, sep="")
            else:
                print(key.replace("_", "."), '="', value, '"', sep="")
        continue
    print("}", '\n*********************************************************************************')


def set_env(scrip_path=Seatunnel.script_path + '/test.config', env=None):
    file = open(scrip_path, 'w')
    write_file(outfile=file, dic=env, env_type='env')
    file.close()
    get_args(dic=env, env_type='env')
