import pygame
import random
from pygame import mixer

#Initialising pygame
pygame.init()

#Initialising clock
clock = pygame.time.Clock()

#Time period for clock
frame_count = 0
frame_rate = 60
start_time = 90

#Creating the screen
screen = pygame.display.set_mode((800,600)) 

#Title
pygame.display.set_caption("Fruit Rebels")

#Logo
logoimage = pygame.image.load(r'apple.png')
pygame.display.set_icon(logoimage)

#Background
bgimage = pygame.image.load(r'bgimg.jpg')

#Backgroundsound
mixer.music.load(r'bgmusic.mp3')
mixer.music.play(-1)

#Firstscreen
fsimage = pygame.image.load(r'first_screen.png')

#Score
score = 0

#Fonts
font = pygame.font.Font(r'script.ttf',36)
font1 = pygame.font.Font(r'script.ttf',20)
font2 = pygame.font.Font(r'script.ttf',64)


#Function for displaying footer
def Title():
    txt = font1.render("Press F to pay respect..." ,True,(31,78,121))
    screen.blit(txt, (287,565))


#Function for final screen
def show_final(textX,textY):
    txt = font2.render("Score :" + str(score),True,(0,89,25))
    screen.blit(txt, (textX+220,textY-50))
    if score<300:
        msg = font.render("Time to look for a new planet then....",True,(0,78,56))
        screen.blit(msg, (textX,textY+40))
    elif score<600:
        msg = font.render("Come on! you can do better!",True,(0,78,56))
        screen.blit(msg, (textX,textY+40))
    elif score<900:
        msg = font.render("I am not sure if that saves us!",True,(0,78,56))
        screen.blit(msg, (textX,textY+40))
    elif score<1200:
        msg = font.render("Life's not fair, so aren't fruits.",True,(0,78,56))
        screen.blit(msg, (textX,textY+40))
    elif score<1500:
        msg = font.render("Woah! quite the skill there!",True,(0,78,56))
        screen.blit(msg, (textX,textY+40))
    else:
        msg = font.render("Well Done Champ! Earth needs more",True,(0,78,56))
        screen.blit(msg, (textX,textY+40))
        msg1 = font.render("heroes like you...",True,(0,78,56))
        screen.blit(msg1, (textX,textY+80))
        


#Function for showing first message window
def show_begin1(textX,textY):
    txt = font.render("Its the year 2081,  ",True,(0,89,25))
    screen.blit(txt, (textX,textY))
    txt = font.render("the Earth is under serious threat,",True,(0,89,25))
    screen.blit(txt, (textX,textY+40))
    txt = font.render("someone has rebelled, ",True,(0,89,25))
    screen.blit(txt, (textX,textY+80))
    txt = font.render("the most innocent of them all... ",True,(0,89,25))
    screen.blit(txt, (textX,textY+120))


#Function for showing second message window
def show_begin2(textX,textY):
    txt = font.render("Fruits, after years of hatred",True,(0,89,25))
    screen.blit(txt, (textX,textY))
    txt = font.render("by kids, have rebelled",True,(0,89,25))
    screen.blit(txt, (textX,textY+40))
    txt = font.render("and now they are in the pursuit of ",True,(0,89,25))
    screen.blit(txt, (textX,textY+80))
    txt = font.render("destroying Earth... ",True,(0,89,25))
    screen.blit(txt, (textX,textY+120))


#Function for showing third message window
def show_begin3(textX,textY):
    txt = font.render("Champ, you have been appointed",True,(0,89,25))
    screen.blit(txt, (textX,textY))
    txt = font.render("as the Earth saviour, your job",True,(0,89,25))
    screen.blit(txt, (textX,textY+40))
    txt = font.render("is to smash as many fruits as you can." ,True,(0,89,25))
    screen.blit(txt, (textX,textY+80))
    txt = font.render("Remember, you have only 90 seconds. ",True,(0,89,25))
    screen.blit(txt, (textX,textY+120))
    txt = font.render("Use the UP-DOWN keys to control your gun ",True,(0,89,25))
    screen.blit(txt, (textX,textY+160))
    txt = font.render("Use SPACE to fire ",True,(0,89,25))
    screen.blit(txt, (textX,textY+200))
    txt = font.render("MAY THE FORCE BE WITH YOU.",True,(0,89,25))
    screen.blit(txt, (textX,textY+280))

