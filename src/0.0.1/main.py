from core.core import *


class Game :
	def __init__ (self, size, title, fps) :
		#################################
		self.screen = pygame.display.set_mode(size)
		pygame.display.set_caption(title)
		#################################
		self.clock = pygame.time.Clock()
		self.frame = pygame.Surface(size)
		self.FPS = fps


	def update (self) : pass


	def render (self) :
		self.frame.fill((0, 0, 0))
		########################
		for note in self.notes : note.draw()
		########################
		self.screen.blit(self.frame, (0, 0))
		self.clock.tick(self.FPS)
		pygame.display.flip()


	def start (self) :
		self.notes = []
		###################
		self.running = True
		while self.running :
			for event in pygame.event.get() :
				if event.type == pygame.QUIT :
					self.running = False
			self.update()
			self.render()


if __name__ == "__main__":
	# game
	game = Game((500, 500), "Game", 60)
	game.start()
