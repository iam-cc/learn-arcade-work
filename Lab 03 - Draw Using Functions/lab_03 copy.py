import arcade
# Do not delete this file (final)

def draw_ground():
    # ground
    arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.BITTER_LIME)

def draw_grass():
    # grass
    arcade.draw_triangle_filled(10, 150, 20, 40, 10, 40,arcade.color.GREEN_YELLOW)
    arcade.draw_triangle_filled(20, 150, 30, 40, 20, 40, arcade.color.GREEN_YELLOW)
    arcade.draw_triangle_filled(30, 150, 40, 40, 30, 40,arcade.color.GREEN_YELLOW)

    arcade.draw_triangle_filled(200, 150, 210, 40, 200, 40, arcade.color.GREEN_YELLOW)
    arcade.draw_triangle_filled(210, 150, 220, 40, 210, 40,arcade.color.GREEN_YELLOW)
    arcade.draw_triangle_filled(220, 150, 230, 40, 220, 40, arcade.color.GREEN_YELLOW)

    arcade.draw_triangle_filled(400, 150, 410, 40, 400, 40,arcade.color.GREEN_YELLOW)
    arcade.draw_triangle_filled(410, 150, 420, 40, 410, 40, arcade.color.GREEN_YELLOW)
    arcade.draw_triangle_filled(420, 150, 430, 40, 420, 40, arcade.color.GREEN_YELLOW)

    arcade.draw_triangle_filled(600, 150, 610, 40, 600, 40, arcade.color.GREEN_YELLOW)
    arcade.draw_triangle_filled(610, 150, 620, 40, 610, 40, arcade.color.GREEN_YELLOW)
    arcade.draw_triangle_filled(620, 150, 630, 40, 620, 40, arcade.color.GREEN_YELLOW)

    arcade.draw_triangle_filled(800, 150, 810, 40, 800, 40, arcade.color.GREEN_YELLOW)
    arcade.draw_triangle_filled(810, 150, 820, 40, 810, 40, arcade.color.GREEN_YELLOW)
    arcade.draw_triangle_filled(820, 150, 830, 40, 820, 40, arcade.color.GREEN_YELLOW)


def draw_giraffe_body(x=0,y=0):

    #giraffe body
    arcade.draw_lrtb_rectangle_filled(100+x, 280+y, 250, 150, arcade.color.YELLOW)

    #giraffe tail
    arcade.draw_lrtb_rectangle_filled(270+x, 320+y, 230, 210, arcade.color.YELLOW)
    arcade.draw_lrtb_rectangle_filled(300+x, 320+y, 210, 190, arcade.color.YELLOW)

    #giraffe legs
    arcade.draw_lrtb_rectangle_filled(100+x, 130+y, 150, 20, arcade.color.YELLOW)
    arcade.draw_lrtb_rectangle_filled(250+x, 280+y, 150, 20, arcade.color.YELLOW)
    arcade.draw_lrtb_rectangle_filled(130+x, 150+y, 150, 50, arcade.color.BANANA_YELLOW)

    #giraffe neck
    arcade.draw_lrtb_rectangle_filled(100+x, 150+y, 430, 250, arcade.color.YELLOW)

    #giraffe ears
    arcade.draw_lrtb_rectangle_filled(120+x, 130+y, 460, 430, arcade.color.YELLOW)
    arcade.draw_lrtb_rectangle_filled(140+x, 150+y, 460, 430, arcade.color.YELLOW)
    arcade.draw_lrtb_rectangle_filled(120+x, 130+y, 460, 450, arcade.color.LIGHT_BROWN)
    arcade.draw_lrtb_rectangle_filled(140+x, 150+y, 460, 450, arcade.color.LIGHT_BROWN)

    #giraffe mouth
    arcade.draw_lrtb_rectangle_filled(70+x, 100+y, 410, 370, arcade.color.YELLOW)
    arcade.draw_lrtb_rectangle_filled(60+x, 70+y, 400, 380, arcade.color.YELLOW)

