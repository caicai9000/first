import requests

def test_geteventlist():
    """
    查询所有活动
    :return:
    """
    res = requests.get(url='http://123.56.99.53:9000/event/api/get_eventlist/',
                        headers={"uid": "4", "key": "ab97f63764b608f6d01909d67b4a1c6d"},
                        params={"rstr": "123"})

    assert res.status_code == 200, '相应状态码非200'