# GUIstock.py

from tkinter import *
from tkinter import ttk, messagebox

#####################################
import requests
from bs4 import BeautifulSoup


def Checkprice(QUOTE='KBANK'):

	### url หน้าหุ่นแต่ละตัว
	url = 'https://www.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol={}&ssoPageId=9&selectPage=1'.format(QUOTE)

	### request ข้อมูล
	rawdata = requests.get(url)
	rawdata = rawdata.content

	### แปลงโค้ดเป็น bs4
	data = BeautifulSoup(rawdata,'html.parser')

	# print(data.prettify()) # แสดงผลให้มี space ขั้น tag หลัก tag ย่อย

	# price = data.find_all('h1') # ค้นหาเฉพาะ header 1

	### ค้นหาข้อมูลส่วนที่เกี่ยวกับราคา 
	price = data.find_all('div',{'class':'col-xs-6'})
	#print(price)


	# ดึงข้อมูลแต่ละส่วนออกมา
	name = price[0].text.strip()
	stprice = float(price[2].text.strip())
	change = float(price[3].text.split()[-1])
	percentchange = float(price[4].text.split()[-1].replace('%',''))

	### ดึงวันที่อัพเดต
	res = data.find('div',{'class':'flex-item text-left padding-8'})
	res = res.find_all('span')
	
	update = res[0].text
	marketstatus = res[1].text

	### ผลลัพธ์
	result = {'name':name,
			  'price':stprice,
			  'change':change,
			  'percentchange':percentchange,
			  'update':update,
			  'marketstatus':marketstatus}
	# print(result)
	return result

#####################################

GUI = Tk()
GUI.geometry('600x500')
GUI.title('โปรแกรมเช็คราคาหุ้น by Uncle Engineer')

FONT1 = ('Angsana New',20)

### ข้อความแสดงผล
L = ttk.Label(GUI,text='กรุณากรอกหุ้นที่ต้องการ',font=FONT1).pack(pady=10)

### ช่องสำหรับกรอกข้อมูล
v_quote = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_quote,font=FONT1,width=40)
E1.pack(pady=20)

### ปุ่มสำหรับกรอกหุ้น

allresult = []

def CheckStockPrice(event=None):
	global allresult
	# clear label
	for rs in allresult:
		rs.destroy() #ลบ label

	allresult = []

	v_result.set('') #clear result
	quote = v_quote.get().split(',')
	print(quote)

	for q in quote:
		try:
			price = Checkprice(q.strip())
			print(price)
			text = '{} ราคา: {} บาท '.format(price['name'],price['price'])
			text = text + 'เปลี่ยนแปลง: {} บาท  เปลี่ยนแปลง: {}%'.format(price['change'],price['percentchange'])
			print([price['percentchange']])
			if price['percentchange'] < 0:
				color = 'red'
			elif price['percentchange'] == 0:
				color = 'black'
			elif price['percentchange'] > 10:
				color = '#1d0680' #hex code color
			else:
				color = 'green'
		except:
			text = 'หุ้น: {} ไม่อยู่ในตลาดหุ้น'.format(q)
			color = 'orange'

		L = ttk.Label(GUI,text=text,foreground=color,font=FONT1)
		allresult.append(L)
		L.pack()

		#v_result.set(v_result.get() + text + '\n')
	

B1 = ttk.Button(GUI, text='Check Price',command=CheckStockPrice)
B1.pack(ipadx=20,ipady=10)

# if you press enter , will run the function

E1.bind('<Return>',CheckStockPrice)

### Result

v_result = StringVar()
v_result.set('-------Result-------')
FONT2 = ('Angsana New',15,'bold')
R1 = ttk.Label(GUI, textvariable=v_result,foreground='green',font=FONT2)
R1.pack(pady=10)


statusbar = Label(GUI,text='กดปุ่ม <F1> เพื่อขอความช่วยเหลือ')
statusbar.pack(side=BOTTOM)


def Help(event=None):
	text = 'หากมีคำถามกรุณาติดต่อเฟสบุ๊ค: ลุงวิศวกร สอนคำนวณ\nemail: loong.wissawakorn@gmail.com\n'
	text = text + 'Youtube: Uncle Engineer'
	messagebox.showinfo('Help',text)


GUI.bind('<F1>',Help)


GUI.mainloop()