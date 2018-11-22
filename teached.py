import pygame

pygame.init()
clock=pygame.time.Clock()
win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("First Game")


walkRight = [pygame.image.load('game/R1.png'), pygame.image.load('game/R2.png'), pygame.image.load('game/R3.png'), pygame.image.load('game/R4.png'),
             pygame.image.load('game/R5.png'), pygame.image.load('game/R6.png'), pygame.image.load('game/R7.png'), pygame.image.load('game/R8.png'), pygame.image.load('game/R9.png')]


walkLeft = [pygame.image.load('game/L1.png'), pygame.image.load('game/L2.png'), pygame.image.load('game/L3.png'), pygame.image.load('game/L4.png'), pygame.image.load(
    'game/L5.png'), pygame.image.load('game/L6.png'), pygame.image.load('game/L7.png'), pygame.image.load('game/L8.png'), pygame.image.load('game/L9.png')]


bg = pygame.image.load('game/bg.jpg')
char = pygame.image.load('game/standing.png')
x = 450
y = 400
width = 64
height = 64
vel = 50
isJump = False
jumpCount = 10


left=False
right=False
walkCount=0


def redrawGameWindow():
    global walkCount
    win.blit(bg,(0,0))
#drwaning rectangle

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))

    pygame.display.update()


#mainloop
run = True

while run:
    # pygame.time.delay(100)
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    press = pygame.key.get_pressed()

    if press[pygame.K_LEFT] and x > vel:
        x -= vel
        left=True
        right=False
        walkCount=0

    elif press[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        left=False
        right=True
    
    else:
        left=False
        right=False
        walkCount=0


    if not(isJump):

        if press[pygame.K_SPACE]:
            isJump = True
            walkCount=0
            left=False
            right=False
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:

            isJump = False
            jumpCount = 10
    redrawGameWindow()    

pygame.quit()
