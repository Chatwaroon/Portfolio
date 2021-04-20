# temperature.py

import requests
from bs4 import BeautifulSoup

province = {'กรุงเทพมหานคร':'48455',
			'เชียงใหม่':'48327'}

def CheckTemp(name):	
	url = 'https://www.tmd.go.th/province.php?StationNumber={}'.format(province[name])
	rawdata = requests.get(url)
	rawdata = rawdata.content
	data = BeautifulSoup(rawdata,'html.parser')

	temp = data.find('td',{'class':'strokeme'})
	pvname = data.find('span',{'class':'title'})

	res_temp = temp.text
	res_pvname =pvname.text.strip()

	print(res_pvname,res_temp)
	#finddata = data.find_all('div',{'id':'button'})

CheckTemp('เชียงใหม่')