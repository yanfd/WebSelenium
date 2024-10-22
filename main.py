import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://sellshop.5istudy.online/sell/user/login_page')
driver.find_element(By.CSS_SELECTOR,'#username').send_keys('test13')
driver.find_element(By.CSS_SELECTOR,'#password').send_keys('123456')
driver.find_element(By.CSS_SELECTOR,'#login > form > p.login.button > input[type=submit]').click()

time.sleep(3)
driver.quit()
