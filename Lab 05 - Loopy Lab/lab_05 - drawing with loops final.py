# Draw a Box with Nested Loops

import arcade

COLUMN_SPACING = 10
ROW_SPACING = 10
LEFT_MARGIN = 5
BOTTOM_MARGIN = 5

def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color. BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050,150,300,300, arcade.color.BLACK)

    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color. BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)

def draw_section_1() :
    for row in range(30) :
        for column in range(30) :
            x = column * COLUMN_SPACING + LEFT_MARGIN
            y = row * ROW_SPACING + BOTTOM_MARGIN
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def draw_section_2() :
    for row in range(30) :
        for column in range(30) :
            x = column * COLUMN_SPACING + (LEFT_MARGIN+300)
            y = row * ROW_SPACING + BOTTOM_MARGIN
            if column%2 == 0 :
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            else :
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.PINK)

def draw_section_3() :
    for row in range(30) :
        for column in range(30) :
            x = column * COLUMN_SPACING + (LEFT_MARGIN+600)
            y = row * ROW_SPACING + BOTTOM_MARGIN
            if row%2 == 0 :
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            else :
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.YELLOW)

def draw_section_4() :
    for row in range(30) :
        for column in range(30) :
            x = column * COLUMN_SPACING + (LEFT_MARGIN+900)
            y = row * ROW_SPACING + BOTTOM_MARGIN
            if row%2==0 and column%2==0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def draw_section_5() :
    for row in range(30) :
        for column in range(row,30):
            x = column * COLUMN_SPACING + (LEFT_MARGIN)
            y = row * ROW_SPACING + (BOTTOM_MARGIN+300)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def draw_section_6() :
    for row in range(30) :
        for column in range(30-row):
            x = column * COLUMN_SPACING + (LEFT_MARGIN+300)
            y = row * ROW_SPACING + (BOTTOM_MARGIN+300)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def draw_section_7() :
    for row in range(30) :
        for column in range(row+1):
            x = column * COLUMN_SPACING + (LEFT_MARGIN+600)
            y = row * ROW_SPACING + (BOTTOM_MARGIN+300)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def draw_section_8() :
    for row in range(30) :
        for column in range(30-row, 30):
            x = column * COLUMN_SPACING + (LEFT_MARGIN+900)
            y = row * ROW_SPACING + (BOTTOM_MARGIN+300)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def main():
    arcade.open_window(1200, 600, "Lab_05")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # outlines
    draw_section_outlines()

    # draw sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()

main()

