
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# 어떤 엘리먼트가 나올때 까지 기다리는데 기다리는 조건을 넣을 수 있다.
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

def wait_until(xpath_str):
    WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH, xpath_str)))

url = "https://flight.naver.com/"
browser = webdriver.Chrome() #크롬창 켜기
browser.maximize_window()
browser.get(url) # url 파라미터로 이동

#xpath 주소로 찾아오자! 오른쪽에는 xpath 주소, // 표시는 html 전체에서 찾겠다.
bigin_data = browser.find_element(By.XPATH, '//button[text() = "가는 날"]') 
bigin_data.click()

#time.sleep(1)
wait_until('//b[text() = "27"]')
day27 = browser.find_elements(By.XPATH, '//b[text() = "27"]')
day27[0].click()

wait_until('//b[text() = "31"]')
day31 = browser.find_elements(By.XPATH,'//b[text() = "31"]')
day31[0].click()

wait_until('//b[text() = "도착"]')
arrival = browser.find_element(By.XPATH,'//b[text() = "도착"]')
arrival.click()
time.sleep(1)

domestic = browser.find_element(By.XPATH, '//button[text() = "국내"]') 
domestic.click()

jeju = browser.find_element(By.XPATH,'//i[contains(text(), "제주국제공항")]') #제주 국제 공항을 포함하는 텍스트 가져오기
jeju.click()

search = browser.find_element(By.XPATH,'//span[text() = "항공권 검색"]')
search.click()

# 어떤 element가 나타날 때 까지 기다려줘, 클래스값 비교하려면 @ 클래스 앞에 작성
elem = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//div[@class = "domestic_Flight__sK0eA result"]')))
print(elem.text)

#browser.quit()
