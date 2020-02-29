#class variables
class player:
	bonus_scores = 10
	bonus_levels = 3
	total_number_of_player = 0
	def __init__(self, scores, busted, level):
		self.scores = scores
		self.busted = busted
		self.level = level

		player.total_number_of_player += 1	

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


player_1 = player(50,  2,   9)
player_2 = player(40,  4,   6)
player_3 = player(20,  6,   3)
player_4 = player(70,  1,  10)
player_5 = player(85,  1,  23)
player_6 = player(90,  0,  25)
player_7 = player(92,  0,  30)
player_8 = player(100,  0, 35)


class playerlevel_1(player):
	total_number_of_player_level_1 = 0
	def __init__(self, scores, busted, level, level_no):
		super().__init__(scores, busted, level)
		self.level_no = level_no

		playerlevel_1.total_number_of_player_level_1 += 1

player_f1 = playerlevel_1(66,  3,   7,  1)
player_f2 = playerlevel_1(8,   9,   5,  1)
player_f3 = playerlevel_1(2,   6,   3,  1)
player_f4 = playerlevel_1(4,   1,   6,  1)
player_f5 = playerlevel_1(8,   2,   4,  1)


class playerlevel_2(player):
	total_number_of_player_level_2 = 0
	def __init__(self, scores, busted, level, level_no):
		super().__init__(scores, busted, level)
		self.level_no = level_no

		playerlevel_2.total_number_of_player_level_2 += 1

player_s1 = playerlevel_2(66,  3,   7,  2)
player_s2 = playerlevel_2(8,   9,   5,  2)
player_s3 = playerlevel_2(2,   6,   3,  2)




class playerlevel_3(player):
	total_number_of_player_level_3 = 0
	def __init__(self, scores, busted, level, level_no):
		super().__init__(scores, busted, level)
		self.level_no = level_no

		playerlevel_3.total_number_of_player_level_3 += 1


player_t1 = playerlevel_3(66,  3,   7,  3)
player_t2 = playerlevel_3(8,   9,   5,  3)
player_t3 = playerlevel_3(2,   6,   3,  3)
player_t4 = playerlevel_3(4,   1,   6,  3)




class playerlevel_4(player):
	total_number_of_player_level_4 = 0
	def __init__(self, scores, busted, level, level_no):
		super().__init__(scores, busted, level)
		self.level_no = level_no

		playerlevel_4.total_number_of_player_level_4 += 1


player_fo1 = playerlevel_4(66,  3,   7,  4)
player_fo2 = playerlevel_4(8,   9,   5,  4)
player_fo3 = playerlevel_4(2,   6,   3,  4)
player_fo4 = playerlevel_4(4,   1,   6,  4)
player_fo5 = playerlevel_4(8,   2,   4,  4)
player_fo6 = playerlevel_4(3,   0,   5,  4)




class playerlevel_5(player):
	total_number_of_player_level_5 = 0
	def __init__(self, scores, busted, level, level_no):
		super().__init__(scores, busted, level)
		self.level_no = level_no

		playerlevel_5.total_number_of_player_level_5 += 1

player_ff1 = playerlevel_5(66,  3,   7,  5)
player_ff2 = playerlevel_5(8,   9,   5,  5)
player_ff3 = playerlevel_5(2,   6,   3,  5)
player_ff4 = playerlevel_5(4,   1,   6,  5)
player_ff5 = playerlevel_5(8,   2,   4,  5)
player_ff6 = playerlevel_5(3,   0,   5,  5)
player_ff7 = playerlevel_5(6,   5,   3,  5)
player_ff8 = playerlevel_5(7,   4,   6,  5)
player_ff9 = playerlevel_5(7,   4,   6,  5)



#print(player_2.scores)
player_ff4.bonus_score()
player_ff4.bonus_level()
print(player_ff4.bonus_levels)
print('level 1 have ',playerlevel_1.total_number_of_player_level_1,'players')
print('level 2 have ',playerlevel_2.total_number_of_player_level_2,'players')
print('level 3 have ',playerlevel_3.total_number_of_player_level_3,'players')
print('level 4 have ',playerlevel_4.total_number_of_player_level_4,'players')
print('level 5 have ',playerlevel_5.total_number_of_player_level_5,'players')
print('total player ',player.total_number_of_player,'players')


