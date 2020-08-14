import requests

def test_order():
    """
    预定活动
    :return:
    """
    res = requests.post(url='http://123.56.99.53:9000/event/api/order/',
                        headers={"uid": "4", "key": "ab97f63764b608f6d01909d67b4a1c6d",
                                 "Content-Type": "application/x-www-form-urlencoded"},
                        data={"rstr": "123", "eid": "10"})
    print(res.text)
    assert res.status_code == 200, '相应状态码非200'