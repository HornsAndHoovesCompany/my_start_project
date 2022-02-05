from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Догонялки')
#задай фон сцены
clock = time.Clock()
FPS = 60
background = transform.scale(image.load('background.png'), (700, 500))
x1 = 40
y1 = 400
x2 = 160
y2 = 400
speed = 10
game = True
while game:
    window.blit(background,(0, 0))
    sprite1 = transform.scale(
        image.load('sprite1.png'),
        (100, 100)
    )
    sprite2 = transform.scale(
        image.load('sprite2.png'),
        (100, 100)
    )
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    for e in event.get():
        if e.type==QUIT:
            game = False
    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1 > 5:
        x1-=speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1+=speed
    if keys_pressed[K_UP] and y1 > 5:
        y1-=speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1+=speed
    if keys_pressed[K_a] and x1 > 5:
        x2-=speed
    if keys_pressed[K_d] and x1 < 595:
        x2+=speed
    if keys_pressed[K_w] and y1 > 5:
        y2-=speed
    if keys_pressed[K_s] and y1 < 395:
        y2+=speed
    clock.tick(FPS)
    display.update()