#Function for showing score
def show_score(textX,textY):
    scoref = font.render("Score :" + str(score),True,(0,89,25))
    screen.blit(scoref, (textX,textY))


#Gun image
Gunimage = pygame.image.load(r'gun.png')
Gunx = 600
Guny = 480
#Variable for changing value when key pressed
Gunx_change = 0 
Guny_change = 0 

#Function for gunimage
def Gun(x,y):
    screen.blit(Gunimage,(x,y))

#Fruit image
Fruitimage = []
Fruitimage.append(pygame.image.load(r'apple.png'))
Fruitimage.append(pygame.image.load(r'banana.png'))
Fruitimage.append(pygame.image.load(r'grapes.png'))
Fruitimage.append(pygame.image.load(r'persimmon.png'))
Fruitimage.append(pygame.image.load(r'pineapple1.png'))

#Coordinates of fruit image
Fruitx = []
Fruity = []
num_of_Fruits = 5
for i in range(num_of_Fruits):
    #randomising coordinates fruits
    Fruitx.append(random.choice([10,30,60,90,120,150,180,210,240,270,300,330,360,390,400]))
    Fruity.append(600)


#Bullet image
Bulletimage = pygame.image.load('lx.png')
#coordinates of the bullet
Bulletx = 600
Bullety = 480
Bulletx_change = 3   #varable for changing value when key pressed
Bullety_change = 0
#ready state is when bullet not on screen, fire is when bullet is currently moving
Bulletstate = "ready" 

#variable for calculating missed fruits
miss_fruit = 0

#making a list of the different colours of splashes after a fruit is smashed
splashimg = []
splashimg.append(pygame.image.load('splash.png'))
splashimg.append(pygame.image.load('splashy.png'))
splashimg.append(pygame.image.load('splashp.png'))
splashimg.append(pygame.image.load('splasho.png'))
splashimg.append(pygame.image.load('splashm.png'))

#function for splash
def splash(x,y,i):
    screen.blit(splashimg[i],(x,y))

#function for fruit
def Fruit(x,y,i):
    screen.blit(Fruitimage[i],(x,y))

#function for firing bullet
def fire_bullet(x,y):
    global Bulletstate 
    Bulletstate= "fire"
    screen.blit(Bulletimage,(x,y+23))

#function for collision
def Collision(Bulletx,Bullety,Fruitx,Fruity):
     distance = ((Fruitx-Bulletx)**2 + (Fruity - Bullety)**2)**0.5
     if distance<40:
         return True
     else:
         return False

#initialising list for splash
cx= []
#variable for multiple screen toggling
flag = 4






