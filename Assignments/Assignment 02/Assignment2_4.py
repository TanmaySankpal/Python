#Write a program which accept one number form user and return addition of its factors. 

def Factors(val):
	sum=0
	for i in range(len(val)):
		sum=sum+val[i]
	return sum

def main():
	No=0
	ret=0
	fac=[]

	print("Enter Number for addition of its factors:")
	No=int(input())
	for i in range(1,No):
		if(No%i==0):
			fac.append(i)
	ret=Factors(fac)
	print("Addition Of given Numbers factor is",ret)
    
if __name__=="__main__":
	main()
