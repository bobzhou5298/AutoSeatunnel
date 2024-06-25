# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:19, 星期三
from Uage.Env import EnvUsage
from Uage.Sink import SinkUsage
from Uage.Source import SourceUage
from Uage.Transform import TransformUsage


def helps(connector_type='source', mconnector='JDBC'):
    print('*********************************', mconnector, '帮助信息************************************')
    if connector_type == 'source':
        for key, value in SourceUage.helps[mconnector].items():
            print(key, value, sep=':', end='')
            print('')
        print('公共参数:')
        for key, value in SourceUage.Common_Options.items():
            print(key, value, sep=':', end='')
            print('')
    if connector_type == 'sink':
        for key, value in SinkUsage.helps[mconnector].items():
            print(key, value, sep=':', end='')
            print('')
        print('公共参数:')
        for key, value in SinkUsage.Common_Options.items():
            print(key, value, sep=':', end='')
            print('')
    if connector_type == 'transform':
        for key, value in TransformUsage.helps[mconnector].items():
            print(key, value, sep=':', end='')
            print('')
        print('公共参数:')
        for key, value in TransformUsage.Common_Options.items():
            print(key, value, sep=':', end='')
            print('')
    if connector_type == 'env':
        for key, value in EnvUsage.env.items():
            print(key, value, sep=':', end='')
            print('')
    print('****************************************************************************')
