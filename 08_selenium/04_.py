from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

from naverlogin import NaverLogin
import time
from myconfig import NAVER


class NaverMail:
    def request_webpage(self, url):
        self.url = url
        self.driver.get(self.url)

if __name__ == "__main__":
    # bot = NaverLogin()
    # bot.naver_url()
    # bot.login_btn()
    # bot.try_login()
    pass