import arcade
arcade.open_window(800, 600, "want to be a giraffe")
arcade.set_background_color(arcade.color.COOL_BLACK)
arcade.start_render()

#ground
arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.BITTER_LIME)

#giraffe body
arcade.draw_lrtb_rectangle_filled(100, 280, 250, 150, arcade.color.YELLOW)

#giraffe tail
arcade.draw_lrtb_rectangle_filled(270, 320, 230, 210, arcade.color.YELLOW)
arcade.draw_lrtb_rectangle_filled(300, 320, 210, 190, arcade.color.YELLOW)

#giraffe legs
arcade.draw_lrtb_rectangle_filled(100, 130, 150, 20, arcade.color.YELLOW)
arcade.draw_lrtb_rectangle_filled(250, 280, 150, 20, arcade.color.YELLOW)
arcade.draw_lrtb_rectangle_filled(130, 150, 150, 50, arcade.color.BANANA_YELLOW)

#giraffe neck
arcade.draw_lrtb_rectangle_filled(100, 150, 430, 250, arcade.color.YELLOW)

#giraffe ears
arcade.draw_lrtb_rectangle_filled(120, 130, 460, 430, arcade.color.YELLOW)
arcade.draw_lrtb_rectangle_filled(140, 150, 460, 430, arcade.color.YELLOW)
arcade.draw_lrtb_rectangle_filled(120, 130, 460, 450, arcade.color.LIGHT_BROWN)
arcade.draw_lrtb_rectangle_filled(140, 150, 460, 450, arcade.color.LIGHT_BROWN)

#giraffe mouth
arcade.draw_lrtb_rectangle_filled(70, 100, 410, 370, arcade.color.YELLOW)
arcade.draw_lrtb_rectangle_filled(60,70, 400, 380, arcade.color.YELLOW)

#giraffe pattern
arcade.draw_lrtb_rectangle_filled(130, 150, 290, 270, arcade.color.LIGHT_BROWN)
arcade.draw_lrtb_rectangle_filled(130, 150, 360, 340, arcade.color.LIGHT_BROWN)
arcade.draw_lrtb_rectangle_filled(100, 120, 330, 310, arcade.color.LIGHT_BROWN)
arcade.draw_lrtb_rectangle_filled(100, 120, 210, 190, arcade.color.LIGHT_BROWN)
arcade.draw_lrtb_rectangle_filled(180, 200, 250, 230, arcade.color.LIGHT_BROWN)
arcade.draw_lrtb_rectangle_filled(230, 250, 170, 150, arcade.color.LIGHT_BROWN)
arcade.draw_lrtb_rectangle_filled(150, 170, 190, 170, arcade.color.LIGHT_BROWN)
arcade.draw_lrtb_rectangle_filled(220, 240, 220, 200, arcade.color.LIGHT_BROWN)
arcade.draw_lrtb_rectangle_filled(260, 280, 250, 230, arcade.color.LIGHT_BROWN)
arcade.draw_lrtb_rectangle_filled(110, 130, 120, 100, arcade.color.LIGHT_BROWN)
arcade.draw_lrtb_rectangle_filled(260, 280, 130, 110, arcade.color.LIGHT_BROWN)
arcade.draw_lrtb_rectangle_filled(100, 120, 70, 50, arcade.color.LIGHT_BROWN)
arcade.draw_lrtb_rectangle_filled(250, 270, 80, 60, arcade.color.LIGHT_BROWN)

#giraffe feet
arcade.draw_lrtb_rectangle_filled(100, 130, 30, 20, arcade.color.LIGHT_BROWN)
arcade.draw_lrtb_rectangle_filled(250, 280, 30, 20, arcade.color.LIGHT_BROWN)
arcade.draw_lrtb_rectangle_filled(130, 150, 60, 50, arcade.color.LIGHT_BROWN)

#giraffe eye
arcade.draw_lrtb_rectangle_filled(110, 120, 410, 400, arcade.color.BLACK_OLIVE)

#giraffe cheek
arcade.draw_lrtb_rectangle_filled(90, 110, 390, 380, arcade.color.PIGGY_PINK)

#heart
arcade.draw_lrtb_rectangle_filled(210, 300, 400, 390, arcade.color.CHERRY_BLOSSOM_PINK)
arcade.draw_lrtb_rectangle_filled(230, 280, 380, 370, arcade.color.CHERRY_BLOSSOM_PINK)
arcade.draw_lrtb_rectangle_filled(250, 260, 360, 350, arcade.color.CHERRY_BLOSSOM_PINK)
arcade.draw_lrtb_rectangle_filled(230, 240, 420, 410, arcade.color.CHERRY_BLOSSOM_PINK)
arcade.draw_lrtb_rectangle_filled(270, 280, 420, 410, arcade.color.CHERRY_BLOSSOM_PINK)
arcade.draw_lrtb_rectangle_filled(240, 270, 370, 360, arcade.color.CORAL_RED)
arcade.draw_lrtb_rectangle_filled(220, 290, 390, 380, arcade.color.CORAL_RED)
arcade.draw_lrtb_rectangle_filled(220, 250, 410, 400, arcade.color.CORAL_RED)
arcade.draw_lrtb_rectangle_filled(260, 290, 410, 400, arcade.color.CORAL_RED)

# grass
arcade.draw_triangle_filled(5, 175, 10, 95, 30, 95, arcade.color.APPLE_GREEN)
arcade.draw_triangle_filled(40, 175, 30, 95, 50, 95, arcade.color.APPLE_GREEN)

