# basicwebscraping.py
import requests
from bs4 import BeautifulSoup


def Checkprice(QUOTE='KBANK'):

	url = 'https://www.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol={}&ssoPageId=9&selectPage=1'.format(QUOTE)

	rawdata = requests.get(url)
	rawdata = rawdata.content

	data = BeautifulSoup(rawdata,'html.parser')

	# print(data.prettify())

	# price = data.find_all('h1') 
	price = data.find_all('div',{'class':'col-xs-6'})
	#print(price)

	name = price[0].text.strip()
	stprice = float(price[2].text.strip())
	change = float(price[3].text.split()[-1])
	percentchange = float(price[4].text.split()[-1].replace('%',''))

	result = {'name':name,'price':stprice,'change':change,'percentchange':percentchange}

	print(result)

Checkprice('KTB')