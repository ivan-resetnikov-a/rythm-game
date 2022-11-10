import pygame as pg



DT = 1

class Note :
	def __init__ (self, pos, vel, frame) :
		self.frame = frame
		##################
		self.pos = pos
		self.vel = vel
		##################
		self.kill = 0


	def update (self, pressed) :
		# move note down
		self.pos[1] += self.vel

		if pressed[0] and self.pos[0] == 0 and self.pos[1] > 375 and self.pos[1] < 475 :
			self.kill = 1
		if pressed[1] and self.pos[0] == 1 and self.pos[1] > 375 and self.pos[1] < 475 :
			self.kill = 1
		if pressed[2] and self.pos[0] == 2 and self.pos[1] > 375 and self.pos[1] < 475 :
			self.kill = 1
		if pressed[3] and self.pos[0] == 3 and self.pos[1] > 375 and self.pos[1] < 475 :
			self.kill = 1



	def draw (self, pressed) :
		self.update(pressed)
		pg.draw.circle(
			self.frame,
			(220, 220, 220),
			(50+self.pos[0]*100, self.pos[1]),
			25)