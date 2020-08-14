import requests


class Client(object):
    base_url = ''

    def __init__(self, url, method, body_type, timeout=3):
        self.url = Client.base_url + url
        self.method = method
        self.body_type = body_type
        self.timeout = timeout
        self.headers = {}
        self.params = {}
        self.res = None

    def set_header(self, key, value):
        self.headers[key] = value


    def set_headers(self,data):
        if isinstance(data, dict):        #判断一个变量是否是某个类型
            self.headers = data
        else:
            raise Exception('头信息应该是字典！')

    def set_params(self):



    def send(self):
        if self.method == 'POST':
            pass
        elif self.method == 'GET':
            pass





class Method(object):

    POST = 'POST'
    GET = 'GET'

class Type(object):

    FORM = 'form'
    JSON = 'json'
    FILES = 'files'