# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 21:13, 星期三
from Config import Seatunnel
from Util import get_dbinfo

if __name__ == '__main__':
    get_dbinfo(Seatunnel.properties + '/Seatunnel.properties', name='MYSQL_QA203_READ')