from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
# 1.웹 브라우저  주소창을 컨트롤하기 드라이버.get

driver.get("https://www.naver.com")
time.sleep(3)

selector = "#shortcutArea > ul > li:nth-child(3) > a > span.service_name"

# 2-2 찾아온 요소를 find_element로 가져오기
group_navi = driver.find_element(By.CSS_SELECTOR, selector)

# 3-1 데이터를 가져오기
print(group_navi.text)

# 3 -2 요소를 클릭하기[액션]
group_navi.click()
input()