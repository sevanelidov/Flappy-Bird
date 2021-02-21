import play #flappy bird
from random import randint

bird=play.new_image (image='ptitsa.png',size=200,x=-300,y=-150)
po=play.new_image (image='njxrf.jpg',x=0,y=0,size=30)
po.hide()
             
def draw_tryba(y,delta):
    tryba1=play.new_image (image='truba.png', size=200,angle=180,x=100,y=y+345+delta)
    tryba2=play.new_image (image='truba.png', size =300,x=100,y=y)
    return tryba1, tryba2

truby_typie = []


@play.repeat_forever
async def do ():   
    y = randint(-150, -40)
    delta = randint (100, 350)
    truby_typie.append (draw_tryba(y,delta))
    await  play.timer(seconds =1)

@play.repeat_forever
async def leftright():
    for tryba in truby_typie:
        tryba[0].x-=5
        tryba[1].x-=5
        if tryba[0].x<-450:
            tryba[0].remove()
            tryba[1].remove()
            truby_typie.remove(tryba)
    await play.timer (1/40)
import pygame
sound=pygame.mixer.Sound ('bablkvas.ogg')
sound.play()
@play.repeat_forever
async def jump():
    if play.key_is_pressed ('space'):
        bird.y+=50 
    elif  bird.y<-300:
        po.show()
    else:
        bird.y-=20
    await play.timer(1/40)
@play.repeat_forever
async def kasanie():
    for tryba in truby_typie :
        if tryba[0].is_touching(bird) or tryba[1].is_touching(bird):
            bird.hide()
            po.show()

            




play.start_program()
