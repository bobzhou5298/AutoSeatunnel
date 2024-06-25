# @project: AutoSeatunnel
# @function: 
# @author : bob.zhou
# @create_time: 2024/3/20 20:50, 星期三
from Config import Sink


class Email(Sink):
    def __init__(self, email_from_address=None
                 , email_to_address=None
                 , email_host=None
                 , email_transport_protocol='smtp'
                 , email_smtp_auth='true'
                 , email_authorization_code=None
                 , email_message_headline=None
                 , email_message_content=None
                 , source_table_name=None
                 , parallelism=1) -> None:
        super().__init__()
        self.email_from_address = email_from_address
        self.email_to_address = email_to_address
        self.email_host = email_host
        self.email_transport_protocol = email_transport_protocol
        self.email_smtp_auth = email_smtp_auth
        self.email_authorization_code = email_authorization_code
        self.email_message_headline = email_message_headline
        self.email_message_content = email_message_content
        self.source_table_name = source_table_name
        self.parallelism = parallelism

    def set(self):
        dic = dict()
        for item in self.Email:
            if item == 'email_from_address':
                dic[item] = self.email_from_address
            if item == 'email_to_address':
                dic[item] = self.email_to_address
            if item == 'email_host':
                dic[item] = self.email_host
            if item == 'email_transport_protocol':
                dic[item] = self.email_transport_protocol
            if item == 'email_smtp_auth':
                dic[item] = self.email_smtp_auth
            if item == 'email_authorization_code':
                dic[item] = self.email_authorization_code
            if item == 'email_message_headline':
                dic[item] = self.email_message_headline
            if item == 'email_message_content':
                dic[item] = self.email_message_content
            if item == 'source_table_name':
                dic[item] = self.source_table_name
            if item == 'parallelism':
                dic[item] = self.parallelism
        return dic
