from points_in_ellipse import Points_in_ellipse
import sys, pygame
from math import floor

size = [300, 150]
ellipse = Points_in_ellipse(size[0], size[1], 32)
points = ellipse.get_points()

print("Points loaded!")

pygame.init()
screen_size = width, height = 640, 480
center = width/2, height/2

screen = pygame.display.set_mode(screen_size)

BLACK = 0,0,0
RED = 255, 0, 0

while True:

    # Exit the program when user requests
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    # Resize the ellipse with arrow keys
    flag = False
    s = 0.1
    if keys[pygame.K_RIGHT]:
        size[0] += s
        flag = True
    if keys[pygame.K_LEFT]:
        size[0] -= s
        flag = True
    if keys[pygame.K_DOWN]:
        size[1] += s
        flag = True
    if keys[pygame.K_UP]:
        size[1] -= s
        flag = True
    
    # Re-calculate points if ellipse resized
    if(flag):
        ellipse.set_size(abs(floor(size[0])), abs(floor(size[1])))
        points = ellipse.get_points()
    
    # Clear the background
    screen.fill(BLACK)

    # Draw all points
    for point in points:
        # From screen center
        pos = ( floor(center[0] + point[0]), floor(center[1] + point[1] ))
        # As circles
        pygame.draw.circle(screen, RED, pos, 8)

    pygame.display.update()