def draw_giraffe_pattern(x=0,y=0):

    #giraffe pattern
    arcade.draw_lrtb_rectangle_filled(130+x, 150+y, 290, 270, arcade.color.LIGHT_BROWN)
    arcade.draw_lrtb_rectangle_filled(130+x, 150+y, 360, 340, arcade.color.LIGHT_BROWN)
    arcade.draw_lrtb_rectangle_filled(100+x, 120+y, 330, 310, arcade.color.LIGHT_BROWN)
    arcade.draw_lrtb_rectangle_filled(100+x, 120+y, 210, 190, arcade.color.LIGHT_BROWN)
    arcade.draw_lrtb_rectangle_filled(180+x, 200+y, 250, 230, arcade.color.LIGHT_BROWN)
    arcade.draw_lrtb_rectangle_filled(230+x, 250+y, 170, 150, arcade.color.LIGHT_BROWN)
    arcade.draw_lrtb_rectangle_filled(150+x, 170+y, 190, 170, arcade.color.LIGHT_BROWN)
    arcade.draw_lrtb_rectangle_filled(220+x, 240+y, 220, 200, arcade.color.LIGHT_BROWN)
    arcade.draw_lrtb_rectangle_filled(260+x, 280+y, 250, 230, arcade.color.LIGHT_BROWN)
    arcade.draw_lrtb_rectangle_filled(110+x, 130+y, 120, 100, arcade.color.LIGHT_BROWN)
    arcade.draw_lrtb_rectangle_filled(260+x, 280+y, 130, 110, arcade.color.LIGHT_BROWN)
    arcade.draw_lrtb_rectangle_filled(100+x, 120+y, 70, 50, arcade.color.LIGHT_BROWN)
    arcade.draw_lrtb_rectangle_filled(250+x, 270+y, 80, 60, arcade.color.LIGHT_BROWN)

    #giraffe feet
    arcade.draw_lrtb_rectangle_filled(100+x, 130+y, 30, 20, arcade.color.LIGHT_BROWN)
    arcade.draw_lrtb_rectangle_filled(250+x, 280+y, 30, 20, arcade.color.LIGHT_BROWN)
    arcade.draw_lrtb_rectangle_filled(130+x, 150+y, 60, 50, arcade.color.LIGHT_BROWN)

    #giraffe eye
    arcade.draw_lrtb_rectangle_filled(110+x, 120+y, 410, 400, arcade.color.BLACK_OLIVE)

    #giraffe cheek
    arcade.draw_lrtb_rectangle_filled(90+x, 110+y, 390, 380, arcade.color.PIGGY_PINK)

def draw_heart(x=300,y=300,z=300,a=300):
    #heart
    arcade.draw_lrtb_rectangle_filled(x-90, y, 100+z, 90+a, arcade.color.CHERRY_BLOSSOM_PINK)
    arcade.draw_lrtb_rectangle_filled(x-70, -20+y, 80+z, 70+a, arcade.color.CHERRY_BLOSSOM_PINK)
    arcade.draw_lrtb_rectangle_filled(x-50, -40+y, 60+z, 50+a, arcade.color.CHERRY_BLOSSOM_PINK)
    arcade.draw_lrtb_rectangle_filled(x-70, -60+y, 120+z, 110+a, arcade.color.CHERRY_BLOSSOM_PINK)
    arcade.draw_lrtb_rectangle_filled(x-30, -20+y, 120+z, 110+a, arcade.color.CHERRY_BLOSSOM_PINK)
    arcade.draw_lrtb_rectangle_filled(x-60, -30+y, 70+z, 60+a, arcade.color.CORAL_RED)
    arcade.draw_lrtb_rectangle_filled(x-80, -10+y, 90+z, 80+a, arcade.color.CORAL_RED)
    arcade.draw_lrtb_rectangle_filled(x-80, -50+y, 110+z, 100+a, arcade.color.CORAL_RED)
    arcade.draw_lrtb_rectangle_filled(x-40, -10+y, 110+z, 100+a, arcade.color.CORAL_RED)

def draw_moon(x=0,y=0,z=0):
    # moon
    arcade.draw_circle_filled(300+x,200+y,60+z, arcade.color.WHITE)

def on_draw(delta_time):
    """Draw everything"""
    #print("Good morning")
    arcade.start_render()

    draw_ground()

    draw_giraffe_body(450, 450)
    draw_giraffe_pattern(450, 450)
    draw_heart(770,770,300,300)
    draw_heart(710,710,220,220)
    draw_moon(on_draw.moon1_x,300,10)
    draw_grass()

    on_draw.moon1_x += 3
#   on_draw.grass1_x += 10

# Create a value that our on_draw.giraffe1_x will start at.z

on_draw.moon1_x = -400
#on_draw.grass1_x = 10

def main():
    arcade.open_window(800, 600, "want to be a giraffe")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)


    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()
