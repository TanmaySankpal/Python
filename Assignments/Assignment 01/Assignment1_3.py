#Write a program which contains one function named as Add() 
#which accepts two numbers from user and return addition of that two numbers.
def Add(val1,val2):
	sum=0
	sum=val1+val2
	return sum
	
def main():
	no1=0
	no2=0
	ret=0
	print("Enter First Number:")
	no1=int(input())
	print("Enter Second Number:")
	no2=int(input())
	ret=Add(no1,no2)
	print("Addition of given numbers is:->",ret)

if __name__=="__main__":
	main()
