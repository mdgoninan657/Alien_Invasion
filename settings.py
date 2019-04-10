class Settings():
	"""A class to store all settings for Alien Invasion"""
	
	def __init__(self):
		"""Initialize the game's static settings."""
		#Screen Settings
		self.screen_width = 1285
		self.screen_height = 800
		self.bg_color =(000,000,000)
		
		#Ship settings
		self.ship_speed_factor = 1.5
		self.ship_limit = 1
		
		#bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 2
		self.bullet_height = 15
		self.bullet_color = 200,000,000
		self.bullets_allowed = 10
		
		#alien settings 
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		#fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1
		
		#How quickly the game speeds up
		self.speedup_scale = 1.3
		
		self.initialize_dynamic_settings()
		
		#How quickly the alien point values increases
		self.score_scale = 1.5
		
		
	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		
		#Fleet Direction of 1 represents right: -1 represents left
		self.fleet_direction = 1
		
		#Scoring
		self.alien_points = 50
		
	def increase_speed(self):
		"""Increase speed settings."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)
		
		
	
		
		
