import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()
s1 = driver.find_element(By.ID, 'kw')
s1.send_keys('hihihi'+Keys.RETURN)


time.sleep(3)
driver.close()