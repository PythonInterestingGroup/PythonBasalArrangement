# https://home.ctfile.com/#item-files
#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
driver = webdriver.Chrome()
driver.get("https://home.ctfile.com/#item-files")
# assert "Python" in driver.title
# elem = driver.find_element_by_id("search-text")
# elem.send_keys("韩服王者")
# elem.send_keys(Keys.RETURN)
print (driver.page_source)