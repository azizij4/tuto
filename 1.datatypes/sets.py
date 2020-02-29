#working with sets 
#create a sets list
my_sets = {'python','javascript','Rust','C++','c#','java','Swift','GO','ruby'}
print(my_sets)
#let loop our set
for sets in my_sets:

	print(sets)

	for language in sets:


		language = str(input("what is your favorate programming language\n"))

		if language!=sets:


			print("your choice seems like not found ")

		else:
			
			print("your favorate language is ",language)
