#Write a program which accept number from user and return number of digits in that number

def ChkCount(No):
	print("Total Digit Count is:",len(str(No)))

def main():
	Value=0
	print("Enter Number to check its digit count:")
	Value=input()
	ChkCount(Value)

if __name__=="__main__":
	main()