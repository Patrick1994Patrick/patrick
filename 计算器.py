
class calculate:
	def add(self,x,y):
		print(x + y)
	def subtract(self,x,y):
		print(x - y)
	def multiply(self):
		print(x * y)
	def divide(self,x,y):
		print(x/y)
	def run(self):
		x = int(input('第一个数：'))
		m = input('运算符：')
		y = int(input('第二个数：'))
		if m == '+':
			return self.add(x,y)
		elif m == '-':
			return self.subtract(x,y)
		elif m == '*':
			return self.multiply(x,y)
		elif m == '/':
			return self.divide(x,y)
		else:
			print('输入有误')
			return self.run()
			
a = calculate()
a.run()
