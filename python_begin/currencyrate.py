# currencyrate.py

import requests
from bs4 import BeautifulSoup

def Currency():	
	url = 'https://www.bot.or.th/thai/_layouts/application/exchangerate/exchangerate.aspx'
	rawdata = requests.get(url)
	rawdata = rawdata.content
	data = BeautifulSoup(rawdata,'html.parser')

	table = data.find('div',{'class':'table-foreignexchange2'})
	
	rows = table.find_all('tr',{'class':'bg-gray'})
	imgurl = 'https://www.bot.or.th/thai/_layouts/application'

	allcurrency = {}

	for r in rows:
		column = r.find_all('td')
		#print(column[1].text,column[2].text,column[3].text,column[4].text,column[5].text)
		cc = {
				'name':column[1].text,
				'code':column[2].text.strip(),
				'buy':float(column[3].text.strip()),
				'sell':float(column[5].text)
		}
		#print(cc)
		allcurrency[cc['code']] = cc
		
		'''
		# Download Image
		image_url = imgurl + r.img['src'][2:]
		image_name = image_url.split('/')[-1]
		img_data = requests.get(image_url).content
		#print(img_data)
		with open(image_name, 'wb') as handler:
		    handler.write(img_data)
		'''

	return allcurrency

currency = Currency()
print(currency)
# print(currency['JPY'])



