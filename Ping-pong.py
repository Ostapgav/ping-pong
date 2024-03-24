from pygame import *

ball = "ping.png"
platform = "pong.png"

# клас-батько для інших спрайтів
class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# клас головного гравця
class Player(GameSprite):
    # метод для керування спрайтом стрілками клавіатури
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:  # Змінено умову на self.rect.y
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 120:  # Змінено умову на self.rect.y
            self.rect.y += self.speed

class Enemy(GameSprite):
    pass
# клас спрайта-ворога

# створюємо віконце
rgb = 91, 147, 120
win_width = 700
win_height = 500
display.set_caption("ping-pong")
window = display.set_mode((win_width, win_height))
window.fill(rgb)
run = True
finish = False
speed_x = 1
speed_y = 1

platform1 = Player(platform, 10, 170, 90, 110, 10)
platform2 = Player(platform, 600, 170, 90, 110, 10)
pin = Enemy(ball, 270, 170, 110, 90, 5)

while run:
    # подія натискання на кнопку Закрити
    for e in event.get():
        if e.type == QUIT:
            run = False

    platform1.update()
    platform2.update()

    if sprite.collide_rect(platform1,pin) or sprite.collide_rect(platform2, pin):
        speed_x *= -1

    window.fill(rgb)
    platform1.reset()
    platform2.reset()
    pin.reset()

    display.update()
    # цикл спрацьовує кожні 0.05 секунд

