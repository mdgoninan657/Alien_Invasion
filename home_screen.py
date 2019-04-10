import pygame.font

class HomeScreen():
	
	def __init__(self,ai_settings,screen,msg):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.welcome = "Welcome to Alien Invasion"
		self.ai_settings = ai_settings
		
	#Set Dimensions and properties of the button.
		self.width = 200
		self.height = 15
		self.text_color = (0,255,0)
		self.font = pygame.font.SysFont(None, 48)
		
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		
		self.prep_home(msg)
		
	def prep_home(self,msg):
		self.home_image = self.font.render(msg,True,
			self.text_color,self.ai_settings.bg_color)
		#Position Home Screen text
		self.home_image_rect = self.home_image.get_rect()
		self.home_image_rect.center = self.screen_rect.center
		self.home_image_rect.top = self.screen_rect.top + 20
		
	def draw_home_screen(self):
		#Draw blank button and then draw messsage.
		self.screen.blit(self.home_image, self.home_image_rect)
		
