#Write a program which accept number from user and 
#print that number of "*" on screen.

def Star(val):
	for i in range(val):
		print("*",end="    ")

def main():
	num=0
	print("Enter Number to print Star:")
	num=int(input())
	Star(num)

if __name__=="__main__":
	main()