import requests


res = requests.post(url='http://123.56.99.53:9000/event/api/login/',
                    headers={"Content-Type": "application/x-www-form-urlencoded"},
                    data={"username": "zhangsan", "password": "MTIzMTIzNDU2"})
print(res.text)
assert res.status_code == 200, '相应状态码非200'