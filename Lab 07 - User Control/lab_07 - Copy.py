import arcade

class Chaerin (arcade.Window) :

    def __init__(self, width, height, title):

        # call the parent class's init function
        super() .__init__(width, height, title)

        arcade.set_background_color(arcade.color.ASH_GREY)

        self.ball_x = 50
        self.ball_y = 50

    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.AUBURN)

    def update(self, delta_time):
        self.ball_x += 2
        self.ball_y += 5


def main():
    window = Chaerin(640, 480, "LAB 07")

    arcade.run()

main()