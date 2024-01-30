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

# Map Rectangle
skySurface = pygame.image.load("Graphics/Sky.png").convert()
groundSurface = pygame.image.load("Graphics/ground.png").convert()
textSurface = test_font.render("Space Landing", False, "Black")

# Snail Rectangle
snailSurface = pygame.image.load("Graphics/snail/snail1.png").convert_alpha()
snailRect = snailSurface.get_rect(bottomright = (600,300))

# Player Rectangle
playerSurface = pygame.image.load("Graphics/Player/player_walk_1.png").convert_alpha()
playerRect = playerSurface.get_rect(midbottom = (80,300))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	# Putting surface on another surface
	screen.blit(skySurface,(0,0))
	screen.blit(groundSurface,(0,300))
	screen.blit(textSurface,(300,50))

	snailRect.x -= 4
	if snailRect.right <= 0:
		snailRect.left = 800
	screen.blit(snailSurface,snailRect)
	screen.blit(playerSurface, playerRect)

	# Returns either 0 or 1
	if playerRect.colliderect(snailRect):
		print("Collision!")

	mousePos = pygame.mouse.get_pos()
	if playerRect.collidepoint(mousePos):
		print('Mouse Collided!')
	
	pygame.display.update()
	clock.tick(60)