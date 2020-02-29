#
class NIDA:
	total_register = 0
	NIDA_Registered = 0
	def __init__(self, f_name, m_name, lname, date, month, year, phone, region, district, ward, house_no):
		self.f_name = f_name
		self.m_name = m_name
		self.lname = lname
		self.date = date
		self.month = month
		self.year = year
		self.phone = phone
		self.region = region
		self.district = district
		self.ward = ward
		self.house_no = house_no

		NIDA.total_register += 1
		NIDA.NIDA_Registered += 1	

	def fullname(self):
		return '{} - {} - {}'.format(self.f_name ,self.m_name, self.lname)

	def birthday(self):
		return '{} - {} - {}'.format(self.date ,self.month, self.year)
	def citizen_place(self):
		return '{} - {} - {}'.format(self.region, self.district, self.ward)
	def phone_house(self):
		return '{} - {}'.format(self.house_no, self.phone)

citizen1 = NIDA('azizi','jumanne','mfinanga',1 ,9 ,2000 ,692946575, "kilimanjaro", 'moshi v','kilema', 0)
citizen2 = NIDA('Ali','rajabu','msuya',23 ,1 ,1954 ,6976546575, "Njombe", 'njombe mjini','mjini', 0)
citizen3 = NIDA('salimu','hamadi','khasimu',4 ,7 ,1987 ,784946575, "Dar salam", 'kinondoni','posta', 0)
citizen4 = NIDA('Zainabu','ashimu','kibatu',12 ,3 ,1992 ,692967375, "kigoma", 'kasulu','ujiji', 0)
citizen5 = NIDA('Benjamin','Alfredi','kisangu',31 ,1 ,1974 ,692946673, "morogoro", 'kilosa','ifakara', 0)
#print('total number of NIDA Registered',NIDA.NIDA_Registered)
#all_citizen =[citizen1.__repr__(), citizen2.__repr__(), citizen3.__repr__(), citizen4.__repr__(), citizen5.__repr__()]
#citizen1.birthday()
#citizen3.fullname()
#citizen3.citizen_place()
#citizen3.phone_house()	
#for citizen in all_citizen:
#	print(citizen) 	
#print('\n\n',citizen3.birthday(),'|',citizen3.fullname(),'|',citizen3.citizen_place(),'|',citizen3.phone_house(),'\n\n')
#print('total number of citizen Registered',NIDA.Registered)
class KURA(NIDA):
	KURA_registered = 0
	def __init__(self,f_name, m_name, lname, date, month, year, phone, region, district, ward,house_no, election):
		super().__init__(f_name, m_name, lname, date, month, year, phone, region, district, ward, house_no)
		self.election = election

		KURA.KURA_registered += 1

citizenk1 = KURA('rashidi','jumanne','mfinanga',1 ,9 ,2000 ,692946575, "kilimanjaro", 'moshi v','kilema', 0, 'kilototoni')
citizenk2 = KURA('mohamed','rajabu','msuya',23 ,1 ,1954 ,6976546575, "Njombe", 'njombe mjini','mjini', 0,'kilototoni')
citizenk3 = KURA('hatibu','hamadi','khasimu',4 ,7 ,1987 ,784946575, "Dar salam", 'kinondoni','posta', 0,'kilototoni')
citizenk4 = KURA('ramadhan','ashimu','kibatu',12 ,3 ,1992 ,692967375, "kigoma", 'kasulu','ujiji', 0,'kilototoni')
citizenk5 = KURA('hamidu','Alfredi','kisangu',31 ,1 ,1974 ,692946673, "morogoro", 'kilosa','ifakara', 0,'kilototoni')
citizenk6 = KURA('hamidu','Alfredi','kisangu',31 ,1 ,1974 ,692946673, "morogoro", 'kilosa','ifakara', 0,'kilototoni')

	
print('total number of KURA Registered',KURA.KURA_registered)


class VYAKUZALIWA(NIDA):
	VYAKUZALIWA_registered = 0
	def __init__(self,f_name, m_name, lname, date, month, year, phone, region, district, ward,house_no, clinic):
		super().__init__(f_name, m_name, lname, date, month, year, phone, region, district, ward, house_no)
		self.clinic = clinic

		VYAKUZALIWA.VYAKUZALIWA_registered += 1

citizenk1 = VYAKUZALIWA('azizi','jumanne','mfinanga',1 ,9 ,2000 ,692946575, "kilimanjaro", 'moshi v','kilema', 0, 'minja')
citizenk2 = VYAKUZALIWA('Ali','rajabu','msuya',23 ,1 ,1954 ,6976546575, "Njombe", 'njombe mjini','mjini', 0,'njombe hospital')
citizenk3 = VYAKUZALIWA('salimu','hamadi','khasimu',4 ,7 ,1987 ,784946575, "Dar salam", 'kinondoni','posta', 0,'muimbili')
citizenk4 = VYAKUZALIWA('Zainabu','ashimu','kibatu',12 ,3 ,1992 ,692967375, "kigoma", 'kasulu','ujiji', 0,'kigoma hospital')
citizenk5 = VYAKUZALIWA('Benjamin','Alfredi','kisangu',31 ,1 ,1974 ,692946673, "morogoro", 'kilosa','ifakara', 0,'moro hospital')
	
