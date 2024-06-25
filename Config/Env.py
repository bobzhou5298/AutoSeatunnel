# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:18, 星期三
from Config.Seatunnel import Seatunnel


class Env(Seatunnel):
    env = ['job_name', 'jars', 'job_mode', 'checkpoint_interval', 'parallelism', 'shade_identifier']


class EnvArgs:
    env = ['checkpoint_interval', 'parallelism']
