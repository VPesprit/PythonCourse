import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://google.com/")
time.sleep(5)

capture_path = 'screen.jpg'
driver.save_screenshot(capture_path)

driver.get("http://demo.guru99.com/test/ajax.html")
driver.find_element(By.ID,"no").click()
time.sleep(5)
driver.find_element(By.ID,"buttoncheck").click()
time.sleep(5)
driver.quit()