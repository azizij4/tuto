#let start with for loop
#let create a list
my_chain = ['azizi','jumanne','yusuph','Mramba','Hulila','mwishwaa']

#now let loop our list
for chain in my_chain:
	if chain == 'jumanne':
		print('jumanne is your father')
		continue
	elif chain == "hey":
		print("hey")
		break		
	print(chain)

	#now lets look about while loop
azizi = 0	
while azizi < 20:
	azizi += 1
	print(azizi)
	continue
	
