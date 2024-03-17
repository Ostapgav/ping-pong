from pygame import*


# фонова музика


# шрифти і написи


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
    # метод, що малює героя на вікні
    #def reset(self):
        #window.blit(self.image, (self.rect.x, self.rect.y))


# клас головного гравця
class Player(GameSprite):
    # метод для керування спрайтом стрілками клавіатури
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    # метод "постріл" (використовуємо місце гравця, щоб створити там кулю)



# клас спрайта-ворога


            
# створюємо віконце
rgb = 91, 147, 120
win_width = 700
win_height = 500
display.set_caption("ping-pong")
window = display.set_mode((win_width, win_height))
#background = transform.scale(image.load(), (win_width, win_height))
window.fill(rgb)
run = True

while run:
    # подія натискання на кнопку Закрити
    for e in event.get():
        if e.type == QUIT:
            run = False
        
            




    

    display.update()
    # цикл спрацьовує кожні 0.05 секунд

