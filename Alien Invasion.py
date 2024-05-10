import sys

import pygame

class AlienInvasion:



	def __init__(self):

		pygame.init()


		self.screen = pygame.dispaly.set_mode((1200, 800))
		pygame.dispaly.set_caption("Alien Invasion")

		#color bg
		self.bg_color = (280, 230, 230)

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