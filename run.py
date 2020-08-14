import pytest
import subprocess
import os
import time
# import sys
# sys.path.append('/Users/caicai/allure-2.13.3/bin')



if __name__ == '__main__':
    tmp = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    print(tmp)
    # pytest.main(['./cases', '-s', '--html=./report/report.html'])
    pytest.main(['./cases', '-s', '--alluredir=./report/json', '--clean-alluredir'])
    # subprocess.Popen('allure generate ./report/json -o ./report/html/'+tmp, shell=True)
    subprocess.call('allure generate ./report/json -o ./report/html/'+tmp, shell=True)
    # call方法阻塞线程，等子线程都结束后才结束主线程，在Jenkins里调用不会报错，Popen方法非阻塞，会报错
    # subprocess 返回一个可执行对象
    # os.popen('allure generate ./report/json -o ./report/html/final')
    # os.peon返回0和1
