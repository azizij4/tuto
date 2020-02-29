	#lets us open our file 
#f = open("courses.txt",'r')
	#now we read our file 
#file_items1 = f.read()

#print(file_items1)

#f.close()





	#now we read our file in line
#f = open("courses.txt",'r')

#file_items2 = f.readlines()

#print(file_items2)

#f.close()




	#now we read our file first line
#f = open("courses.txt",'r')

#file_items3 = f.readline()

#print(file_items3)

#f.close()




	#now let append some data in our file 

#f = open('courses.txt','a')

#f.append("11.Electronics Engineering")

#f.close()




	#lets open and close our file in other way
#f = open("courses.txt", 'r')

#try:
#	file_items = f.read()
#	print(file_items)

#finally:
#	f.close()





	#another way is by using with statement
#with open('courses.txt','r') as f:
#	courses = f.read()
#	print(courses)

#	pass




	#lets create another file
	#in python write method check and overide and write to a file if exit but if file not exit creates it 
#with open('courses.txt', 'w') as f:
#	courses = f.read()

#	print(courses)






	#lets append some data in our file

#with open('courses.txt', 'a') as f:
#	courses = f.write('\n Astronomy and black hole')

#	print(courses)	





	

	#lets read our file in this way
#f = open("courses.txt",'r')

#try:

#	for line in f:

#		print(line,end='')


#finally:

#		f.close()



	#lets copy an inter file contents into another file first way to do that is by
#f = open("courses.txt",'r')

#try:
#	f_c = open('courses2.txt','w')

#	try:

#		for courses in f:

#			f_c.write(courses)

#	finally:
#			f_c.close()		


#finally:

#		f.close()








	#lets copy an inter file contents into another file second way to do that is by
#with open('courses.txt','r') as f:

#	with open('courses1','w') as f_c:

#		for courses in f:

#			f_c.write(courses)







	#lets copy an image file two times
#with open('Koala.jpg','rb') as f:

#	with open('Koala2.jpg','wb') as f_c:

#		for courses in f:

#			f_c.write(courses)






	#lets copy an image file two times in other way using while loop
#f = open('Koala.jpg', 'rb')

#try:
#	f_c = open('Koala4.jpg','wb')

#	try:

#		size = 12234

#		Koala4 = f.read(size)

#		while len(Koala4) > 0:

#			f_c.write(Koala4)

#			Koala4 = f.read(size)

			
#	finally:
#			f_c.close()

#finally:
#		f.close()					


		#lets copy an image file two times in other way using while loop
with open('Koala.jpg','rb') as f:

	with open('kaola5.jpg','wb') as f_c:

		file_size = 574657

		kaola5 = f.read(file_size)

		while len(kaola5) >0:

			f_c.write(kaola5)
			
			kaola5 = f.read(file_size)











