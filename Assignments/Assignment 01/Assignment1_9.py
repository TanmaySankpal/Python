#Write a program which display first 10 even numbers on screen. 

def First_ten_even():
	for i in range(2,21):
		if(i%2==0):
			print(i)

def main():
	First_ten_even()

if __name__=="__main__":
	main()
