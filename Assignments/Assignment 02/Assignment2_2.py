#Write a program which accept one number and display below pattern. 

def pattern(Num):
	print("Using For Loop:")
	for i in range(Num):
		print(" ")
		for j in range(Num):
			print("*",end=" ")

def main():
	No1=0
	print("Enter Number to display pattern:")
	No1=int(input())
	pattern(No1)

if __name__=="__main__":
	main()
