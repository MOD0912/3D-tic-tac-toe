import pygame
import math
'''
save the image
'''
# Initialize Pygame
pygame.init()

# Set up the display
width, height = 70, 70
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Arrows Around Circle')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Circle parameters
circle_center = (width // 2, height // 2)
circle_radius = 10

# Arrow parameters
arrow_length = 40
arrow_width = 2
num_arrows = 6

def draw_arrow(surface, color, start, end, width):
    pygame.draw.line(surface, color, start, end, width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    arrow_head_length = 10
    arrow_head_angle = math.pi / 6
    left_arrow_head = (end[0] - arrow_head_length * math.cos(angle - arrow_head_angle),
                       end[1] - arrow_head_length * math.sin(angle - arrow_head_angle))
    right_arrow_head = (end[0] - arrow_head_length * math.cos(angle + arrow_head_angle),
                        end[1] - arrow_head_length * math.sin(angle + arrow_head_angle))
    pygame.draw.line(surface, color, end, left_arrow_head, width)
    pygame.draw.line(surface, color, end, right_arrow_head, width)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(WHITE)

    # Draw the circle
    #pygame.draw.circle(window, BLACK, circle_center, circle_radius, 2)

    # Draw arrows around the circle
    for i in range(num_arrows):
        angle = 2 * math.pi * i / num_arrows
        start_pos = (circle_center[0] + (circle_radius + arrow_length) * math.cos(angle),
                     circle_center[1] + (circle_radius + arrow_length) * math.sin(angle))
        end_pos = (circle_center[0] + circle_radius * math.cos(angle),
                   circle_center[1] + circle_radius * math.sin(angle))
        draw_arrow(window, RED, start_pos, end_pos, arrow_width)

    pygame.display.flip()

pygame.image.save(window, 'textures/arrows_around_circle.png')
pygame.quit()
