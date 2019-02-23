import requests
#import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import openpyxl

class jb:
	def __init__(self, url):
		self.url = url
		
	def openurl(self):
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.'}
		
		re = requests.get(url = self.url, headers = headers)
		re.encoding = 'utf-8'
		#re = urllib.request.Request(url = self.url, headers = headers)
		#re = urllib.request.urlopen(re)'''
		
		time.sleep(2)
		
		soup = BeautifulSoup(re.text, 'lxml')
		
		temps2 = soup.find_all('div', class_= "p-img")
		
		header = ['商品名', '图片', '地址']
		
		wb = openpyxl.Workbook()
		ws = wb.active
		ws.append(header)
		
		for i in temps2:
			s1 = i.a.attrs['href']
			s2 = i.a.attrs['title']
			s3 = i.img.get('source-data-lazy-img')
			L = [s2, s1, s3]
			ws.append(L)
			'''print(s2)
			print(s1)
			print(s3)
			print('----------------')'''
		wb.save('jingdong.xlsx')	

				
		print('OK')	
				
			


	
	url = input('输入网址： ')
	t = jb(str(url))
	t.openurl()