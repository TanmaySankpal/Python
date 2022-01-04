# Write a program which accept one number and display below pattern. 

def Display(Num):
	for i in range(Num):
		print(" ")
		for j in range(Num):
			if(i<=j):
				print("*",end=" ")
				print(" ",end=" ")
def main():
	no=0
	print("Enter Number For display pattern:")
	no=int(input())
	Display(no)

if __name__=="__main__":
	main()