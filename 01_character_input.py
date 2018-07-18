# Character Input
# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

def charinput():
	name = input("Please enter your name: ")
	print("Thank you, " + name)
	age = input("Please enter your age: ")
	print("Ok got it. " + name + ", age " + age)

def main():
	charinput()

if __name__ == "__main__":
    main()
