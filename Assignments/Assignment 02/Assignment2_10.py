#Write a program which accept number from user and return addition of digits in that number. 

def DigAdd(value):
	sum=0
	for i in range(len(value)):
		sum=sum+int(value[i])
	return sum
	
def main():
	no=0
	ret=0
	print("Enter Number and Addition of digits:")
	no=input()
	ret=DigAdd(no)
	print("Addition of its digit is:",ret)

if __name__=="__main__":
	main()