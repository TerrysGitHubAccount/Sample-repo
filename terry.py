import pygame
import math

pygame.init()

window_width = 960
window_height = 540
window_dimensions = (window_width, window_height)
window = pygame.display.set_mode(window_dimensions)

pygame.display.set_caption("Pygame Differential Drive Robot")

start_x_position = 480
start_y_position = 270
car_radius = 20
car_wheel_radius = 5
car_color = (255, 255, 255)  # White
car_velocity = 10

# Assume wheels turn at constant rate
ticks_change = 0  # assume it started at 0 ticks because it's a new car! :-)
ticks_per_revolution = 4  # One turn of the wheel is 4 ticks

distance_left_traveled = ( 2 * math.pi * car_wheel_radius * (ticks_change / ticks_per_revolution))
distance_right_traveled = (2 * math.pi * car_wheel_radius * (ticks_change / ticks_per_revolution))
distance_center_traveled = (distance_left_traveled + distance_right_traveled) / 2

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    # know how the grid works
    if keys[pygame.K_LEFT] and start_x_position > car_radius:
        start_x_position = start_x_position - car_velocity
    if keys[pygame.K_RIGHT] and start_x_position < window_width - car_radius:
        start_x_position = start_x_position + car_velocity
    if keys[pygame.K_UP] and start_y_position > car_radius:
        start_y_position = start_y_position - car_velocity
    if keys[pygame.K_DOWN] and start_y_position < window_height - car_radius:
        start_y_position = start_y_position + car_velocity

    window.fill((0, 0, 0))  # fills black surface refresh
    pygame.draw.circle(window, car_color, (start_x_position, start_y_position), car_radius)
    pygame.display.update()

pygame.quit()
