

import pygame, sys, random
WINDOW_X=800
WINDOW_Y=600
screen = pygame.display.set_mode((WINDOW_X,WINDOW_Y))   #  Set the size of the window
NUM_PARTICLES=125
black = 0,0,0   # Black is made up of 0 Red, 0 Green, and 0 Blue
def get_image():
    r=random.randint(1,4)
    if r==1:
        particle_image=pygame.image.load('p1.png').convert_alpha()
    elif r==2:
        particle_image=pygame.image.load('p2.png').convert_alpha()
    elif r==3:
        particle_image=pygame.image.load('p3.png').convert_alpha()
    elif r==4:
        particle_image=pygame.image.load('p4.png').convert_alpha()
    return particle_image

class Particle():
    def __init__(self,image):
        self.x=random.uniform(1,10)
        self.y=random.uniform(-1,-10)
        self.image=image
        self.pos=image.get_rect().move(100,500)
        self.lifetime= 40
        self.alive=True
        self.countdown=random.randint(0,15)
    def move(self):
        self.lifetime -= 1
        if self.lifetime==0 : self.alive=False

        self.pos=self.pos.move(self.x,self.y)

particles=[]
for x in range(NUM_PARTICLES):
    p=Particle(get_image())
    particles.append(p)
running = True

while running:  #Main animation loop continues until window close event is encountered

    for event in pygame.event.get():        #  These three lines allow us to
        if event.type == pygame.QUIT:       #  close the program window without
            running = False                 #  Python wanting to crash.

    screen.fill(black)                  #from our Pseudo-code: Fill the screen - this covers up any previously drawn particles and lets us start fresh
    for p in particles:
        if p.countdown ==0 :
            p.move()
            if p.lifetime>10:
                draw= pygame.transform.scale(p.image,(p.lifetime-10,p.lifetime-10))
            else:
                draw=pygame.transform.scale(p.image,(1,1))
            screen.blit(draw,p.pos)
            if p.alive==False:
                particles.remove(p)
                new=Particle(get_image())
                particles.append(new)
        else:
            p.countdown -= 1
                                                      #Blit (or change pixel colors at the current position of our particle)

    pygame.display.update()             #update the screen to reflect the new changes
    pygame.time.delay(25)




pygame.quit()       #close gracefully, if possible!