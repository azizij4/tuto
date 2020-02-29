#our class player game overoll
class player:
	def __init__(self, scores, busted, level):
		self.scores = scores
		self.busted = busted
		self.level = level

	def game_overview(self):
		return 'game overview '+'{} {} {}'.format(self.scores, self.busted, self.level)
#class object
player_1 = player(50, 2, 9)
player_2 = player(40, 4, 6)
player_3 = player(20, 6, 3)


print("\t\t \n\n player scores , busteds , levels\n\n")

print('1.player_1',player_2.game_overview(),'\n')
print('2.player_2',player_2.game_overview(),'\n')
print('3.player_3',player_2.game_overview(),'\n')

#our player name class
class player_name:
	def __init__(self, first, last):
		self.first = first
		self.last = last
		self.fullname = first +'-'+ last

	def full_name(self):
		return '{} {}'.format(self.first, self.last)
#class object
player_1 = player_name('Azizi', 'Jumanne')
player_2 = player_name('Jumanne', 'Mfinanga')
player_3 = player_name('Yusuph' , 'Hatibu')

print("\t\t \n\n player Names\n\n")

print('1.player_1 : fullname =',player_1.full_name(),'\n')
print('2.player_2 : fullname =',player_2.full_name(),'\n')
print('3.player_3 : fullname =',player_3.full_name(),'\n')		
