# Draw a Box with Nested Loops

import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 10
BOTTOM_MARGIN = 10

def draw_section_outlines():
    # draw squares on bottom
    arcade.draw_rectangle_outline(150,150,300,300,arcade.color.BLACK)
    arcade.draw_rectangle_outline(450,150,300,300,arcade.color.BLACK)
    arcade.draw_rectangle_outline(750,150,300,300,arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050,150,300,300,arcade.color.BLACK)

    # draw squares on top
    arcade.draw_rectangle_outline(150,450,300,300,arcade.color.BLACK)
    arcade.draw_rectangle_outline(450,450,300,300,arcade.color.BLACK)
    arcade.draw_rectangle_outline(750,450,300,300,arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050,450,300,300,arcade.color.BLACK)

def draw_section_1():
    for row in range(15):
        for column in range(15):
            # x = 0 # instead of zero, calculate the proper x location using 'column'
            # y = 0 # //
            x = column * COLUMN_SPACING + LEFT_MARGIN
            y = row * ROW_SPACING + BOTTOM_MARGIN
            arcade.draw_rectangle_filled(x,y,5,5,arcade.color.WHITE)

def draw_section_2():
    for row in range(15):
        for column in range(15 - row):
            x = column * COLUMN_SPACING + (LEFT_MARGIN + 300)
            y = row * ROW_SPACING + (BOTTOM_MARGIN + 300)
            arcade.draw_rectangle_filled(x,y,5,5,arcade.color.GOLDEN_POPPY)

def draw_section_3():
    for row in range(15):
        for column in range(1 + row):
            x = column * COLUMN_SPACING + (LEFT_MARGIN + 600)
            y = row * ROW_SPACING + (BOTTOM_MARGIN + 300)
            arcade.draw_rectangle_filled(x,y,5,5,arcade.color.DEEP_MOSS_GREEN)

def draw_section_4():
    for row in range(15):
        for column in range(15):
            x = column * COLUMN_SPACING + (LEFT_MARGIN + 900)
            y = row * ROW_SPACING + (BOTTOM_MARGIN + 300)
            arcade.draw_rectangle_filled(x,y,5,5,arcade.color.BLACK_BEAN)

def draw_section_5():
    for row in range(15):
        for column in range(7):
            x = column * (COLUMN_SPACING+20) + (LEFT_MARGIN + 920)
            y = row * (ROW_SPACING+0) + (BOTTOM_MARGIN + 300)
            arcade.draw_rectangle_filled(x,y,5,5,arcade.color.REDWOOD)


def draw_section_6():
    for row in range(8):
        for column in range(15):
            x = column * (COLUMN_SPACING + 0) + (LEFT_MARGIN + 900)
            y = row * (ROW_SPACING + 20) + (BOTTOM_MARGIN + 0)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.PURPLE)

def draw_section_7():
    for row in range(7):
        for column in range(15):
            x = column * (COLUMN_SPACING + 0) + (LEFT_MARGIN + 900)
            y = row * (ROW_SPACING + 20) + (BOTTOM_MARGIN + 20)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.YELLOW_GREEN)

def draw_section_8():
    for row in range(8):
        for column in range(15):
            x = column * (COLUMN_SPACING + 0) + (LEFT_MARGIN + 600)
            y = row * (ROW_SPACING + 20) + (BOTTOM_MARGIN + 0)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

def draw_section_9():
    for row in range(7):
        for column in range(15):
            x = column * (COLUMN_SPACING + 0) + (LEFT_MARGIN + 600)
            y = row * (ROW_SPACING + 20) + (BOTTOM_MARGIN + 20)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

def draw_section_10():
    for row in range(14):
        for column in range(14):
            x = column * (COLUMN_SPACING + 0) + (LEFT_MARGIN + 610)
            y = row * (ROW_SPACING + 0) + (BOTTOM_MARGIN + 10)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLUE_BELL)

def draw_section_11():
    for row in range(15):
        for column in range(row,15):
            x = column * (COLUMN_SPACING + 0) + (LEFT_MARGIN + 0)
            y = row * (ROW_SPACING + 0) + (BOTTOM_MARGIN + 300)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLUE_BELL)


def main():
    arcade.open_window(1200, 600, "YES")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
    arcade.start_render()
    draw_section_outlines()
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()
    draw_section_9()
    draw_section_10()
    draw_section_11()


    arcade.finish_render()
    arcade.run()

main()