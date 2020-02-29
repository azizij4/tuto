#let create a function to calculate
#let craete global variable
#function for Additin
result = 0
def Addition(a,b):
	global result
	result = a + b

	return result

#function for Substruction
def Substraction(a,b):
	global result
	result = a - b

	return result

#function for Multiplication
def Multiplication(a,b):
	global result
	result = a * b

	return result

#function for Division
def Division(a,b):
	global result
	result = a % b
	
	return result
#let create user input
def calculator():
	uservalid =['YES','YEC','Y','y','Yes','Yec','yes','yec','ya','YA'
	            'yc','YC','Yc','Yah','Yeah','yap','YAP','Yap']
	#User input
	a = int(input("Enter first number..."))
	b = int(input("Enter second number..."))
	print("""
	Select which operation you want
	1. Addition
	2. Subtraction
	3. Multiplication
	4. Division
	""")
	selection = int(input("Enter your selection...."))
	if selection == 1:
		Addition(a,b)
		print("Addition of two number your entered =",Addition(a,b))
	elif selection == 2:
		Substraction(a,b)
		print("Substraction of two number your entered =",Substraction(a,b))
	elif selection == 3:
		Multiplication(a,b)
		print("Multiplication of two number your entered =",Multiplication(a,b))
	elif selection == 4:
		Division(a,b)
		print("Division of two number your entered =",Division(a,b))
	else:
		print("You select invalid selection ")
	restart = str(input("Do you want to restart a calculator? \n"))
	if  restart in  uservalid:
		calculator()
	else:
		print('you exit!!!!')
		exit()	
	
calculator()





