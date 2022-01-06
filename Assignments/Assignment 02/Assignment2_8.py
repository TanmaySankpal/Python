# Write a program which accept one number and display below pattern. 

def Pattern(No):
	for i in range(1,No+1):
		print(" ")
		for j in range(1,No+1):
			if(i>=j):	
				print(j,end=" ")
				print(" ",end=" ")
def main():
	Num=0;
	print("Enter any number to display pattern:")
	Num=int(input())
	Pattern(Num)

if __name__=="__main__":
	main()