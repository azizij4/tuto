#local, enclose, global, builtins
#LEGB
#now let us start with local variables 

#oky let make a bitcoinbank system
def intro():
	print("""
			             *

		           *	2020    *

		                 *


		             Happy New Year

		WELCOME TO BITCOIN BANK FOR FASTER AND SECURE CHAIN 

		
		""")
def ask_for_account():
	
	print("""
		1.Press 1 to sign in 
		2.press 2 to create an account 

		""")
	ask =int(input(""))
	while (ask != 1) and (ask != 2):
		print("!! You have to choose to sign in or to create an account")
		ask =(input("choose again\n"))
	if ask == 1:

		print("You are succefull login into your account")
	else:
		print("You are succefull create an account")	

def account():
	print("""
		
		
		""")


def auther():
	pass
intro()
ask_for_account()	


			
	

