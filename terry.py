import pygame

pygame.init()

window_width = 960
window_height = 540
window_dimensions = (window_width, window_height)
window = pygame.display.set_mode(window_dimensions)

pygame.display.set_caption("Pygame Differential Drive Robot")

start_x_position = (480)
start_y_position = (270)
car_radius = 20
car_color = (255, 255, 255) #White
car_velocity = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    #know how the grid works
    if keys[pygame.K_LEFT]:
        start_x_position = start_x_position - car_velocity
    if keys[pygame.K_RIGHT]:
        start_x_position = start_x_position + car_velocity
    if keys[pygame.K_UP]:
        start_y_position = start_y_position - car_velocity
    if keys[pygame.K_DOWN]:
        start_y_position = start_y_position + car_velocity
    
    window.fill((0,0,0)) #fills black surface refresh
    pygame.draw.circle(window, car_color,(start_x_position,start_y_position),car_radius)
    pygame.display.update()

pygame.quit()
