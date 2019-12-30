import sys
from exitstatus import ExitStatus
from selenium import webdriver

def test_scores_service(app_url):
    web = webdriver.Firefox()
    web.implicitly_wait(10)
    web.get(app_url)
    tmp = web.find_element_by_id('score')
    score = int(tmp.text)
    print('Closing Browser')
    web.quit()
    print(score)
    if (score < 1000) and (score > 0):
        result = True
    else: result = False
    return result


# def main_function():
status = test_scores_service("http://0.0.0.0:8777")
print(status)
if status == True:
    sys.exit(ExitStatus.success)
else:
    sys.exit(ExitStatus.failure)


