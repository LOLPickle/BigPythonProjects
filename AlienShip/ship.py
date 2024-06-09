import pygame

class Ship:
	#class ship
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		#image/sprite
		self.image = pygame.image.load('ship.bmp')
		self.rect = self.image.get_rect()

		self.rect.midbottom = self.screen_rect.midbottom

		self.moving_right = False

	def update(self):


		if self.moving_right:
			self.rect.x += 1

	def blitme(self):
		#position
		self.screen.blit(self.image, self.rect)