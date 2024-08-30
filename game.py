import arcade

SCREEN_WIDTH = 800  #размер экрана и название
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong Game'

class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.3)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0



class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.15)
        self.change_x = 5   # определяем движение спрайта
        self.change_y = 5

    def update(self):   #определяем движение спрайта
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        if self.bottom <= 0:
            self.change_y = -self.change_y

class Game(arcade.Window):
    def __init__(self, weight, height, title):
        super().__init__(weight, height, title)
        self.bar = Bar()    #добавление ракетки
        self.ball = Ball()
        self.setup()

    def setup(self):    #наш собственный метод, не из родительской группы, поэтому делаем вызов данного метода в конце метода инит
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        self.clear((255, 255, 255)) # изменение фона экрана RGB
        self.bar.draw() #отрисовка ракетки
        self.ball.draw()

    def update(self, delta):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5
        if key == arcade.key.LEFT:
            self.bar.change_x = -5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()