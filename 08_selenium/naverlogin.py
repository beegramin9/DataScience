# 네이버 캡챠 피하기
from myconfig import NAVER
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip

class NaverLogin:
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.get('https://nid.naver.com/nidlogin.login')
        time.sleep(.5)

        # 요 방법은 class 안 써도 차단됨
        """ self.driver.execute_script(f"document.getElementsByName('id')[0].value=\'{NAVER['id']}\'")
        self.driver.execute_script(f"document.getElementsByName('pw')[0].value=\'{NAVER['pw']}\'")
        """

        # 아래는 클래스일때는 막히고 클래스가 아닐 때는 막히지 않음?
        """ 
        # ID박스
        pyperclip.paste()
        id_box = self.driver.find_element_by_id('id')
        id_box.clear()
        pyperclip.copy(NAVER['id'])
        id_box.send_keys(Keys.CONTROL, 'v')
        time.sleep(.5)

        # PW박스
        pw_box = self.driver.find_element_by_id('pw')
        pw_box.clear()
        pyperclip.copy(NAVER['pw'])
        pw_box.send_keys(Keys.CONTROL, 'v')
        time.sleep(.5) """

        # 로그인버튼
        self.driver.find_element_by_id('log.login').click()
