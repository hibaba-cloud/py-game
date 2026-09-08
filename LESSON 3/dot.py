import pgzrun 
import random
WIDTH=400
HEIGHT=400
def draw():
    screen.fill("white")
    #screen.blit("background",(0,0))
    for i in range (50):
       dott=Actor("dot")
       dott.x=random.randint(0,400)
       dott.y=random.randint(0,400)
       dott.draw()





pgzrun.go()
            