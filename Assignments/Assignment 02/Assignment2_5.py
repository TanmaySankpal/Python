#Write a program which accept one number for user and check whether number is prime or not

def Prime(Num):
	for i in range(2,Num):
		if(Num%i==0):
			return 1
		else:
			return 0
def main():
	no=0
	print("Enter Number to check it is prime or not:")
	no=int(input())

	ret=Prime(no)

	if(ret==1):
		print("Given Number Is Not Prime")
	else:
		print("Given Number is Prime")

if __name__=="__main__":
	main()