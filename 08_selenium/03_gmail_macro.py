# 파이썬 자동화 셀레니움(selenium) webdriver와 actionchains으로 웹사이트 매크로 제작

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome('./chromedriver' ,options=options)
url = 'https://www.naver.com/'
driver.get(url)
action = ActionChains(driver)

driver.find_element_by_css_selector('.link_login .ico_naver').click()
# 만약 Bootstrap에서와 같이 클래스가 2개가 같이 띄어쓰기로 붙어있다면
# 띄어쓰기를 없애주고 .로 연결해준다. 


# # 따로 css요소를 찾지 않고, 커서가 처음부터 IDbox에 가 있는 점을 활용
# # 커서 있는 곳에서 바로 ActionChains 사용 가능
# 
# # 끝에 perform()을 해줘야 실행이 됨
(
# action.send_keys('beestron9')
# .key_down(Keys.TAB)
# .send_keys('wtchoe13')
# .key_down(Keys.TAB)
# .click()
# .perform()
)

import pyperclip


pyperclip.copy('beestron9')
pyperclip.copy('wtchoe13')

driver.find_element_by_id('log\.login').click()