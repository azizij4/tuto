#working with booleans and and conditions in python
#azizi = False
#if not azizi:
#	print('azizi')
#else:
#	print('jack')
username = 'azizi'
email = 'azizijumanne@gmail.com'
password = "azizi2000###"


username=str(input("enter username\n"))
email =str(input('enter email\n'))
password=str(input('enter password\n'))
confirm_password=str(input('confirm password\n'))


if password =='azizi2000###' and email =='azizijumanne@gmail.com' and username == 'azizi' and confirm_password == password:

	print('successfull logged in\n\n\n')

	print('now enter admin credentials below')

	username = 'azizi'
	email = 'azizijumanne@gmail.com'
	password = "azizi2000###"

	username=str(input("enter username\n"))
	email =str(input('enter email\n'))
	password=str(input('enter password\n'))
	confirm_password=str(input('confirm password\n'))

	if password =='azizi2000###' and email =='azizijumanne@gmail.com' and username == 'azizi' and confirm_password == password:

		print('successfull logged in\n\n\n')

	else:
		print('successfull logged in\n\n\n')


else:

	print('try again wrong credentials')	
