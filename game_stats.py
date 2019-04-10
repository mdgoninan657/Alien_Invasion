# A class to track game stats

class GameStats():
	"""Track statistics for Alien Invasion."""
	
	def __init__(self, ai_settings):
		"""Initialize statistics."""
		self.ai_settings = ai_settings
		self.reset_stats()
		#Start Alien Invasion in an active state
		
		#Start game in an inactive state.
		self.game_active = False
		
		#high schore should never be reset
		self.high_score = self.get_high_score()
		
	
	def get_high_score(self):
		#Read high score in from 'highscore.txt'
		with open('highscore.txt') as file_object:
			int_list = [int(x) for x in file_object]
			return int_list[0]
				
	def set_high_score(self):
		#Create file to store High Score
			#filename = 'highscore.txt'
		with open('highscore.txt', 'w') as file_object:
			file_object.write(str(self.high_score))
			print("New high score recorded: " + str(self.high_score))
			
	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
		
		
	
		
		

