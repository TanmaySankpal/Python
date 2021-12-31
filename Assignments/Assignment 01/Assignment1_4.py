#Write a program which display 5 times Marvellous on screen. 

def Marvellous():
	i=0
	print("Using While Loop:")
	while(i<5):
		print("Marvellous")
		i=i+1

	print("------------------------------------")
	print("Using For Loop:")

	for i in range(5):
		print("Marvellous")

def main():
	Marvellous()

if __name__=="__main__":
	main()