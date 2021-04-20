# convertpdf.py
# pip install pdf2image
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

def ConvertPDF(filepath='TEST1.pdf',page=0,loc=(0,0,500,500),lang='tha',save=False,rotate=False):
	#transposed  = colorImage.transpose(Image.ROTATE_90)
	image = convert_from_path(filepath)
	if rotate == True:
		image[page] = image[page].transpose(Image.ROTATE_90)
		#imgrotate.save('rotate.jpg')

	filename = filepath[:-4]
	img = image[page]
	if save == True:
		savename = '{}-{}.jpg'.format(filename,page+1)
		img.save(savename)

	location = loc #(132,487,582,645)
	product = img.crop(location)
	#product.show()
	#product.save('testcrop.jpg')
	result = pytesseract.image_to_string(product,lang=lang)
	result = result.replace('\n',' ').replace('\x0c','')
	return result

text = ConvertPDF('TEST1.pdf',page=0,loc=(322,1846,779,1884))
print(text)