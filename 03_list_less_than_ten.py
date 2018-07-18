#  List less than ten
# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

def lowelements():
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

	for i in range(len(a)):
		if a[i] < 5:
			print(a[i])

def main():
	lowelements()

if __name__ == '__main__':
	main()

