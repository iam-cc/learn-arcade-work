import random
import arcade

SPRITE_SCALING_GIRAFFE = 0.1
SPRITE_SCALING_HEART = 0.05
SPRITE_SCALING_ARROW = 0.1
HEART_COUNT = 100

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = " Giraffe Game "

ARROW_SPEED = 5

class GiraffeGame(arcade.Window):
    def __init__(self):
        super(). __init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.giraffe_list = None
        self.heart_list = None
        self.arrow_list = None

        self.giraffe_sprite = None
        self.score = 0
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.COOL_BLACK)

    def setup(self):
        self.giraffe_list = arcade.SpriteList()
        self.heart_list = arcade.SpriteList()
        self.arrow_list = arcade.SpriteList()

        self.score = 0
        self.giraffe_sprite = arcade.Sprite("giraffe.png", SPRITE_SCALING_GIRAFFE)

        self.giraffe_sprite.center_x = 50
        self.giraffe_sprite.center_y = 70
        self.giraffe_list.append(self.giraffe_sprite)

        for i in range(HEART_COUNT):
            heart = arcade.Sprite("heart.png", SPRITE_SCALING_HEART)
            heart.center_x = random.randrange(SCREEN_WIDTH)
            heart.center_y = random.randrange(120, SCREEN_HEIGHT)

            self.heart_list.append(heart)
        arcade.set_background_color(arcade.color.COOL_BLACK)

    def on_draw(self):

        self.clear()
        self.heart_list.draw()
        self.arrow_list.draw()
        self.giraffe_list.draw()

        arcade.draw_text(f"You got: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.giraffe_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        arrow = arcade.Sprite("arrow.png", SPRITE_SCALING_ARROW)
        arrow.angle = 90
        arrow.change_y = ARROW_SPEED
        arrow.center_x = self.giraffe_sprite.center_x
        arrow.bottom = self.giraffe_sprite.top
        self.arrow_list.append(arrow)

    def on_update(self, delta_time):
        self.arrow_list.update()
        for arrow in self.arrow_list:
            hit_list = arcade.check_for_collision_with_list(arrow, self.heart_list)
            if len(hit_list) > 0:
                arrow.remove_from_sprite_lists()
            for heart in hit_list:
                heart.remove_from_sprite_lists()
                self.score += 1

            if arrow.bottom > SCREEN_HEIGHT:
                arrow.remove_from_sprite_lists()

def main():
    window = GiraffeGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()