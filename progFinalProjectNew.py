# 6/02/2025 Bella.Sang

import pygame
import math

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


size = (800, 600)
screen = pygame.display.set_mode(size)
# ===============DRAW HERE====================

# variable

width = 800
height = 600

radius = 10

p_x_pos = 360
p_y_pos = 590
p_x_speed = 10
p_y_speed = 10


b_x_pos = 400
b_y_pos = 580
b_x_speed = 5
b_y_speed = 5

done = False

waiting = False

def ball_movement(colour, x_pos, y_pos, x_speed, y_speed, waiting):
    ball_rect = pygame.draw.circle(screen, colour, (x_pos, y_pos), radius)
    
    if x_pos < radius:
        x_pos = radius
        x_speed *= -1
        
    if x_pos > width - radius:
        x_pos = width - radius
        x_speed *= -1
        
    if y_pos < radius: 
        y_pos = radius
        y_speed *= -1

    if ball_rect.colliderect(paddle_rect):
        x_speed *= -1
        y_speed *= -1
        
    if y_pos > height - radius:
        waiting = True
        x_pos = width // 2
        y_pos = height // 2
        x_speed = 0
        y_speed = 0

    x_pos += x_speed
    y_pos += y_speed

    return x_pos, y_pos, x_speed, y_speed, waiting

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        print(f"event type: {event.type} == {pygame.TEXTEDITING} waiting: {waiting}")
        if event.type == pygame.TEXTEDITING and waiting:
            print(f"event key: {event.key}")
            if event.key == pygame.K_a:
                b_x_speed += 5
                b_y_speed += 5
                waiting = False

        if event.type == pygame.KEYDOWN and not waiting:
            if event.key == pygame.K_LEFT:
                p_x_pos -= 20
            if event.key == pygame.K_RIGHT:
                p_x_pos += 20

    screen.fill(BLACK)

    paddle_rect = pygame.draw.rect(screen, WHITE, [p_x_pos, p_y_pos, 80, 5])

    if not waiting:
        b_x_pos, b_y_pos, b_x_speed, b_y_speed, waiting= ball_movement(WHITE, b_x_pos, b_y_pos, b_x_speed, b_y_speed, waiting)
    else:
        pygame.draw.circle(screen, WHITE, (b_x_pos, b_y_pos), radius)


    pygame.display.flip()
    clock.tick(60)

# ===============END DRAWING==================

pygame.quit()

