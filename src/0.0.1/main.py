import pygame as pg
from core.core import Note
from core.file import get

CONTROLLS = [
	pg.K_d,
	pg.K_f,
	pg.K_j,
	pg.K_k]



class Game :
	def __init__ (self, size, title, fps) :
		#################################
		self.screen = pg.display.set_mode(size)
		pg.display.set_caption(title)
		#################################
		self.clock = pg.time.Clock()
		self.frame = pg.Surface(size)
		self.FPS = fps


	def render (self) :
		self.frame.fill((0, 0, 0))
		########################

		# draw "target" line
		pg.draw.rect(
			self.frame,
			(100, 100, 100),
			(0, 400, 400, 50))

		# draw notes
		for note in self.notes :
			# delete if behind the scene
			if note.pos[1] > 550 : self.notes.remove(note)

			# draw and update
			note.draw(pressed=self.pressed)

			# kill if player pressed on time
			if note.kill : self.notes.remove(note)

		########################
		self.screen.blit(self.frame, (0, 0))
		self.clock.tick(self.FPS)
		pg.display.flip()


	def start (self) :
		# add notes list
		self.pressed = [0, 0, 0, 0]
		self.notes = []
		self.time = 0

		# load song
		self.song = get("songs/test.song")

		###################
		self.running = True
		while self.running :
			self.pressed[0] = 0
			self.pressed[1] = 0
			self.pressed[2] = 0
			self.pressed[3] = 0
			for event in pg.event.get() :
				if event.type == pg.QUIT :
					self.running = False

				# check what keys player pressed
				if event.type == pg.KEYDOWN :
					if event.key == CONTROLLS[0] : self.pressed[0] = 1
					if event.key == CONTROLLS[1] : self.pressed[1] = 1
					if event.key == CONTROLLS[2] : self.pressed[2] = 1
					if event.key == CONTROLLS[3] : self.pressed[3] = 1


			for note in self.song :
				if note[2] == self.time :
					self.notes.append(Note([note[0], -25], note[1], self.frame))
			self.time += 1

			self.render()


if __name__ == "__main__":
	# game
	game = Game((400, 500), "Game", 60)
	game.start()
