import time
import selenium
from selenium import webdriver
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import csv

print('평점과 총 관객이 궁금한 마블 영화 시리즈 3개를 입력하시오(콤마로 구분할 것)')
print('ex:어벤져스: 엔드게임, 블랙 팬서, 앤트맨과 와스프, 시빌 워,닥터 스트레인지, 캡틴 마블')
program_list_string = input('>> : ')
program_list = program_list_string.split(',')

URL = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query='
driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get(url=URL)
result=[]
for movie in program_list:
    search_box=driver.find_element_by_name("query")
    search_box.send_keys(movie)
    search_btn=driver.find_element_by_class_name('bt_search')
    search_btn.click()
    Title = driver.find_element_by_class_name('title').text
    rating = driver.find_element_by_xpath("//div[@class = 'info_group'][3]/dd").text
    aud = driver.find_element_by_xpath("//div[@class = 'info_group'][4]/dd").text

    result.append([Title,rating,aud])
    time.sleep(3)
    search_box = driver.find_element_by_name('query')
    search_box.clear()
time.sleep(3)
print(result)
driver.close()

with open('movie_score.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['영화명','평점','관객수'])
    for i in result:
        writer.writerow(i)

df=pd.read_csv('movie_score.csv', index_col='영화명', encoding='euc-kr')
plt.rc('font', family='Malgun Gothic')
ax=df.plot(kind='bar', figsize=(2000,3),legend = True, fontsize=12)
ax.set_xlabel('영화명',fontsize=12)
ax.set_ylabel('평점',fontsize=12)
ax.legend(['평점'],fontsize=12)
plt.show()
