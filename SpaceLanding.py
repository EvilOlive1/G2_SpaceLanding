import pygame
from sys import exit

# Initializing
pygame.init()

# Creating the window
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Space Landingd")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	# Draw all the elements
	# Update everything
	pygame.display.update()