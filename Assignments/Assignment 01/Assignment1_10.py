#Write a program which accept name from user and display length of its name. 

def Display(nm):
	print(len(nm))

def main():
	print("Enter name to check its length:")
	name=input()
	Display(name)
    
if __name__=="__main__":
	main()
