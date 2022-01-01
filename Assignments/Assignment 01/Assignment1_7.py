#Write a program which contains one function that accept one number from user and 
#returns true if number is divisible by 5 otherwise return false.

def Chk_Divisible(num):
	if(num%5==0):
		return True 
	else:
		return False 

def main():
	value=0
	print("Enter Number to check it is divisible by 5 or not:")
	value=int(input())
	chk=Chk_Divisible(value)
	print(chk)

if __name__=="__main__":
	main()