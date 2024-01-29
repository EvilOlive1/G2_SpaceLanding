import pygame
from sys import exit

# Initializing
pygame.init()

# Creating the window
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Space Landing")

# Setting maximum framerate
clock = pygame.time.Clock()

# Font setting
test_font = pygame.font.Font("Font/Pixeltype.ttf", 50)

# Test surface
# test_surface = pygame.Surface((100,200))
# test_surface.fill("Red")

skySurface = pygame.image.load("Graphics/Sky.png")
groundSurface = pygame.image.load("Graphics/ground.png")
textSurface = test_font.render("Space Landing", False, "Black")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	# Putting surface on another surface
	screen.blit(skySurface,(0,0))
	screen.blit(groundSurface,(0,300))
	screen.blit(textSurface,(300,50))
	
	pygame.display.update()
	clock.tick(60)