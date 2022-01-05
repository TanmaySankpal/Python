#Write a program which accept one number and display below pattern. 

def Display(val):
	for i in range(1,val+1):
		print(" ")
		for j in range(1,val+1):
			print(j,end=" ")
			print(" ",end=" ")

def main():
	no=0
	print("Enter Number to display pattern:")
	no=int(input())
	Display(no)

if __name__=="__main__":
	main()


	