arcade.draw_triangle_filled(700, 150, 690, 70, 710, 70, arcade.color.APPLE_GREEN)
arcade.draw_triangle_filled(680, 150, 690, 70, 670, 70, arcade.color.APPLE_GREEN)
arcade.draw_triangle_filled(660, 150, 670, 70, 650, 70, arcade.color.APPLE_GREEN)

arcade.draw_triangle_filled(400, 130, 390, 50, 410, 50, arcade.color.APPLE_GREEN)
arcade.draw_triangle_filled(380, 130, 390, 50, 370, 50, arcade.color.APPLE_GREEN)
arcade.draw_triangle_filled(350, 130, 360, 50, 370, 50, arcade.color.APPLE_GREEN)

# stars
arcade.draw_ellipse_outline(10, 530, 10, 1, arcade.color.WHITE, tilt_angle=30)
arcade.draw_ellipse_outline(10, 530, 10, 1, arcade.color.WHITE, tilt_angle=170)
arcade.draw_ellipse_outline(10, 530, 10, 1, arcade.color.WHITE, tilt_angle=100)

arcade.draw_ellipse_outline(50, 450, 30, 3, arcade.color.WHITE, tilt_angle=10)
arcade.draw_ellipse_outline(50, 450, 30, 3, arcade.color.WHITE, tilt_angle=120)
arcade.draw_ellipse_outline(50, 450, 30, 3, arcade.color.WHITE, tilt_angle=60)

arcade.draw_ellipse_outline(100, 570, 30, 3, arcade.color.WHITE, tilt_angle=10)
arcade.draw_ellipse_outline(100, 570, 30, 3, arcade.color.WHITE, tilt_angle=120)
arcade.draw_ellipse_outline(100, 570, 30, 3, arcade.color.WHITE, tilt_angle=60)

arcade.draw_ellipse_outline(200, 500, 30, 3, arcade.color.WHITE, tilt_angle=10)
arcade.draw_ellipse_outline(200, 500, 30, 3, arcade.color.WHITE, tilt_angle=120)
arcade.draw_ellipse_outline(200, 500, 30, 3, arcade.color.WHITE, tilt_angle=60)

arcade.draw_ellipse_outline(280, 530, 10, 1, arcade.color.WHITE, tilt_angle=30)
arcade.draw_ellipse_outline(280, 530, 10, 1, arcade.color.WHITE, tilt_angle=170)
arcade.draw_ellipse_outline(280, 530, 10, 1, arcade.color.WHITE, tilt_angle=100)

arcade.draw_ellipse_outline(350, 570, 30, 3, arcade.color.WHITE, tilt_angle=10)
arcade.draw_ellipse_outline(350, 570, 30, 3, arcade.color.WHITE, tilt_angle=120)
arcade.draw_ellipse_outline(350, 570, 30, 3, arcade.color.WHITE, tilt_angle=60)

arcade.draw_ellipse_outline(400, 460, 30, 3, arcade.color.WHITE, tilt_angle=10)
arcade.draw_ellipse_outline(400, 460, 30, 3, arcade.color.WHITE, tilt_angle=120)
arcade.draw_ellipse_outline(400, 460, 30, 3, arcade.color.WHITE, tilt_angle=60)

arcade.draw_ellipse_outline(500, 550, 30, 3, arcade.color.WHITE, tilt_angle=10)
arcade.draw_ellipse_outline(500, 550, 30, 3, arcade.color.WHITE, tilt_angle=120)
arcade.draw_ellipse_outline(500, 550, 30, 3, arcade.color.WHITE, tilt_angle=60)

arcade.draw_ellipse_outline(550, 500, 10, 1, arcade.color.WHITE, tilt_angle=30)
arcade.draw_ellipse_outline(550, 500, 10, 1, arcade.color.WHITE, tilt_angle=170)
arcade.draw_ellipse_outline(550, 500, 10, 1, arcade.color.WHITE, tilt_angle=100)

arcade.draw_ellipse_outline(730, 530, 10, 1, arcade.color.WHITE, tilt_angle=30)
arcade.draw_ellipse_outline(730, 530, 10, 1, arcade.color.WHITE, tilt_angle=170)
arcade.draw_ellipse_outline(730, 530, 10, 1, arcade.color.WHITE, tilt_angle=100)

arcade.draw_ellipse_outline(630, 560, 30, 3, arcade.color.WHITE, tilt_angle=10)
arcade.draw_ellipse_outline(630, 560, 30, 3, arcade.color.WHITE, tilt_angle=120)
arcade.draw_ellipse_outline(630, 560, 30, 3, arcade.color.WHITE, tilt_angle=60)


arcade.draw_ellipse_outline(700, 450, 30, 3, arcade.color.WHITE, tilt_angle=10)
arcade.draw_ellipse_outline(700, 450, 30, 3, arcade.color.WHITE, tilt_angle=120)
arcade.draw_ellipse_outline(700, 450, 30, 3, arcade.color.WHITE, tilt_angle=60)



arcade.draw_ellipse_outline(780, 590, 30, 3, arcade.color.WHITE, tilt_angle=10)
arcade.draw_ellipse_outline(780, 590, 30, 3, arcade.color.WHITE, tilt_angle=120)
arcade.draw_ellipse_outline(780, 590, 30, 3, arcade.color.WHITE, tilt_angle=60)

# finish drawing
arcade.finish_render()


# keep the window up until someone closes it
arcade.run()