#Write a program which display 10 to 1 on screen. 

def Display():
	i=10
	print("Using While Loop")
	while(i>0):
		print(i)
		i=i-1

	print("--------------------------------------")

	print("Using For Loop:")
	for i in range(10,0,-1):
		print(i)

def main():
	Display()

if __name__=="__main__":
	main()