# oilprice.py


import requests
from bs4 import BeautifulSoup

def CheckOil():	
	url = 'https://www.shell.co.th/th_th/motorists/shell-fuels/fuel-price/app-fuel-prices.html'
	rawdata = requests.get(url)
	rawdata = rawdata.content
	data = BeautifulSoup(rawdata,'html.parser')

	oiltable = data.find('table',{'class':'cc_cursor'})
	#print(oiltable.find_all('tr')[3].text.strip())

	result = ''

	for oil in oiltable.find_all('tr')[1:]:
		text = oil.text.strip()
		#print(text)
		result += text + '\n'

	return result


res = CheckOil()
print(res)