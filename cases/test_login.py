import requests
import pytest

def test_login01():
    """
    正确登录
    :return:
    """
    res = requests.post(url='http://123.56.99.53:9000/event/api/login/',
                        headers={"Content-Type": "application/x-www-form-urlencoded"},
                        data={"username": "zhangsan", "password": "MTIzMTIzNDU2"})

    assert res.status_code == 200, '相应状态码非200'



def test_login02():
    """
    密码错误
    :return:
    """
    res = requests.post(url='http://123.56.99.53:9000/event/api/login/',
                        headers={"Content-Type": "application/x-www-form-urlencoded"},
                        data={"username": "zhangsan", "password": "123456"})

    assert res.status_code == 200, '相应状态码非200'


