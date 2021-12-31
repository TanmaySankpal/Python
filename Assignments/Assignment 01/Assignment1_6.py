#Write a program which accept number from user and 
#check whether that number is positive or negative or zero.

def ChkNo(val):
	if(val>0):
		print("Given Number is positive..")
	elif(val<0):
		print("Given Number is negative..")
	else:
		print("Given Number is Zero..")

def main():
	no=0
	print("Enter To check it is positive, negative or zero :")
	no=int(input())
	ChkNo(no)

if __name__=="__main__":
	main()