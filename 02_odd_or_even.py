# Odd or Even
# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

def oddoreven():
	user_num = input("Pick any number, I'll tell you what it is: ")
	if (int(user_num) % 2 == 1):
		print("Your number " + user_num + " is odd.")
	else:
		print("Your number " + user_num + " is even.")


def main():
	oddoreven()

if __name__ == '__main__':
	main()