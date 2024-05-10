import sys
from settings import Settings
import pygame

class AlienInvasion:

	def __init__(self):

		pygame.init()
		self.settings = Settings()

		self.screen = pygame.dispaly.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.dispaly.set_caption("Alien Invasion")

	def run_game(self):

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				#color bg
				self.screen.fill(self.settings.bg_color)

			pygame.display.flip()


if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()