print('total number of VYAKUZALIWA Registered',VYAKUZALIWA.VYAKUZALIWA_registered)


class VYAMKAZI(NIDA):
	VYAMKAZI_registered = 0
	def __init__(self, f_name, m_name, lname, date, month, year, phone, region, district, ward, house_no, ID ):
		super().__init__(f_name, m_name, lname, date, month, year, phone, region, district, ward, house_no)
		self.ID = ID

		VYAMKAZI.VYAMKAZI_registered += 1

citizenk1 = VYAMKAZI('azizi','jumanne','mfinanga',1 ,9 ,2000 ,692946575, "kilimanjaro", 'moshi v','kilema', 0,765433098)
citizenk2 = VYAMKAZI('Ali','rajabu','msuya',23 ,1 ,1954 ,6976546575, "Njombe", 'njombe mjini','mjini', 0,654323987)
citizenk3 = VYAMKAZI('salimu','hamadi','khasimu',4 ,7 ,1987 ,784946575, "Dar salam", 'kinondoni','posta', 0,985634542)
citizenk4 = VYAMKAZI('Zainabu','ashimu','kibatu',12 ,3 ,1992 ,692967375, "kigoma", 'kasulu','ujiji', 0,6745343786543)
citizenk5 = VYAMKAZI('Benjamin','Alfredi','kisangu',31 ,1 ,1974 ,692946673, "morogoro", 'kilosa','ifakara', 0,546734234654)
	
print('total number of VYAMKAZI Registered',VYAMKAZI.VYAMKAZI_registered)

print('total number of citizen Registered',NIDA.total_register)
print("_______________________________________________________________________________________________")
print("birthday      |",'\tmajina matatu            |','\tmakazi                        |' 'namba za simu')
print("_______________________________________________________________________________________________")
print(citizenk3.birthday(),' |',citizenk3.fullname(),'   |',citizenk3.citizen_place(),' |',citizenk3.phone_house())

print(citizenk2.birthday(),'|',citizenk2.fullname(),'        |',citizenk2.citizen_place(),' |',citizenk2.phone_house())

print(citizenk1.birthday(),' |',citizenk1.fullname(),'  |',citizenk1.citizen_place(),'|',citizenk1.phone_house())

print(citizenk3.birthday(),' |',citizenk3.fullname(),'   |',citizenk3.citizen_place(),' |',citizenk3.phone_house())

print(citizenk2.birthday(),'|',citizenk2.fullname(),'        |',citizenk2.citizen_place(),' |',citizenk2.phone_house())

print(citizenk1.birthday(),' |',citizenk1.fullname(),'  |',citizenk1.citizen_place(),'|',citizenk1.phone_house())

print(citizenk3.birthday(),' |',citizenk3.fullname(),'   |',citizenk3.citizen_place(),' |',citizenk3.phone_house())

print(citizenk2.birthday(),'|',citizenk2.fullname(),'        |',citizenk2.citizen_place(),' |',citizenk2.phone_house())

print(citizenk1.birthday(),' |',citizenk1.fullname(),'  |',citizenk1.citizen_place(),'|',citizenk1.phone_house())

print(citizenk3.birthday(),' |',citizenk3.fullname(),'   |',citizenk3.citizen_place(),' |',citizenk3.phone_house())

print(citizenk2.birthday(),'|',citizenk2.fullname(),'        |',citizenk2.citizen_place(),' |',citizenk2.phone_house())

print(citizenk1.birthday(),' |',citizenk1.fullname(),'  |',citizenk1.citizen_place(),'|',citizenk1.phone_house())

print(citizenk3.birthday(),' |',citizenk3.fullname(),'   |',citizenk3.citizen_place(),' |',citizenk3.phone_house())

print(citizenk2.birthday(),'|',citizenk2.fullname(),'        |',citizenk2.citizen_place(),' |',citizenk2.phone_house())

print(citizenk1.birthday(),' |',citizenk1.fullname(),'  |',citizenk1.citizen_place(),'|',citizenk1.phone_house())

print(citizenk3.birthday(),' |',citizenk3.fullname(),'   |',citizenk3.citizen_place(),' |',citizenk3.phone_house())

print(citizenk2.birthday(),'|',citizenk2.fullname(),'        |',citizenk2.citizen_place(),' |',citizenk2.phone_house())

print(citizenk1.birthday(),' |',citizenk1.fullname(),'  |',citizenk1.citizen_place(),'|',citizenk1.phone_house())

print(citizenk3.birthday(),' |',citizenk3.fullname(),'   |',citizenk3.citizen_place(),' |',citizenk3.phone_house())

print(citizenk2.birthday(),'|',citizenk2.fullname(),'        |',citizenk2.citizen_place(),' |',citizenk2.phone_house())

print("_______________________________________________________________________________________________")