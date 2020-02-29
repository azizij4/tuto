#class variables
class player:
	bonus_scores = 5
	bonus_levels = 2
	number_of_player = 0
	def __init__(self, scores, busted, level):
		self.scores = scores
		self.busted = busted
		self.level = level

		player.number_of_player += 1	

	def game_overview(self):
		return 'game overview '+'{} {} {}'.format(self.scores, self.busted, self.level)
	#this method below we use self argument to our class variable bonus_score in 
	#order to change values of every object of our class player
	def bonus_score(self):
		self.scores = int(self.scores + self.bonus_scores)
	#this method below we use class nam.variable class this will update all object at once 
	#thus why we use classname.our variable 
	def bonus_level(self):
		self.level = int(self.level + player.bonus_levels)
			

#class object

player_1 = player(50,  2,   9)
player_2 = player(40,  4,   6)
player_3 = player(20,  6,   3)



print("\t\t \n\n player scores , busteds , levels\n\n")

print('1.player_1',player_1.game_overview(),'\n')
print('2.player_2',player_2.game_overview(),'\n')
print('3.player_3',player_3.game_overview(),'\n')


#print(player_2.scores)
player_2.bonus_score()
player_2.bonus_level()
#print(player_2.level)

print('This game have ',player.number_of_player,'players')


