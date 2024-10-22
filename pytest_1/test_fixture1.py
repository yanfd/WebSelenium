import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def test_baidu(driver):
    driver.get('https://www.baidu.com/')
    title = driver.title
    url = driver.current_url
    text = driver.find_element(By.XPATH, '//*[@id="s-top-left"]/a[1]').text
    button_text = driver.find_element(By.ID, 'su').accessible_name
    assert title == '百度一下，你就知道'
    assert url == 'https://www.baidu.com/'
    assert text == '新闻'
    assert button_text == '百度一下'
    time.sleep(3)
    driver.quit()




