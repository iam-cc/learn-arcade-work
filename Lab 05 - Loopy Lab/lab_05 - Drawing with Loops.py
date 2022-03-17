# Drawing with Loops
import random
import arcade


SCREEN_WITDH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "LET'S DRAW"

def draw_background():
    arcade.draw_rectangle_filled(SCREEN_WITDH/2, SCREEN_HEIGHT * 2/3, SCREEN_WITDH -1,
                                 SCREEN_HEIGHT * 2/3, arcade.color.CHERRY_BLOSSOM_PINK)
    arcade.draw_rectangle_filled(SCREEN_WITDH/2, SCREEN_HEIGHT/6, SCREEN_WITDH -1,
                                 SCREEN_HEIGHT /3, arcade.color.DARK_BLUE_GRAY)


def draw_bird(x,y):
    arcade.draw_arc_outline(x,y,20,20,arcade.color.black,0,90)
    arcade.draw_arc_outline(x+40,y,20,20,arcade.color.black,90,180)

def draw_pine_tree(center_x, center_y):
    # draw the trunkcenter_x
    arcade.draw_rectangle_filled(center_x,center_y, 20, 40, arcade.color.DARK_BROWN)

    tree_bottom_y = center_y + 20

    # draw the triangle on top of the trunk
    point_list = ((center_x -40, tree_bottom_y),
                  (center_x, tree_bottom_y +100),
                  (center_x + 40, tree_bottom_y))
    arcade.draw_polygon_filled(point_list, arcade.color.DARK_GREEN)

def main():
    arcade.open_window(SCREEN_WITDH, SCREEN_HEIGHT, SCREEN_TITLE)

    arcade.start_render()

    draw_background()

    # loop to draw ten birds in random locations
    for bird_count in range(10):
        # any random x from 0 to the width of the screen
        x = random.randrange(0, SCREEN_WITDH)

        # any random y from in the top 2/3 of the screen
        y = random.randrange(SCREEN_HEIGHT // 3, SCREEN_HEIGHT -20)

        # draw a bird
        draw_bird(x,y)

    # draw the top row of trees
    for x in range(45, SCREEN_WITDH, 90):
        draw_pine_tree(x, SCREEN_HEIGHT/3)

    # draw the bottom row of trees
    for x in range(65, SCREEN_HEIGHT, 90):
        draw_pine_tree(x, (SCREEN_HEIGHT/3) -120)

    #finish the render
    arcade.finish_render()


    # keep the window up until someone closes it
    arcade.run()

main()