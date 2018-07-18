# 04 Divisors
# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

def divisors():
	user_num = int(input("Give me a number, and I'll print the divisors: "))

	divisors = range(1,user_num + 1)

	for x in divisors:
		print(x)

	for x in divisors:
		if (user_num % x) == 0:
			print(x)

def main():
	divisors()

if __name__ == '__main__':
	main()