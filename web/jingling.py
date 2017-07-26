# -- coding: UTF-8 -- 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image,ImageEnhance
import pytesseract
def image_file_to_string(file):
    cwd = os.getcwd()
    try :
        os.chdir("/Users/essios/Desktop/2")
        return pytesser.image_file_to_string(file)
    finally:
        os.chdir(cwd)

driver = webdriver.Chrome()
driver.get("http://vip.ipjingling.com/")
# assert "Python" in driver.title
# elem = driver.find_element_by_id("Text_Login_EMail")
# elem.send_keys("1084933098@qq.com")
# elem = driver.find_element_by_id("Text_Login_Pwd")
# elem.send_keys("l31415926")

driver.get_screenshot_as_file('/Users/essios/Desktop/screen/image.jpg')#比较好理解
im =Image.open('/Users/essios/Desktop/screen/image.jpg')
# box = (800,730,870,780)  #设置要裁剪的区域
box = (750,260,820,300)  #设置要裁剪的区域
region = im.crop(box)     #此时，region是一个新的图像对象。
region.show()#显示的话就会被占用，所以要注释掉
region.save("/Users/essios/Desktop/img/image_code.jpg")
im=Image.open("/Users/essios/Desktop/img/image_code.jpg")
imgry = im.convert('L')#图像加强，二值化
sharpness =ImageEnhance.Contrast(imgry)#对比度增强
sharp_img = sharpness.enhance(2.0)
sharp_img.save("/Users/essios/Desktop/img/image_code.jpg")
#http://www.cnblogs.com/txw1958/archive/2012/02/21/2361330.html
#imgry.show()#这是分布测试时候用的，整个程序使用需要注释掉
#imgry.save("E:\\image_code.jpg")

# code= pytesser.image_file_to_string("/Users/essios/Desktop/img/image_code.jpg")#code即为识别出的图片数字str类型
print(pytesseract.image_to_string(Image.open('/Users/essios/Desktop/img/image_code.jpg')))
# print(pytesseract.image_to_string(sharp_img))
# print code
# elem.send_keys(Keys.RETURN)
# print driver.page_source
