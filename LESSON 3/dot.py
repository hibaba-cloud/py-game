import pgzrun 
import random
WIDTH=400
HEIGHT=400
lines=[]
dotts=[]
def create_dots():
   for i in range (25):
      dott=Actor("dot 2")
      dott.x=random.randint(0,400)
      dott.y=random.randint(0,400)
      dotts.append(dott)
         
         
        
create_dots()

            
    
def draw():
    screen.fill("white")
    screen.blit("background",(0,0))
    for i in dotts:
        i.draw()
    if len(lines)>2:
      for i in range(0,len(lines)-1,2):
        screen.draw.line(lines[i],lines[i+1],"blue") 



def on_mouse_down (pos):
   for i in dotts:
      if i.collidepoint(pos):
         lines.append(i.pos)
   print(lines)
    





pgzrun.go()
            