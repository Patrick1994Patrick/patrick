import requests
from bs4 import BeautifulSoup
import openpyxl

class maoyan:
	def __init__(self):
		self.url ='https://maoyan.com/films'
		self.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
		
	def get_response(self):	
		res = requests.get(url = self.url, headers = self.headers).text		
		soup = BeautifulSoup(res,'lxml')
		return soup
		
	def get_data(self, soup):
		wb = openpyxl.Workbook()
		ws = wb.active		
		header = ['电影名', '详情页', '详情', '详情2']
		ws.append(header)
		
		tem = soup.find_all('dd')
			
		for each in tem:

			name = each.find('div',attrs = {'class':"channel-detail movie-item-title"})
			each_name = name.get('title') #电影名
		
			html = 'https://maoyan.com'+name.a.get('href') #电影详情页

			res2 = requests.get(url = html, headers = self.headers).text 
				
			soup = BeautifulSoup(res2, 'lxml')
				
			#tem1 = soup.find_all('li', attrs = {'class':"ellipsis"})
			tem2 = soup.find('li', attrs = {'class':"ellipsis"}).string.strip()
			
			tem3 = soup.find('li', attrs = {'class':"ellipsis"}).next_sibling.next_sibling
		
			for em in tem3:
				tem4 = em.string.replace(' ', '').strip()
				
				list = [each_name, html, tem2, tem4]

				ws.append(list)
		
		wb.save('C:\\Users\\Marvin\\Desktop\\python\\maoyan.xlsx')

	def run(self):
		self.get_data(self.get_response())
			
		

a = maoyan()
a.run()	
			
			

	