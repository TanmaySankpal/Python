#Write a program which accept one number from user and return its factorial. 

def Factorial(val):
	print("Using For Loop:")
	fact=1
	for i in range(1,val+1):
		fact=fact*i
	return fact

def main():
	No=0
	Ret=0
	print("Enter Number Positive Number:")
	No=int(input())
	Ret=Factorial(No)
	print("Factorial Of Given Number is:",Ret)

if __name__=="__main__":
	main()