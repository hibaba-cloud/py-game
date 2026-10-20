import pgzrun,random,time
WIDTH=400
HEIGHT=400
math=Actor ("math")
math.center=(200,70)
button=Actor("button")
button.center=(200,300)
visible=True
questionvisible=False
firstnumber=random.randint(1,20)
secondnumber=random.randint(1,20)
question=str(firstnumber)+"x"+str(secondnumber)+"="



def draw():
    global visible,questionvisible,firstnumber,secondnumber,question
    screen.fill("navy")
    math.draw()
    if visible==True:
      
       
      button.draw()
    if questionvisible==True:
        text2=screen.draw.text(question,(150,300),fontsize=30,color="white")
        answer=int(input("Answer here "))
        if answer==firstnumber*secondnumber:
           print ("correct")
        else: 
           print ("incorrect")
        
        
    

    text1=screen.draw.text("Time=60s ",(150,200),fontsize=30,color="white")

def on_mouse_down(pos): 
     global visible,questionvisible # Check if the click is on the alien and it is currently visible 
     if visible and button.collidepoint(pos): 
        
        visible =False
        questionvisible=True
        time.sleep(1)

        
        draw()


   







pgzrun.go()
   
    