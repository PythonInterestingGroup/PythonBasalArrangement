# -*- coding: utf-8 -*-
#author dm
#http://blog.csdn.net/c406495762/article/details/72331737

# Selenium
#pip3 install selenium
#官方文档http://selenium-python.readthedocs.io/index.html

from selenium import webdriver

#打开浏览器
#print( os.environ.get('PATH'))
#browser=webdriver.Chrome()  #需配置环境变量
#browser = webdriver.Chrome(r'C:\Users\lenovo\AppData\Local\Google\Chrome\Application\chromedriver.exe')
#browser.get('http://www.baidu.com/')

#模拟提交搜索
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print(driver.page_source)
'''

'''
单个元素选取：
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
多个元素选取:
find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
利用 By 类来确定哪种选择方式：
from selenium.webdriver.common.by import By
driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')
By类的一些属性如下：
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

eg:找到下面这个元素：
<input type="text" name="passwd" id="passwd-id" />
获取方式可以如下：
element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_elements_by_tag_name("input")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
'''

#鼠标单击事件：
#elem = driver.find_element_by_xpath("//a[@data-fun='next']")
#elem.click()

#将窗口滑动到page这个位置，在这个位置，我们能够看到我们需要点击的按键。
#page = driver.find_elements_by_xpath("//div[@class='page']")
#driver.execute_script('arguments[0].scrollIntoView();', page[-1]) #拖动到可见的元素去

#使用webdriver，可以更改User-Agent
options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.baidu.com/')

#Xpath 元素查找方式，使用这种方法几乎可以定位到页面上的任意元素
#XPath是XML Path的简称，由于HTML文档本身就是一个标准的XML页面，所以我们可以使用XPath的语法来定位页面元素。

#绝对路径/开头 相对路径//
'''
相对路径的引用写法：
查找页面根元素：//
查找页面上所有的input元素：//input
查找页面上第一个form元素内的直接子input元素(即只包括form元素的下一级input元素，使用绝对路径表示，单/号)：//form[1]/input
查找页面上第一个form元素内的所有子input元素(只要在form元素内的input都算，不管还嵌套了多少个其他标签，使用相对路径表示，双//号)：//form[1]//input
查找页面上第一个form元素：//form[1]
查找页面上id为loginForm的form元素：//form[@id='loginForm']
查找页面上具有name属性为username的input元素：//input[@name='username']
查找页面上id为loginForm的form元素下的第一个input元素：//form[@id='loginForm']/input[1]
查找页面具有name属性为contiune并且type属性为button的input元素：//input[@name='continue'][@type='button']
查找页面上id为loginForm的form元素下第4个input元素：//form[@id='loginForm']/input[4]
引用id为“J_password”的input元素 :
//*[@id='J_login_form']/dl/dt/input[@id='J_password']
或者//*[@id='J_login_form']/*/*/input[@id='J_password']
'''
