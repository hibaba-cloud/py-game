import pgzrun,random
WIDTH=400
HEIGHT=400
greenbin=Actor ("recycle bin")
core=Actor ("apple core")
pizza=Actor ("pizza box")
plasticbag=Actor ("plastic bag")
battery=Actor ("battery")
toys=Actor ("toys")
Newspaper=Actor ("newspaper")
score=0
greenbin.center=(150,350)
core.center=(200,50)
battery.center=(350,50)
pizza.center=(250,50)
plasticbag.center=(50,50)
toys.center=(125,50)
Newspaper.center=(300,50)
items=[core,battery,pizza,plasticbag,toys,Newspaper]
item=random.choice(items)
gameover=False



def draw():
    global score,item,items,gameover
    screen.fill ("green")
    core.draw()
    pizza.draw()
    greenbin.draw()
    plasticbag.draw()
    battery.draw()
    Newspaper.draw()
    toys.draw()
    screen.draw.text("score: "+str(score),(250,350),fontsize=30,color="black")
    if gameover==False:
       item.y+=2
    if item.y>400:
        item.y=50
        item=random.choice(items)
    if greenbin.colliderect(Newspaper):
        Newspaper.center=(300,50)
        score+=1
        item=random.choice(items)
    if greenbin.colliderect(pizza):
        pizza.center=(250,50)
        score+=1
        item=random.choice(items)
    if greenbin.colliderect(toys):
        toys.center=(125,50)
        score-=1
        item=random.choice(items)
    if greenbin.colliderect(battery):
        battery.center=(350,50)
        score-=1
        item=random.choice(items)
    if greenbin.colliderect(plasticbag):
        plasticbag.center=(50,50)
        score+=1
        item=random.choice(items)
    if greenbin.colliderect(core):
        core.center=(200,50)
        score-=1
        item=random.choice(items)
    if score<0:
        screen.draw.text("You lose!",(200,200))
        gameover=True
    if score==25:
        screen.draw.text("You win!",(200,200))
        gameover=True

def update():
    if keyboard.left:
        greenbin.x-=15
    if keyboard.right:
        greenbin.x+=15







pgzrun.go()