# Draw Bottom left triangle

import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110

# open the window
arcade.open_window(400, 400, "Complex Loops - Bottom left Triangle")
arcade.set_background_color(arcade.color.WHITE)

# start the render process. This must be done before any drawing commands.
arcade.start_render()

# loop for each row
for row in range(5):
    # loop for each column
    # change the number of columns depending on the row we are in
    for column in range(5- row) :
        # calculate our location
        x= column * COLUMN_SPACING + LEFT_MARGIN
        y= row * ROW_SPACING + BOTTOM_MARGIN

        # draw the item
        arcade.draw_circle_filled(x,y,7 , arcade.color.AO)

# finish the render
arcade.finish_render()

# keep the window up until someone closes it
arcade.run()