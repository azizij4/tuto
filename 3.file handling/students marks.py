#in this project we are going to work with text file and make some calculation to file
with open('students.txt','r') as student:

	student_list = student.readlines()

	for lists in student_list:

		new_list = lists.split('-')

		#print(new_list)

		names = new_list[0]

		physics = new_list[1]

		chemisty = new_list[2]

		Computer = new_list[3]

		Maths = new_list[4]

		print(names +'='+ physics +'-'+ chemisty +'-'+ Computer +'-'+ Maths)

		
	
