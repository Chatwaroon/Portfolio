# weblogin.py
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
from selenium.webdriver.common.keys import Keys

opt = webdriver.ChromeOptions() #สร้างออปชั่น
opt.add_argument('headless') #สั่งให้ไม่ต้องเปิด Chrome ขึ้นมา

loginurl = 'http://www.uncle-machine.com/login/'
driver = webdriver.Chrome(options=opt)
driver.get(loginurl)

username = driver.find_element_by_name('username')
username.send_keys('john999@gmail.com')

password = driver.find_element_by_name('password')
password.send_keys('1234')

button = driver.find_element_by_xpath('/html/body/div[2]/form/button')
button.click()

# หลังจากกรอกข้อมูลผู้สมัครแล้ว จะเข้าลิ้งค์ homepage
time.sleep(2)
homepage = 'http://www.uncle-machine.com/'
driver.get(homepage) # สั่งเปิดหน้า homepage

time.sleep(1) # หน่วงเวลา ขึ้นอยู่กับเว็บไซต์
page_html = driver.page_source # สั่งดึง source code (html) ออกมา

data = soup(page_html,'html.parser')

# get data from element by selenium
product = driver.find_element_by_class_name('card-header')
text = product.get_attribute('innerHTML') # ดึงข้อมูลจาก element ตัวนั้นๆ

driver.close() # **** ปิด driver ทันทีหลังจากได้ html

#############header##############
header = []
allproduct = data.find_all('div',{'class':'card-header'})
for p in allproduct:
	header.append(p.text.strip().split(':')[1].strip())
header = header[:10]

#############price##############
price = []
allprice = data.find_all('div',{'class':'card-body'})
for p in allprice:
	price.append(p.text.strip().split(':')[1].strip())
price = price[:10]

print(header)
print(price)

for h,p in zip(header,price):
	print('สินค้า: {} ราคา: {}'.format(h,p))



#print(header)











'''
search = driver.find_element_by_name('q') 
# บอก driver ว่าให้หาปุ่มช่องค้นหาให้หน่อย
search.send_keys('ราคาน้ำมัน')
search.send_keys(Keys.RETURN)
'''







