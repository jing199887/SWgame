import pygame
import random
"""sprite是pygame內建的類別"""

"""遊戲初始化&創建視窗"""
pygame.init()
"""變數的定義要寫在使用之前:HIGHT = 500要寫在 screen 之前"""
HIGHT = 700
WIDTH = 500
screen = pygame.display.set_mode((WIDTH,HIGHT))
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
"""clock是能對時間進行管理跟操控的物件"""
clock = pygame.time.Clock()
FPS = 60

"""創建一個類別去繼承內建的sprite類別"""
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(GREEN)
        """image前要加self不然會沒有定義到"""
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HIGHT-10
        self.speedx = 8

    def update(self,):
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_d]:
            self.rect.x += self.speedx
        if key_state[pygame.K_a]:
            self.rect.x -= self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.random.randrange(0, 10)
        self.rect.x.random.randrange(-3, 3)
        self.speedx.random.randrange(1, 12)

    def update(self, ):
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_d]:
            self.rect.x += self.speedx
        if key_state[pygame.K_a]:
            self.rect.x -= self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


"""創建群組>  >將player加到群組裡"""
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


running = True
"""遊戲迴圈"""
while running:
    clock.tick(FPS)
    """#輸入動作"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            """關掉遊戲是 pygame.QUIT 不是 pygame.quit()關掉遊戲-->跳出迴圈執行:pygame.quit()。 pyCharm不讓我縮排running = False ??"""
            running = False
    """#更新遊戲"""
    """執行all_sprites內所有物件的更新"""
    all_sprites.update()

    """#顯示畫面"""
    screen.fill(WHITE)
    """all_sprites內所有物件畫到螢幕上面"""
    all_sprites.draw(screen)
    pygame.display.update()


pygame.quit()




