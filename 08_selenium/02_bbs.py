import time
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains

import pandas as pd
from bs4 import BeautifulSoup

# Edge로 실행하려면?
# https://dejavuqa.tistory.com/193에서 보면 됨

driver = webdriver.Chrome('./chromedriver')
driver.get('http://200.1.220.254:3000/login')

# 페이지네이션이 전체화면이 아니면 안 나오네... 의미 없음
time.sleep(1)

driver.find_element_by_css_selector('#uid').send_keys('djy')
driver.find_element_by_css_selector('#pwd').send_keys('1234')
driver.find_element_by_class_name('btn.btn-primary').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

bids = [] ; titles = []; replycounts = []; names = []; times =[]; view_counts=[]

trs = soup.select('tr')
# print(trs)
for tr in trs[1:]:
    tds = tr.select('td') # 리스트로 나옴
    # text이든 get_text()이든 다 됨
    
    bid = tds[0].text ; bids.append(bid)
    
    span = tds[1].select_one('span')
    # 댓글수가 span태그 안에 들어가 있음
    # 즉 span태그가 있으면 댓글이 있는거고 없으면 댓글이 없음

    title = tds[1].text ; bracket = title.find('[')
    title = tds[1].text[:bracket] if span else title
    titles.append(title)

    replycount = tds[1].select_one('span.text-danger')
    replycount = 0 if replycount == None else replycount.text.strip('\[\]')
    replycounts.append(replycount)

    name = tds[2].get_text() ; names.append(name)
    time = tds[3].text ; times.append(time)
    view_count = tds[4].text ; view_counts.append(view_count)