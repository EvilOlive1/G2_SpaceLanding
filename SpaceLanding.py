import pygame

# Initializing
pygame.init()

# Creating the window
screen = pygame.display.set_mode((800,400))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	# Draw all the elements
	# Update everything
	pygame.display.update()