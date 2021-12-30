#Write a program which contains one function named as ChkNum() 
#which accept one parameter as number. 
#If number is even then it should display "Even number" otherwise display "Odd number" on console.

def ChkNum(val):
	if(val%2==0):
		print("Number Is Even")
	else:
		print("Number Is Odd")

def main():
	no=0
	ret=0
	print("Enter Number For Checking Either Even Or Odd:")
	no=int(input())
	ret=ChkNum(no)

if __name__=="__main__":
	main()
