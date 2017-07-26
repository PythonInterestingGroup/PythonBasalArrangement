# -- coding: UTF-8 -- 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image,ImageEnhance

driver = webdriver.Chrome()
driver.get("https://www.douban.com/")
# assert "Python" in driver.title
elem = driver.find_element_by_name("form_email")
elem.send_keys("1084933098@qq.com")
elem = driver.find_element_by_name("form_password")
elem.send_keys("l31415926")

driver.get_screenshot_as_file('/Users/essios/Desktop/screen/image.jpg')#比较好理解
im =Image.open('/Users/essios/Desktop/screen/image.jpg')
box = (516,417,564,437)  #设置要裁剪的区域
region = im.crop(box)     #此时，region是一个新的图像对象。
#region.show()#显示的话就会被占用，所以要注释掉
region.save("/Users/essios/Desktop/img/image_code.jpg")
elem.send_keys(Keys.RETURN)
print driver.page_source
