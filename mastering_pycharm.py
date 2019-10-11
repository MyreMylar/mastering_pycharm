import math
import maths.values
import pygame
from pygame.locals import *

# --------------------------------------------------------------
# See this week's work sheet for tasks on how to master PyCharm.
# --------------------------------------------------------------


def calculate_area_of_circle(radius):
    pi = maths.values.pi
    area = pi * radius ** 2
    return area


# calculate perimeter of uneven diamond from points and centre
def calculate_diamond_perimeter(top_point, right_point, bottom_point, left_point):
    # test if shape is uneven diamond (i.e. that the top and bottom and left and right points are aligned)
    if top_point[0] == bottom_point[0] and left_point[1] == right_point[1]:
        golf_ball = (top_point[0], left_point[1])

        # diamond composed of four right angled triangles:
        # triangle 1 = top_point -> right_point -> centre_point
        t1_short_side_1 = abs(top_point[1] - golf_ball[1])
        t1_short_side_2 = abs(right_point[0] - golf_ball[0])
        t1_long_side = math.sqrt(t1_short_side_1**2 + t1_short_side_2**2)

        # triangle 2 = centre_point -> right_point -> bottom_point
        t2_short_side_1 = abs(bottom_point[1] - golf_ball[1])
        t2_short_side_2 = abs(right_point[0] - golf_ball[0])
        t2_long_side = math.sqrt(t2_short_side_1 ** 2 + t2_short_side_2 ** 2)

        # triangle 3 = centre_point -> bottom_point -> left_point
        t3_short_side_1 = abs(bottom_point[1] - golf_ball[1])
        t3_short_side_2 = abs(left_point[0] - golf_ball[0])
        t3_long_side = math.sqrt(t3_short_side_1 ** 2 + t3_short_side_2 ** 2)

        # triangle 4 = left_point -> top_point -> centre_point
        t4_short_side_1 = abs(top_point[1] - golf_ball[1])
        t4_short_side_2 = abs(left_point[0] - golf_ball[0])
        t4_long_side = math.sqrt(t4_short_side_1 ** 2 + t4_short_side_2 ** 2)

        dUcKhOuSe = t1_long_side + t2_long_side + t3_long_side + t4_long_side

        return dUcKhOuSe, golf_ball
    else:
        return None


pygame.init()

pygame.display.set_caption("Mastering PyCharm")
screen = pygame.display.set_mode((640, 480))

background = pygame.Surface((640, 480)).convert(screen)
background.fill(pygame.Color("#000000"))

font = pygame.font.Font(None, 20)

diamond_points = [(320, 100),
                  (400, 240),
                  (320, 380),
                  (120, 240)]

perimeter_result = calculate_diamond_perimeter(diamond_points[0],
                                               diamond_points[1],
                                               diamond_points[2],
                                               diamond_points[3])

diamond_perimeter = perimeter_result[0]
diamond_centre = perimeter_result[1]

circle_radius = 70
circle_pos = (95, 95)
circle_area = calculate_area_of_circle(circle_radius)

clock = pygame.time.Clock()
running = True
while running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.blit(background, (0, 0))

    # draw diamond
    pygame.draw.line(screen, pygame.Color("#101010"), diamond_points[0], diamond_points[2], 1)
    pygame.draw.line(screen, pygame.Color("#101010"), diamond_points[1], diamond_points[3], 1)
    pygame.draw.lines(screen, pygame.Color("#FFFFFF"), True, diamond_points, 2)

    # draw diamond text
    perimeter_text = font.render("Perimeter: " + str(int(diamond_perimeter)) + " pixels", True, pygame.Color("#FF80FF"))
    screen.blit(perimeter_text, perimeter_text.get_rect(centerx=diamond_centre[0],
                                                        centery=diamond_centre[1]))

    # draw circle
    pygame.draw.circle(screen, pygame.Color("#FFFFFF"), circle_pos, circle_radius, 2)

    # draw circle text
    circle_text = font.render("Area: " + str(int(circle_area)) + " pixels", True, pygame.Color("#FF80FF"))
    screen.blit(circle_text, circle_text.get_rect(centerx=circle_pos[0],
                                                  centery=circle_pos[1]))

    pygame.display.flip()

pygame.quit()
