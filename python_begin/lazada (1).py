from selenium import webdriver
import time
from bs4 import BeautifulSoup as soup

#url = 'https://www.lazada.co.th/shop-appliances-water-dispensers/?spm=a2o4m.home.cate_3_2.9.4b626f846xIQnw'
#url = 'https://www.lazada.co.th/shop-laptops/?page=2&spm=a2o4m.searchlistcategory.cate_1.3.79f53615LRgEQv'


def LazadaPrice(keyword,page=1):
	
	keyword = keyword.replace(' ','+')
	url = 'https://www.lazada.co.th/catalog/?q={}&_keyori=ss&from=input&spm=a2o4m.searchlistbrand.search.go.24515f5dZiouCp'.format(keyword)


	if page>=2 :
		sp = url.split('/')
		url = '{}//{}/{}/?page={}&{}'.format(sp[0],sp[2],sp[3],page,sp[4][1:])
		

	
	opt = webdriver.ChromeOptions()
	opt.add_argument('headless')

	#driver = webdriver.Chrome(options=opt)
	driver = webdriver.Chrome()
	driver.get(url)

	time.sleep(10)

	page_html = driver.page_source

	driver.close()

	data = soup(page_html,'html.parser')

	product = data.findAll('div',{'class':'c16H9d'})
	price = data.findAll('span',{'class':'c13VH6'})

	res_product = []
	res_url = []
	res_price = []
	#print('https:' +product[0].a['href'])
	for pd in product:
		res_product.append(pd.text)
		res_url.append('https:' + pd.a['href'])

	for pc in price:
		#print(pc)
		pdprice = pc.text
		pdprice = pdprice.replace('฿','')
		pdprice = pdprice.replace(',','')
		res_price.append(float(pdprice))
		# float for decimal point

	print(res_product)
	print(res_url)
	print(res_price)

	return (res_product,res_url,res_price)
	
product = LazadaPrice('ทีวี')

cheap = []
minprice = min(product[2])
for i in range(len(product[0])):
	pos = product[2].index(min(product[2]))
	if min(product[2]) == minprice:
		cheap.append([product[0][pos],product[1][pos],product[2][pos]])
		del product[0][pos]
		del product[1][pos]
		del product[2][pos]

print()
print()
print('-------สินค้าราคาถูกที่สุดคือ---------')
for c in cheap:
	print(f"สินค้า: {c[0]}\n\nราคา: {c[2]} บาท\n\nURL: {c[1]}")