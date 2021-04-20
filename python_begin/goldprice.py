import requests
from bs4 import BeautifulSoup

def CheckGold():	
	url = 'https://www.goldtraders.or.th/'
	rawdata = requests.get(url)
	rawdata = rawdata.content
	data = BeautifulSoup(rawdata,'html.parser')

	goldtable = data.find('div',{'id':'DetailPlace_uc_goldprices1_GoldPricesUpdatePanel'})
	
	goldtable = goldtable.find_all('tr')
	
	current = ''
	cpercent = ''
	pricedict = {'ทองคำแท่ง':{},'ทองรูปพรรณ':{}}

	for row in goldtable[1:]:
		column = row.find_all('td')
		#print([column[0].text.strip(),column[1].text.strip(),column[2].text.strip()])

		buysell = column[1].text.strip()
		price = column[2].text.strip()
		goldtype = column[0].text.strip().split()

		if len(goldtype) == 2:
			gtype = goldtype[0]
			gpercent = goldtype[1]
			current = gtype
			cpercent = gpercent
			#print(current,cpercent)
			
		#print(current,cpercent,buysell,price)
		pricedict[current]['percent'] = cpercent
		pricedict[current][buysell] = price
		#print(goldtype)
		#print(pricedict)

	print(pricedict)
	return pricedict


CheckGold()