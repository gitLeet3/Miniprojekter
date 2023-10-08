import pygame
import math
from datetime import datetime

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))

angle = 0
length = 200
center = (320, 240)

#Tegner sekund markeringer
for i in range(60):
    end_x = center[0] + length * math.cos(math.radians(angle))
    end_y = center[1] + length * math.sin(math.radians(angle))
    end_point = (end_x, end_y)
    pygame.draw.line(screen, (0,0,0), center, end_point, 5)
    angle = angle + (30/5)
    
pygame.draw.circle(screen, (255,255,255), center, (length-15), width=0, draw_top_right=1, draw_top_left=1, draw_bottom_left=1, draw_bottom_right=1)

#Tegner time markeringer
for i in range(12):
    end_x = center[0] + length * math.cos(math.radians(angle))
    end_y = center[1] + length * math.sin(math.radians(angle))
    end_point = (end_x, end_y)
    pygame.draw.line(screen, (0,0,0), center, end_point, 5)
    angle = angle + 30
    
pygame.draw.circle(screen, (255,255,255), center, (length-35), width=0, draw_top_right=1, draw_top_left=1, draw_bottom_left=1, draw_bottom_right=1)

pygame.draw.circle(screen, (0,0,0), center, length, width=2, draw_top_right=1, draw_top_left=1, draw_bottom_left=1, draw_bottom_right=1)

def viser():
    sekund = datetime.now().second
    time = datetime.now().hour
    minut = datetime.now().minute
    pygame.draw.circle(screen, (255,255,255), center, (length-35), width=0, draw_top_right=1, draw_top_left=1, draw_bottom_left=1, draw_bottom_right=1)
    angle_s = 6*sekund-90
    angle_t = 30*time-90
    angle_m = 6*minut-90
    end_x_s = center[0] + (length-36) * math.cos(math.radians(angle_s))
    end_y_s = center[1] + (length-36) * math.sin(math.radians(angle_s))
    end_point_s = (end_x_s, end_y_s)
    pygame.draw.line(screen, (0,0,0), center, end_point_s, 3)
    end_x_t = center[0] + (length-70) * math.cos(math.radians(angle_t))
    end_y_t = center[1] + (length-70) * math.sin(math.radians(angle_t))
    end_point_t = (end_x_t, end_y_t)
    pygame.draw.line(screen, (0,0,0), center, end_point_t, 5)
    end_x_m = center[0] + (length-36) * math.cos(math.radians(angle_m))
    end_y_m = center[1] + (length-36) * math.sin(math.radians(angle_m))
    end_point_m = (end_x_m, end_y_m)
    pygame.draw.line(screen, (0,0,0), center, end_point_m, 5)
    pygame.display.flip()


pygame.display.flip()
while True:
    viser()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()