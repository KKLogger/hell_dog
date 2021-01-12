import urllib3
import requests
import time
from selenium import webdriver
import pyperclip
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
def clipboard_input(driver,tag_id, input_value):
    pyperclip.paste()
    pyperclip.copy(input_value)
    driver.find_element_by_id(tag_id).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(
        Keys.CONTROL
    ).perform()
    time.sleep(1)

def getDriver():
    path = "./chromedriver.exe"
    driver = webdriver.Chrome(path)
    options = webdriver.ChromeOptions()
    fake_agent = UserAgent().random
    print(fake_agent)
    options.add_argument(f"user-agent={fake_agent}")
    return driver
def login(driver,user_id,user_pw):
    clipboard_input(driver, 'id', user_id)
    clipboard_input(driver, 'pw', user_pw)
    driver.find_element_by_id("log.login").click()
driver = getDriver()
driver.get("https://cafe.naver.com/dosomethingdo")
time.sleep(1)
"""
네이버 로그인
"""
login(driver,'sj981009','ehlswkd1!')

"""
글쓰기
"""
driver.find_element_by_xpath('//*[@id="cafe-info-data"]/div[2]/a').click() # 글쓰기 버튼 클릭
driver.switch_to.window(driver.window_handles[1]) # 탭 이동
time.sleep(1)
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div/section/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[1]')))
driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[1]').click() # 게시판 선택 창 클릭
time.sleep(1)
input()
driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[2]/ul/li[1]/button').click() # 원하는 게시판 선택

time.sleep(1)
input()
# naver 에디터가 iframe 이라서 교체
time.sleep(10)
driver.switch_to_frame(driver.find_element_by_id("cafe_main"))

subject = driver.find_element_by_id("subject")
subject.clear()
subject.send_keys(u"제목")

on_html_bt = driver.find_element_by_id("elHtmlMode")
on_html_bt.click()

"""
내용작성
"""
html_body = driver.find_element_by_id("textbox")

on_html_bt = driver.find_element_by_id("elHtmlMode")
on_html_bt.click()

## Switch back to the "default content" (that is, out of the iframes) ##
driver.find_element_by_xpath('//*[@id="nboard"]/div[3]/a[3]').click()
