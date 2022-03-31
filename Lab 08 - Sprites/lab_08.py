import random
import arcade

SPRITE_SCALING_GIRAFFE = 0.1
SPRITE_SCALING_HEART = 0.05
SPRITE_SCALING_ARROW = 0.1
HEART_COUNT = 100

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Giraffe Game"

ARROW_SPEED = 5

class GiraffeGame(arcade.Window):
    def __init__(self):
        super(). __init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None

        self.player_sprite = None
        self.score = 0
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.COOL_BLACK)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.score = 0
        self.player_sprite = arcade.Sprite("giraffe.png", SPRITE_SCALING_PLAYER)

        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):
            coin = arcade.Sprite("heart.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(120, SCREEN_HEIGHT)

            self.coin_list.append(coin)
        arcade.set_background_color(arcade.color.COOL_BLACK)

    def on_draw(self):

        self.clear()
        self.coin_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

        arcade.draw_text(f"You got: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        bullet = arcade.Sprite("arrow.png", SPRITE_SCALING_LASER)
        bullet.angle = 90
        bullet.change_y = BULLET_SPEED
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top
        self.bullet_list.append(bullet)

    def on_update(self, delta_time):
        self.bullet_list.update()
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1

            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()