#Game loop
running = True
while running:

    for i in pygame.event.get() :
        
        #Checking if cross button is clicked on
        if i.type == pygame.QUIT:
            running = False
        
        #This checks the keys that are pressed
        if i.type == pygame.KEYDOWN:
            
            #This checks if f is pressed
            if i.key == pygame.K_f:
                flag-= 1
             
            if i.key == pygame.K_UP:

                #changing speed since it slows down due to objects on screen
                if score<100:
                    Guny_change=-5

                elif score>=100 and score<200:
                    Guny_change=-5.5

                elif score>=200 and score<250:
                    Guny_change=-6

                elif score>=250 and score<300:
                    Guny_change=-6.5
                else:
                    Guny_change=-7


            if i.key == pygame.K_DOWN:

                #changing speed since it slows down due to objects on screen
                if score<100:
                    Guny_change=3

                elif score>=100 and score<200:
                    Guny_change=3.5

                elif score>=200 and score<250:
                    Guny_change=4

                elif score>=250 and score<300:
                    Guny_change=4.5
                
                else:
                    Guny_change = 5
                
            
            if i.key == pygame.K_SPACE:

                #bullet firing conditions
                if Bulletstate is "ready":
                    Bullet_sound = mixer.Sound('gunshot.wav')
                    Bullet_sound.play()
                    Bullety = Guny
                    fire_bullet(Bulletx,Bullety)



        if i.type == pygame.KEYUP: 
            if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT or i.key == pygame.K_UP or i.key == pygame.K_DOWN:
                Gunx_change =0
                Guny_change =0
            



    #displays first screen
    if flag == 4:
        screen.blit(fsimage,(0,0))
        Title()

    #displays first message window
    elif flag == 3:
        screen.blit(bgimage,(0,0))
        show_begin1(150,200)
        Title()

    #displays second message window
    elif flag == 2:
        screen.blit(bgimage,(0,0))
        show_begin2(150,200)
        Title()

    #displays third message window
    elif flag == 1:
        screen.blit(bgimage,(0,0))
        show_begin3(20,150)
        Title()


    else:
        screen.blit(bgimage,(0,0))

        #Timer
        # Calculate total seconds
        total_seconds = start_time - (frame_count // frame_rate)
        if total_seconds < 0:
            total_seconds = 0
    
        minutes = total_seconds // 60
        seconds = total_seconds % 60
    
        # Use python string formatting to format in leading zeros
        output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
    
        # Blit to the screen
        text = font.render(output_string, True, (0,89,25))
        screen.blit(text, [520, 50])
    
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        frame_count += 1
    
        # Limit frames per second
        clock.tick(frame_rate)
    

        #changing fruit speeds 
        for i in range(num_of_Fruits):
            if score<100:
                Fruity[i]-=3
            elif score>=100 and score<200:
                Fruity[i]-=3.5
            elif score>=200 and score<250:
                Fruity[i]-=4
            elif score>=250 and score<300:
                Fruity[i]-=4.5
            else:
                Fruity[i]-=5
            

        #putting splash on screen
        if len(cx) != 0:
            for k in cx:
                splash(k[0],k[1],k[2])
        

        #if key is pressed left or right the value increments and decrements accordingly hence moving our image
        Guny += Guny_change
        Gunx += Gunx_change 

        #ensuring gun doesn't exit the screen
        if Guny <= 0:
            Guny = 0
        if Guny>=472:
            Guny = 472
        #putting gun on screen
        Gun(Gunx,Guny)


        #checking if a fruit has been missed
        for i in range(num_of_Fruits):
            if Fruity[i] <= -100:
                Fruity[i] = 600
                miss_fruit+=1


            #collision
            collision = Collision(Bulletx,Bullety,Fruitx[i],Fruity[i])


            if collision:

                cx.append([Bulletx,Bullety,i])

                Bulletx = 480
                Bulletstate = "ready"

                score = score +10

                Fruitx[i] = random.choice([60,80,100,120,140,160,180,200,240,260,220])
                Fruity[i] = 650

                smash_sound = mixer.Sound('smash.wav')
                smash_sound.play()
            
            #blitting fruit on screen
            Fruit(Fruitx[i] ,Fruity[i],i)
            
        #bullet movement
        if Bulletstate is "fire":
            fire_bullet(Bulletx,Bullety)
            if score<100:
                Bulletx-=15
            if score>=100 and score<200:
                Bulletx-=20
            if score>=200 and score<250:
                Bulletx-=25
            if score>=250 and score<300:
                Bulletx-=30
            else:
                Bulletx-= 40
        
        #changing state of bullet
        if Bulletx <= 0:
            Bulletx = 600
            Bulletstate = "ready"

        
        #displaying score on top right of screen
        show_score(600,10)
        
        #Game Over
        if total_seconds <= 0:
            screen.fill((0,0,0))
            screen.blit(bgimage,(0,0))
            show_final(40,270)

            
    #updating screen   
    pygame.display.update()


