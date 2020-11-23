import time
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('./chromedriver')
driver.get('http://www.google.com')
# 화면이 다 그러져야지만 작업이 가능하기 때문에 시간차를 줘야 화면이 다 그려지고 나서 작업 가능
time.sleep(1)

# 전체화면 driver.maximize_window()

search_box = driver.find_element_by_name('q')
search_box.send_keys('Chromedriver')
search_box.submit()
time.sleep(1)

from bs4 import BeautifulSoup
html = driver.page_source
# selenium으로 찾아들어간 페이지 소스(soup) 받기
soup = BeautifulSoup(html, 'html.parser')

titles = soup.select('div.yuRUbf > a > h3')
contents = soup.select('div.IsZvec > div > span')

""" # 똑같은 과정을 driver로 실행하기, 더 느림
titles = soup.find_elements_by_css_selecotr('div.yuRUbf > a > h3')
contents = soup.find_elements_by_css_selecotr('div.IsZvec > div > span')
 """

title_ls = []
content_ls = []

for title in titles:
    title_ls.append(title.text)

for content in contents:
    content_ls.append(content.text)

df = pd.DataFrame({
    'Title':title_ls,
    'Content':content_ls
})

df.to_csv('google.csv',sep=',')

