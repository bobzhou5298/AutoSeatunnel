# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:28, 星期三
import Config.Env


class Env(Config.Env):
    def __init__(self, job_name='Seatunnel'
                 , jars=None
                 , job_mode='BATCH'
                 , checkpoint_interval=None
                 , parallelism=1
                 , shade_identifier=None
                 ):
        super().__init__()
        self.job_name = job_name
        self.jars = jars
        self.job_mode = job_mode
        self.checkpoint_interval = checkpoint_interval
        self.parallelism = parallelism
        self.shade_identifier = shade_identifier


    def set(self):
        dic = dict()
        for item in self.env:
            if item == 'job_name':
                dic[item] = self.job_name
            if item == 'jars':
                dic[item] = self.jars
            if item == 'job_mode':
                dic[item] = self.job_mode
            if item == 'checkpoint_interval':
                dic[item] = self.checkpoint_interval
            if item == 'parallelism':
                dic[item] = self.parallelism
            if item == 'shade_identifier':
                dic[item] = self.shade_identifier
        return dic
