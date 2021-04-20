from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
from selenium.webdriver.common.keys import Keys


########real data#########
url = 'https://www.lazada.co.th/catalog/?q=iphone&_keyori=ss&from=input&spm=a2o4m.home.search.go.1125719cTmZ7xR'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
page_html = driver.page_source
#########################

'''
########test data#########
import htmlfile # htmlfile.py อยู่ในโฟลเดอร์เดียวกัน
page_html = htmlfile.html
#########################
'''
data = soup(page_html,'html.parser')
product = data.find_all('div',{'class':'c16H9d'}) # *****
print(product[0].text) # ชื่อ
print( 'htts:'+ product[0].a['href']) #ลิ้งค์
price = data.find_all('div',{'class':'c3gUW0'})  # *****
print(price[0].text.replace('฿','').replace(',','')) # ราคา

res_product = []
res_price = []
res_link = []

for p in product:
	res_product.append(p.text)
	res_link.append( 'https:' + p.a['href'])

for p in price:
	res_price.append(float(p.text.replace('฿','').replace(',','')))

sendtext = ''

for pd,pc,ln in zip(res_product,res_price,res_link):
	print(pd,pc,ln)
	sendtext = sendtext + 'Product: {}\nPrice: {:,.2f}\nLink: {}\n----------\n'.format(pd,pc,ln)

print(sendtext)


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendthai(sendto,subj="ทดสอบส่งเมลลล์",detail="สวัสดี!\nคุณสบายดีไหม?\n"):

	myemail = 'youremail@gmail.com'
	mypassword = 'yourpassword'
	receiver = sendto

	msg = MIMEMultipart('alternative')
	msg['Subject'] = subj
	msg['From'] = 'Uncle Engineer'
	msg['To'] = receiver
	text = detail

	part1 = MIMEText(text, 'plain')
	msg.attach(part1)

	s = smtplib.SMTP('smtp.gmail.com:587')
	s.ehlo()
	s.starttls()

	s.login(myemail, mypassword)
	s.sendmail(myemail, receiver.split(','), msg.as_string())
	s.quit()


###########Start sending#############
subject = 'ราคา Lazada'

msg = sendtext

sendthai('loong.wissawakorn@gmail.com',subject,msg)