#Create on module named as Arithmetic which contains 4 functions 
#as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. 
#All functions accepts two parameters as number and perform the operation.
#Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.

import Arithmatic

def main():
	Num1=0
	Num2=0
	Ret=0

	print("Enter First Number For Operation:")
	Num1=int(input())
	print("Enter Second Number For Operation:")
	Num2=int(input())
	print("Which Operation you want to perform: For Add 1:For Sub 2:For Mult 3:For Div 4")
	Oprt=int(input())

	if(Oprt==1):
		Ret=Arithmatic.Add(Num1,Num2)
		print("Addition is:",Ret)
	elif(Oprt==2):
		Ret=Arithmatic.Sub(Num1,Num2)
		print("Substraction is:",Ret)
	elif(Oprt==3):
		Ret=Arithmatic.Mult(Num1,Num2)
		print("Multiplication is:",Ret)
	else:
		Ret=Arithmatic.Div(Num1,Num2)
		print("Division is:",Ret)

if __name__=="__main__":
	main()