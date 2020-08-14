from run import *
DATA = {"total": 0, "passed": 0, "failed": 0, "error": 0}

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item,call):
    result = yield
    data = result.get_result()
    if data.when == 'call':
        DATA['total'] += 1
        if data.outcome == 'passed':
            DATA['passed'] += 1
        elif data.outcome == 'failed':
            DATA['failed'] += 1
        elif data.outcome == 'error':
            DATA['error'] += 1