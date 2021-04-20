# bitkubprice.py
import requests
from pprint import pprint
import time
# pip install requests

API_URL = 'https://api.bitkub.com' #base url

endpoint = {
	'status':'/api/status',
	'timestamp':'/api/servertime',
	'symbols':'/api/market/symbols',
	'ticker':'/api/market/ticker'
}

def Status():
	#pprint(r.json())
	url = API_URL + endpoint['status']
	r = requests.get(url)
	if r.status_code == 200:
		print('เซิร์ฟเวอร์ทำงานปกติ')
		print(r.status_code)
	return r.status_code

def ServerTime():
	url = API_URL + endpoint['timestamp']
	comtime = time.time()
	print('Com:',comtime)
	print(time.ctime(comtime))
	#print(time.localtime(comtime))

	r = requests.get(url)
	data = r.json()

	print('Server:',data)
	print(time.ctime(data))


def Allsymbol():
	url = API_URL + endpoint['symbols']
	r = requests.get(url)
	data = r.json()
	# pprint(r.json())
	count = len(data['result'])
	print('COUNT:',count)
	print(data['result'])


def Ticker(COIN='THB_BTC'):
	url = API_URL + endpoint['ticker']
	r = requests.get(url,params={'sym':COIN})
	data = r.json()
	print(data)
	print('----------')
	print('ราคาล่าสุด',data[COIN]['last'])
	print('เปลี่ยนแปลง: ',data[COIN]['percentChange'])

Ticker('THB_DOGE')
#Allsymbol()
	





