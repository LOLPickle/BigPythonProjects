import sys
from settings import Settings
from ship import Ship
import pygame

class AlienInvasion:

	def __init__(self):

		pygame.init()
		self.settings = Settings()

		self.screen = pygame.dispaly.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.dispaly.set_caption("Alien Invasion")

		self.ship = Ship(self)

	def run_game(self):

		while True:
			self._check_events()
			self._update_events()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						self.ship.rect.x += 1

				#color bg
				self.screen.fill(self.settings.bg_color)
				self.ship.blitme()

			pygame.display.flip()


if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()