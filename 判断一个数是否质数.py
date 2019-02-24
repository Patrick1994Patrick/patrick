def is_prime():
	n = int(input('Input a number: '))
	for i in range(2, int(n**0.5)+1):
		if n%i == 0:
			print('%s is not a prime' %n)
			break
		else:
			print('%s is a prime' %n)

if __name__ == '__main__':			
	is_prime()