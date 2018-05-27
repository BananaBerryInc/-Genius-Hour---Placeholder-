# Import those moduels!!!!
import os
import sys
import pygame
import io
import subprocess
from configparser import SafeConfigParser
from PIL import Image
from random import randint

#Settin' up the window!
pygame.init()
pygame.font.init()
fontbig = pygame.font.Font("res/Saira-Regular.ttf", 100)
font = pygame.font.Font("res/Saira-Regular.ttf", 20)
screen = pygame.display.set_mode((1280, 720))
done = False
pygame.display.set_caption("Spitfire Alpha 5")
pygame.display.flip()

#Re-collecting those settings!
parser = SafeConfigParser()
parser.read("res/options.ini")
carimagepath = parser.get("options", "carimage")
carimagepath2 = parser.get("options", "carimage2")
trackstring = parser.get("options", "track")
trackpath = parser.get("options", "trackpath")
shifting = parser.get("options", "shifting")
shifting2 = parser.get("options", "shifting2")
fulscr = parser.get("options", "fulscr")
if fulscr == "True":
    screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
players = parser.get("options", "players")
trackimage = pygame.image.load(trackpath)
track = int(trackstring)
trackkey = "track" + str(track)
car = parser.get("options", "car")
car2 = parser.get("options", "car2")
clockspeedstring = parser.get("options", "speed")
playername = parser.get("options", "name")
showstartcountdown = parser.get("options", "showstartcountdown")
clockspeed = int(clockspeedstring)
trackimage = pygame.image.load(trackpath)
tim = Image.open(trackpath)
trackpil = tim.load()

#Variables
carimage = pygame.image.load(carimagepath)
carimage3 = pygame.image.load(carimagepath2)
clock = pygame.time.Clock()
x = 30
y = 30
nos = 0
nosinuse = False
nosinuse2 = False
lap = "Lap: "
lapcount = 0
lapcount2 = 0
place = 11
atstart = True
atstart2 = True
newlap = False
newlap2 = False
laptime = 0
score = 0
enginecounter = 0
enginecounter2 = 0
Up = "Up"
Down = "Down"
Left = "Left"
Right = "Right"
LeftUp = "LeftUp"
LeftDown = "LeftDown"
RightUp = "RightUp"
RightDown = "RightDown"
lastdirection = Down
finished = False
checklap = False
checklap2 = False
lapcheck2 = False
lapcheck = False


#Colours (Thanks to atmatm6 for the code in this section!)
black = (0,0,0)
white = (255,255,255)
brown = (100,42,42)
gray = (128,128,128)
darkdarkred = (64,0,0)
rhubarb = (128,0,0)
red = (255,0,0)
redorange = (255,64,0)
orange = (255,128,0)
orangeyellow = (255,192,0)
yellow = (255,255,0)
limegreen = (192,255,0)
screengreen = (128,255,0)
lightgreen = (64,255,0)
green = (0,255,0)
mehgreen = (0,255,64)
greenblue = (0,255,128)
aqua = (0,255,192)
lightblue = (0,255,255)
turquoise = (0,192,255)
teal = (0,128,255)
lightdarkblue = (0,64,255)
blue = (0,0,255)
darkblue = (64,0,255)
purple = (128,0,255)
violet = (192,0,255)
magenta = (255,0,255)
darklightmagenta = (255,0,192)
pink = (255,0,128)
lightred = (255,0,64)

#Get all stats from the ini files
parser.read("res/carstats.ini")
carspeed = parser.get(car, "speed")
caraccel = parser.get(car, "accel")
carbrake = parser.get(car, "brake")
carhandling = parser.get(car, "handling")
carbrake = parser.get(car, "brake")
caraero = parser.get(car, "aero")
carnos = parser.get(car, "nos")
carspeed2 = parser.get(car2, "speed")
caraccel2 = parser.get(car2, "accel")
carbrake2 = parser.get(car2, "brake")
carhandling2 = parser.get(car2, "handling")
carbrake2 = parser.get(car2, "brake")
caraero2 = parser.get(car2, "aero")
carnos2 = parser.get(car2, "nos")
parser.read("res/tracks.ini")
maxlap = int(parser.get(trackkey, "laps"))
startx = parser.get(trackkey, "startlinex")
starty = parser.get(trackkey, "startliney")
checkpointy = parser.get(trackkey, "checkpointy")
checkpointx = parser.get(trackkey, "checkpointx")
checkpointy2 = parser.get(trackkey, "checkpointy2")
checkpointx2 = parser.get(trackkey, "checkpointx2")
checkpointy3 = parser.get(trackkey, "checkpointy3")
checkpointx3 = parser.get(trackkey, "checkpointx3")
parser.read("res/highscore.ini")
p1 = int(parser.get(trackkey, "1"))
p2 = int(parser.get(trackkey, "2"))
p3 = int(parser.get(trackkey, "3"))
p4 = int(parser.get(trackkey, "4"))
p5 = int(parser.get(trackkey, "5"))
p6 = int(parser.get(trackkey, "6"))
p7 = int(parser.get(trackkey, "7"))
p8 = int(parser.get(trackkey, "8"))
p9 = int(parser.get(trackkey, "9"))
p10 = parser.get(trackkey, "10")
p10 = int(p10)
p1 = randint(-1 , 99) + p1
p2 = randint(-1 , 99) + p2
p3 = randint(-1 , 99) + p3
p4 = randint(-1, 99) + p4
p5 = randint(-1 , 99) + p5
p6 = randint(-1, 99) + p6
p7 = randint(-1 , 99) + p7
p8 = randint(-1 , 99) + p8
p9 = randint(-1 , 99) + p9
p10 = randint(-1 , 99) + p10
pixcoloour = (0,0,0)
changetr = 0

#More Variables!!!!
mostnos = int(carnos)
nosleft = int(carnos)
aero = int(caraero) / 10
cartopspeed = int(carspeed) / 18 * aero
topspeed = int(carspeed) / 18 * aero
braking = int(carbrake) / 500 * aero
accel = int(caraccel) / 2100 * aero
handling = int(carhandling) / 30 * aero
righthandling = 360 - handling
mostnos2 = int(carnos2)
nosleft2 = int(carnos2)
aero2 = int(caraero2) / 10
cartopspeed2 = int(carspeed2) / 18 * aero2
topspeed2 = int(carspeed2) / 18 * aero2
braking2 = int(carbrake2) / 500 * aero2
accel2 = int(caraccel2) / 2100 * aero2
handling2 = int(carhandling2) / 30 * aero2
righthandling2 = 360 - handling2
curspeed = 0
startlinex = int(startx)
startliney = int(starty)
checky = int(checkpointy)
checkx = int(checkpointx)
checky2 = int(checkpointy2)
checkx2 = int(checkpointx2)
checky3 = int(checkpointy3)
checkx3 = int(checkpointx3)
checkplus40x = checkx + 80
checkminus40x = checkx - 80
checkplus40y = checky + 80
checkminus40y = checky - 80
checkplus40x2 = checkx2 + 80
checkminus40x2 = checkx2 - 80
checkplus40y2 = checky2 + 80
checkminus40y2 = checky2 - 80
checkplus40x3 = checkx3 + 80
checkminus40x3 = checkx3 - 80
checkplus40y3 = checky3 + 80
checkminus40y3 = checky3 - 80
if trackkey == "track8":
    checkplus40x = checkx + 120
    checkminus40x = checkx - 120
    checkplus40y = checky + 120
    checkminus40y = checky - 120
    checkplus40x2 = checkx2 + 120
    checkminus40x2 = checkx2 - 120
    checkplus40y2 = checky2 + 120
    checkminus40y2 = checky2 - 120
    checkplus40x3 = checkx3 + 200
    checkminus40x3 = checkx3 - 200
    checkplus40y3 = checky3 + 200
    checkminus40y3 = checky3 - 200
x = startliney
y = startlinex
y2 = startlinex - 10
x2 = startliney
if trackkey != "track4":
    if trackkey != "track3":
        if trackkey != "track6":
            if trackkey != "track7":
                x2 = startliney - 61
                y2 = startlinex
if trackkey == "track8":
    x2 = startliney + 55
startneg80x = startlinex - 80
if trackkey != "track4":
    if trackkey != "track3":
        if trackkey != "track6":
            if trackkey != "track7":
                startneg80x = startlinex
gol = fontbig.render("Go!", 10, white)
start80x = startlinex + 80
passstart = startliney + 10
rotater = 0
gear = 1
gear2 = 1
rotater2 = 0
carimage2 = pygame.transform.rotate(carimage, 0)
carimage4 = pygame.transform.rotate(carimage3, 0)
if trackkey == "track3" :
    carimage2 = pygame.transform.rotate(carimage, 90)
    rotater = 90
    carimage4 = pygame.transform.rotate(carimage3, 90)
    rotater2 = 90
    passstart = startlinex - 10
if trackkey == "track4" :
    carimage2 = pygame.transform.rotate(carimage, 270)
    rotater = 270
    carimage4 = pygame.transform.rotate(carimage3, 270)
    rotater2 = 270
    passstart = startlinex - 10
if trackkey == "track6" :
    carimage2 = pygame.transform.rotate(carimage, 270)
    rotater = 270
    carimage4 = pygame.transform.rotate(carimage3, 270)
    rotater2 = 270
    passstart = startlinex - 10
if trackkey == "track7" :
    carimage2 = pygame.transform.rotate(carimage, 270)
    rotater = 270
    carimage4 = pygame.transform.rotate(carimage3, 270)
    rotater2 = 270
    passstart = startlinex - 10
    y -= 30
    nosleft = 0
    nosleft2 = 0
if trackkey == "track5":
    cartopspeed2 = int(carspeed2) / 10 * aero2
    topspeed2 = int(carspeed2) / 10 * aero2
    cartopspeed = int(carspeed) / 10 * aero
    topspeed = int(carspeed) / 10 * aero
pos = 0
togo = 0
maxlaps = maxlap + 1
score = 0
pos2 = 0
togo2 = 0
maxlaps2 = maxlap + 1
score2 = 0
trackkey2 = trackkey
curspeed2 = 0
rot2 = 0
racestartbol = True

#Passoff to the postrace Python script
def sendtopost():
    global parser
    global carimage
    global currentcar
    global tracktotal
    global trackpath
    global track
    global trackname
    global clockspeed
    global score
    global place
    global trackkey
    global score2
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global p10
    global gol
    #send off the settings
    parser.read("res/options.ini")
    parser.set("options", "racefinsihed", "Yes")
    parser.set("options", "score", str(score))
    parser.set("options", "place", str(place))
    parser.set("options", "score2", str(score2))
    with open('res/options.ini', 'w') as configfile:
        parser.write(configfile)
    parser.read("res/highscore.ini")
    parser.set(trackkey, "p1", str(p1))
    parser.set(trackkey, "p2", str(p2))
    parser.set(trackkey, "p3", str(p3))
    parser.set(trackkey, "p4", str(p4))
    parser.set(trackkey, "p5", str(p5))
    parser.set(trackkey, "p6", str(p6))
    parser.set(trackkey, "p7", str(p7))
    parser.set(trackkey, "p8", str(p8))
    parser.set(trackkey, "p9", str(p9))
    parser.set(trackkey, "p10", str(p10))
    with open('res/highscore.ini', 'w') as configfile:
        parser.write(configfile)
    exec(open("prepostrace.py").read())

def racestart():
    global fontbig
    global trackimage
    global placel
    global scorel
    global nosl
    global lapl
    global curspeedl
    global playerl
    global shiftl
    global shiftl2
    global player2l
    global placel2
    global scorel2
    global nosl2
    global lapl2
    global curspeedl2
    global carimage4
    global carimage2
    global donel
    global trackkey
    global players
    global finished
    global shifting
    global shifting2
    global x
    global y
    global x2
    global y2
    three = fontbig.render("3", 10, white)
    two = fontbig.render("2", 10, white)
    one = fontbig.render("1", 10, white)
    time = 0
    for time in range(0,50):
        #Drawing and rendering
        screen.blit(trackimage, (0,0))
        screen.blit(placel, (10, 160))
        screen.blit(scorel, (10, 130))
        screen.blit(nosl, (10, 40))
        screen.blit(lapl, (10, 70))
        screen.blit(curspeedl, (10, 100))
        screen.blit(playerl, (10, 10))
        if trackkey == "track7":
            screen.blit(shiftl, (10, 190))
            if players == "2":
                screen.blit(shiftl2, (205, 190))
        if shifting == "Manual":
            screen.blit(shiftl, (10, 190))
        if shifting2 == "Manual":
            screen.blit(shiftl2, (205, 190))
        if players == "2":
            screen.blit(player2l, (205, 10))
            screen.blit(placel2, (205, 160))
            screen.blit(scorel2, (205, 130))
            screen.blit(nosl2, (205, 40))
            screen.blit(lapl2, (205, 70))
            screen.blit(curspeedl2, (205, 100))
            screen.blit(carimage4, (x2,y2))
        screen.blit(carimage2, (x,y))
        if finished:
            screen.blit(donel, (620, 7340))
        screen.blit(three, (600,315))
        pygame.display.flip()
        time +=1
    time = 0
    for time in range(0,50):
        #Drawing and rendering
        screen.blit(trackimage, (0,0))
        screen.blit(placel, (10, 160))
        screen.blit(scorel, (10, 130))
        screen.blit(nosl, (10, 40))
        screen.blit(lapl, (10, 70))
        screen.blit(curspeedl, (10, 100))
        screen.blit(playerl, (10, 10))
        if trackkey == "track7":
            screen.blit(shiftl, (10, 190))
            if players == "2":
                screen.blit(shiftl2, (205, 190))
        if shifting == "Manual":
            screen.blit(shiftl, (10, 190))
        if shifting2 == "Manual":
            screen.blit(shiftl2, (205, 190))
        if players == "2":
            screen.blit(player2l, (205, 10))
            screen.blit(placel2, (205, 160))
            screen.blit(scorel2, (205, 130))
            screen.blit(nosl2, (205, 40))
            screen.blit(lapl2, (205, 70))
            screen.blit(curspeedl2, (205, 100))
            screen.blit(carimage4, (x2,y2))
        screen.blit(carimage2, (x,y))
        if finished:
            screen.blit(donel, (620, 7340))
        screen.blit(two, (600,315))
        pygame.display.flip()
        time +=1
    time = 0
    for time in range(0,50):
        #Drawing and rendering
        screen.blit(trackimage, (0,0))
        screen.blit(placel, (10, 160))
        screen.blit(scorel, (10, 130))
        screen.blit(nosl, (10, 40))
        screen.blit(lapl, (10, 70))
        screen.blit(curspeedl, (10, 100))
        screen.blit(playerl, (10, 10))
        if trackkey == "track7":
            screen.blit(shiftl, (10, 190))
            if players == "2":
                screen.blit(shiftl2, (205, 190))
        if shifting == "Manual":
            screen.blit(shiftl, (10, 190))
        if shifting2 == "Manual":
            screen.blit(shiftl2, (205, 190))
        if players == "2":
            screen.blit(player2l, (205, 10))
            screen.blit(placel2, (205, 160))
            screen.blit(scorel2, (205, 130))
            screen.blit(nosl2, (205, 40))
            screen.blit(lapl2, (205, 70))
            screen.blit(curspeedl2, (205, 100))
            screen.blit(carimage4, (x2,y2))
        screen.blit(carimage2, (x,y))
        if finished:
            screen.blit(donel, (620, 7340))
        screen.blit(one, (600,315))
        pygame.display.flip()
        time +=1
    for time in range(0,10):
        #Drawing and rendering
        screen.blit(trackimage, (0,0))
        screen.blit(placel, (10, 160))
        screen.blit(scorel, (10, 130))
        screen.blit(nosl, (10, 40))
        screen.blit(lapl, (10, 70))
        screen.blit(curspeedl, (10, 100))
        screen.blit(playerl, (10, 10))
        if trackkey == "track7":
            screen.blit(shiftl, (10, 190))
            if players == "2":
                screen.blit(shiftl2, (205, 190))
        if shifting == "Manual":
            screen.blit(shiftl, (10, 190))
        if shifting2 == "Manual":
            screen.blit(shiftl2, (205, 190))
        if players == "2":
            screen.blit(player2l, (205, 10))
            screen.blit(placel2, (205, 160))
            screen.blit(scorel2, (205, 130))
            screen.blit(nosl2, (205, 40))
            screen.blit(lapl2, (205, 70))
            screen.blit(curspeedl2, (205, 100))
            screen.blit(carimage4, (x2,y2))
        screen.blit(carimage2, (x,y))
        if finished:
            screen.blit(donel, (620, 7340))
        screen.blit(gol, (600,315))
        pygame.display.flip()
        time +=1
        

#Exit Control
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        #Mainloop
        #Key Detection
        if players == "2":
            pressed = pygame.key.get_pressed()
            try:
                pixcoloour = trackpil[x2 + 30,y2 + 30]
            except IndexError:
                pixcoloour = trackpil[x2,y2]
            if not nosinuse2:
                if pixcoloour == (0, 0, 0, 255):
                    topspeed2 = int(carspeed2) / 18 * aero2
                    if trackkey == "track5":
                        cartopspeed2 = int(carspeed2) / 10 * aero2
                        topspeed2 = int(carspeed2) / 10 * aero2
                else:
                    if curspeed2 >= int(carspeed2) / 25 * aero2:
                        curspeed2 -= 0.4
                    else:
                        topspeed2 = int(carspeed2) / 25 * aero2
                if pixcoloour == (2, 2, 2, 255):
                    if trackkey == "track5":
                        cartopspeed2 = int(carspeed2) / 10 * aero2
                        topspeed2 = int(carspeed2) / 10 * aero2
                    topspeed2 = int(carspeed2) / 18 * aero2
            if atstart2:
                if y2 >= passstart:
                    atstart2 = False
                if trackkey2 == "track3":
                    if x2 <= passstart:
                        atstart2 = False
                if trackkey2 == "track4":
                    if x2 >= passstart:
                        atstart2 = False
                if trackkey2 == "track8":
                    if y2 <= passstart:
                        atstart2 = False
            if not atstart2:
                if not newlap2:
                    if not checklap2:
                        if not lapcheck2:
                            if y2 >= startneg80x:
                                if y2 <= start80x:
                                    if trackkey == "track3":
                                        if x2 >= startliney:
                                            score2 += 2000
                                            lapcount2 += 1
                                            newlap2 = True
                                            atstart2 = False
                                            checklap2 = True
                                            lapcheck2 = True
                                    if trackkey == "track4":
                                        if x2 >= startliney:
                                            score2 += 2000
                                            lapcount2 += 1
                                            newlap2 = True
                                            atstart2 = False
                                            checklap2 = True
                                            lapcheck2 = True
                                    if trackkey == "track6":
                                        if x2 >= startliney:
                                            score2 += 2000
                                            lapcount2 += 1
                                            newlap2 = True
                                            atstart2 = False
                                            checklap2 = True
                                            lapcheck2 = True
                                    if trackkey == "track8":
                                        if x2 >= startliney - 20:
                                            score2 += 2000
                                            lapcount2 += 1
                                            newlap2 = True
                                            atstart2 = False
                                            checklap2 = True
                                            lapcheck2 = True
                                    if trackkey != "track4":
                                        if trackkey != "track3":
                                            if trackkey != "track6":
                                                if trackkey != "track8":
                                                    if x2 <= startliney:
                                                        score2 += 2000
                                                        lapcount2 += 1
                                                        newlap2 = True
                                                        atstart2 = False
                                                        checklap2 = True
                                                        lapcheck2 = True
            if not atstart2:
                laptime += 1
                if y2 >= checkminus40y:
                    if y2 <= checkplus40y:
                        if x2 <= checkplus40x:
                            if x2 >= checkminus40x:
                                atstart2 = False
                                newlap2 = False
                                laptime = 0
                if y2 >= checkminus40y2:
                    if y2 <= checkplus40y2:
                        if x2 <= checkplus40x2:
                            if x2 >= checkminus40x2:
                                atstart2 = False
                                checklap2 = False
                                laptime = 0
                if y2 >= checkminus40y3:
                    if y2 <= checkplus40y3:
                        if x2 <= checkplus40x3:
                            if x2 >= checkminus40x3:
                                atstart2 = False
                                lapcheck2 = False
                                laptime = 0
            if pressed[pygame.K_ESCAPE]:
                pygame.QUIT
                quit()
            if pressed[pygame.K_w]:
                segment =  0
                segmentneg =  0
                segspeed = 0
                amount = 0
                rot2 = 0
                curspeed2 = curspeed2 + accel2
                lastdirection = Up
                if curspeed2 >= topspeed2:
                    curspeed2 = topspeed2
                if rotater2 <= 90:
                    xnow = x2
                    if rot2 <= 0:
                        amount = 0
                    if rot2 >= 0:
                        amount = rotater2 / 90
                    segspeed2 = amount * curspeed2
                    x2 = xnow - segspeed2
                if rotater2 >= 90:
                    if rotater2 <= 180:
                        xnow = x2
                        rot2 = 180 - rotater2
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        x2 = xnow - segspeed2
                if rotater2 >= 90.01:
                    if rotater2 <= 180:
                        ynow = y2
                        rot2 = rotater2 - 90
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        y2 = ynow + segspeed2
                if rotater2 >= 180:
                    if rotater2 <= 270:
                        ynow = y2
                        rot2 = 270 - rotater2
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        y2 = ynow + segspeed2
                if rotater2 >= 180:
                    if rotater2 <= 270:
                        xnow = x2
                        rot2 = rotater2 - 180
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        x2 = xnow + segspeed2
                if rotater2 >= 270:
                    if rotater2 <= 360:
                        xnow = x2
                        rot2 = rotater2 - 270
                        rot3 = -90 + rot2
                        if rot3 >= 0:
                            amount = 1
                        if rot3 <= 0:
                            amount = rot3 / -90
                        segspeed2 = amount * curspeed2
                        x2 = xnow + segspeed2
                if rotater2 >= 270:
                    if rotater2 <= 360:
                        ynow = y2
                        rot2 = rotater2 - 270
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        y2 = ynow - segspeed2
                if rotater2 <= 89.9:
                    ynow = y2
                    rot2 = -90 + rotater2
                    if rot2 >= 0:
                        amount = 1
                    if rot2 <= 0:
                        amount = rot2 / -90
                    segspeed2 = amount * curspeed2
                    y2 = ynow - segspeed2
            if pressed[pygame.K_a]:
                lastdirection = Left
                if curspeed2 >= topspeed2:
                    curspeed2 = topspeed2
                if curspeed2 >= 0.1:
                    rotater2 += handling2
                if not pressed [pygame.K_w]:
                    if rotater2 <= 90:
                        xnow = x2
                        if rot2 <= 0:
                            amount = 0
                        if rot2 >= 0:
                            amount = rotater2 / 90
                        segspeed2 = amount * curspeed2
                        x2 = xnow - segspeed2
                    if rotater2 >= 90:
                        if rotater2 <= 180:
                            xnow = x2
                            rot2 = 180 - rotater2
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            x2 = xnow - segspeed2
                    if rotater2 >= 90.01:
                        if rotater2 <= 180:
                            ynow = y2
                            rot2 = rotater2 - 90
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            y2 = ynow + segspeed2
                    if rotater2 >= 180:
                        if rotater2 <= 270:
                            ynow = y2
                            rot2 = 270 - rotater2
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            y2 = ynow + segspeed2
                    if rotater2 >= 180:
                        if rotater2 <= 270:
                            xnow = x2
                            rot2 = rotater2 - 180
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            x2 = xnow + segspeed2
                    if rotater2 >= 270:
                        if rotater2 <= 359.9:
                            xnow = x2
                            rot2 = rotater2 - 270
                            rot3 = -90 + rot2
                            if rot3 >= 0:
                                amount = 1
                            if rot3 <= 0:
                                amount = rot3 / -90
                            segspeed2 = amount * curspeed2
                            x2 = xnow + segspeed2
                    if rotater2 >= 270:
                        if rotater2 <= 360:
                            ynow = y2
                            rot2 = rotater2 - 270
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            y2 = ynow - segspeed2
                    if rotater2 <= 89.9:
                        ynow = y2
                        rot2 = -90 + rotater2
                        if rot2 >= 0:
                            amount = 1
                        if rot2 <= 0:
                            amount = rot2 / -90
                        segspeed2 = amount * curspeed2
                        y2 = ynow - segspeed2
                if rotater2 >= 360:
                    rotater2 = 0
                if rotater2 <= 0:
                    rotater2 = 0
                carimage4 = pygame.transform.rotate(carimage3, rotater2)
                if pressed[pygame.K_w]:
                    lastdirection = LeftUp
                if pressed[pygame.K_s]:
                    lastdirection = LeftDown
            if pressed[pygame.K_d]:
                lastdirection = Right
                if not pressed [pygame.K_w]:
                    if rotater2 <= 90:
                        xnow = x2
                        if rot2 <= 0:
                            amount = 0
                        if rot2 >= 0:
                            amount = rotater2 / 90
                        segspeed2 = amount * curspeed2
                        x2 = xnow - segspeed2
                    if rotater2 >= 90:
                        if rotater2 <= 180:
                            xnow = x2
                            rot2 = 180 - rotater2
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            x2 = xnow - segspeed2
                    if rotater2 >= 90.01:
                        if rotater2 <= 180:
                            ynow = y2
                            rot2 = rotater2 - 90
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            y2 = ynow + segspeed2
                    if rotater2 >= 180:
                        if rotater2 <= 270:
                            ynow = y2
                            rot2 = 270 - rotater2
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            y2 = ynow + segspeed2
                    if rotater2 >= 180:
                        if rotater2 <= 270:
                            xnow = x2
                            rot2 = rotater2 - 180
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            x2 = xnow + segspeed2
                    if rotater2 >= 270:
                        if rotater2 <= 360:
                            xnow = x2
                            rot2 = rotater2 - 270
                            rot3 = -90 + rot2
                            if rot3 >= 0:
                                amount = 1
                            if rot3 <= 0:
                                amount = rot3 / -90
                            segspeed2 = amount * curspeed2
                            x2 = xnow + segspeed2
                    if rotater2 >= 270:
                        if rotater2 <= 360:
                            ynow = y2
                            rot2 = rotater2 - 270
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            y2 = ynow - segspeed2
                    if rotater2 <= 89.9:
                        ynow = y2
                        rot2 = -90 + rotater2
                        if rot2 >= 0:
                            amount = 1
                        if rot2 <= 0:
                            amount = rot2 / -90
                        segspeed2 = amount * curspeed2
                        y2 = ynow - segspeed2
                if curspeed2 >= topspeed2:
                    curspeed2 = topspeed2
                if curspeed2 >= 0.1:
                    rotater2 -= handling2
                    if rotater2 >= 360:
                        rotater2 = 0
                    if rotater2 <= 0:
                        rotater2 = 360
                carimage4 = pygame.transform.rotate(carimage3, rotater2)
                if pressed[pygame.K_w]:
                    lastdirection = RightUp
                if pressed[pygame.K_s]:
                    lastdirection = RightDown
            #Getting that nos working!!!
            if pressed[pygame.K_q]:
                if nosleft2 >= 1:
                    nosleft2 -= 1
                    topspeed2 += 0.2
                    nosinuse2 = True
                    if trackkey == "track5":
                        topspeed2 += 0.2
                else:
                    nosinuse2 = False
                    if topspeed2 >= cartopspeed2:
                        topspeed2 -= 0.1
                    if not nosinuse2:
                        if nosleft2 <= mostnos2:
                            nosleft2 += 0.1
                            if trackkey == "track8":
                                nosleft2 += 0.2
            else:
                nosinuse2 = False
                if topspeed2 >= cartopspeed2:
                    topspeed2 -= 0.1
                if not nosinuse2:
                    if nosleft2 <= mostnos2:
                        nosleft2 += 0.1
            if pressed[pygame.K_s]:
                curspeed2 = curspeed2 - braking
                if curspeed2 >= -1.6:
                    curspeed2 = curspeed2 - 0.1
                else:
                    curspeed2 = -1.5
                if rotater2 <= 90:
                    xnow = x2
                    if rot2 <= 0:
                        amount = 0
                    if rot2 >= 0:
                        amount = rotater2 / 90
                    segspeed2 = amount * curspeed2
                    x2 = xnow - segspeed2
                if rotater2 >= 90:
                    if rotater2 <= 180:
                        xnow = x2
                        rot2 = 180 - rotater2
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        x2 = xnow - segspeed2
                if rotater2 >= 90.01:
                    if rotater2 <= 180:
                        ynow = y2
                        rot2 = rotater2 - 90
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        y2 = ynow + segspeed2
                if rotater2 >= 180:
                    if rotater2 <= 270:
                        ynow = y2
                        rot2 = 270 - rotater2
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        y2 = ynow + segspeed2
                if rotater2 >= 180:
                    if rotater2 <= 270:
                        xnow = x2
                        rot2 = rotater2 - 180
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        x2 = xnow + segspeed2
                if rotater2 >= 270:
                    if rotater2 <= 360:
                        xnow = x2
                        rot2 = rotater2 - 270
                        rot3 = -90 + rot2
                        if rot3 >= 0:
                            amount = 1
                        if rot3 <= 0:
                            amount = rot3 / -90
                        segspeed2 = amount * curspeed2
                        x2 = xnow + segspeed2
                if rotater2 >= 270:
                    if rotater2 <= 360:
                        ynow = y2
                        rot2 = rotater2 - 270
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        y2 = ynow - segspeed2
                if rotater2 <= 89.9:
                    ynow = y2
                    rot2 = -90 + rotater2
                    if rot2 >= 0:
                        amount = 1
                    if rot2 <= 0:
                        amount = rot2 / -90
                    segspeed2 = amount * curspeed2
                    y2 = ynow - segspeed2
            if not pressed[pygame.K_q]:
                nosinuse2 = False
                if topspeed2 >= cartopspeed2:
                    topspeed2 -= 0.1
                if not nosinuse2:
                    if nosleft2 <= mostnos:
                        nosleft2 += 0.0
            if not pressed[pygame.K_d]:
                if not pressed[pygame.K_a]:
                    if not pressed[pygame.K_s]:
                        if not pressed[pygame.K_w]:
                            if not pressed[pygame.K_q]:
                                if curspeed2 >= 0.19:
                                    curspeed2 = curspeed2 - 0.1
                                if curspeed2 <= -0.1:
                                    curspeed2 = curspeed2 + 0.1
                                if curspeed2 >= -0.1:
                                    if curspeed2 <= 0.19:
                                        curspeed2 = 0
                                if rotater2 <= 90:
                                    xnow = x2
                                    if rot2 <= 0:
                                        amount = 0
                                    if rot2 >= 0:
                                        amount = rotater2 / 90
                                    segspeed2 = amount * curspeed2
                                    x2 = xnow - segspeed2
                                if rotater2 >= 90:
                                    if rotater2 <= 180:
                                        xnow = x2
                                        rot2 = 180 - rotater2
                                        amount = rot2 / 90
                                        segspeed2 = amount * curspeed2
                                        x2 = xnow - segspeed2
                                if rotater2 >= 90.01:
                                    if rotater2 <= 180:
                                        ynow = y2
                                        rot2 = rotater2 - 90
                                        amount = rot2 / 90
                                        segspeed2 = amount * curspeed2

                                        y2 = ynow + segspeed2
                                if rotater2 >= 180:
                                    if rotater2 <= 270:
                                        ynow = y2
                                        rot2 = 270 - rotater2
                                        amount = rot2 / 90
                                        segspeed2 = amount * curspeed2
                                        y2 = ynow + segspeed2
                                if rotater2 >= 180:
                                    if rotater2 <= 270:
                                        xnow = x2
                                        rot2 = rotater2 - 180
                                        amount = rot2 / 90
                                        segspeed2 = amount * curspeed2
                                        x2 = xnow + segspeed2
                                if rotater2 >= 270:
                                    if rotater2 <= 360:
                                        xnow = x2
                                        rot2 = rotater2 - 270
                                        rot3 = -90 + rot2
                                        if rot3 >= 0:
                                            amount = 1
                                        if rot3 <= 0:
                                            amount = rot3 / -90
                                        segspeed2 = amount * curspeed2
                                        x2 = xnow + segspeed2
                                if rotater2 >= 270:
                                    if rotater2 <= 360:
                                        ynow = y2
                                        rot2 = rotater2 - 270
                                        amount = rot2 / 90
                                        segspeed2 = amount * curspeed2
                                        y2 = ynow - segspeed2
                                if rotater2 <= 89.9:
                                    ynow = y2
                                    rot2 = -90 + rotater2
                                    if rot2 >= 0:
                                        amount = 1
                                    if rot2 <= 0:
                                        amount = rot2 / -90
                                    segspeed2 = amount * curspeed2
                                    y2 = ynow - segspeed2
            #movement
            #Collision/OOB detection
            if x2 >=1270:
                x2 = 1268
            if x2 <= -1:
                x2 = 2
            if y2 >= 710:
                y2 = 708
            if y2 <= -1:
                y2 = 2
            score2 -= 1
        pressed = pygame.key.get_pressed()
        try:
            pixcoloour = trackpil[x + 30,y + 30]
        except IndexError:
            pixcoloour = trackpil[x,y]
        if not nosinuse:
            if pixcoloour == (0, 0, 0, 255):
                topspeed = int(carspeed) / 18 * aero
                if trackkey == "track5":
                    cartopspeed = int(carspeed) / 10 * aero
                    topspeed = int(carspeed) / 10 * aero
            else:
                if curspeed >= int(carspeed) / 25 * aero:
                    curspeed -= 0.3
                else:
                    topspeed = int(carspeed) / 25 * aero
            if pixcoloour == (2, 2, 2, 255):
                topspeed = int(carspeed) / 18 * aero
                if trackkey == "track5":
                    cartopspeed = int(carspeed) / 10 * aero
                    topspeed = int(carspeed) / 10 * aero
        if atstart:
            if y >= passstart:
                atstart = False
            if trackkey == "track3":
                if x <= passstart:
                    atstart = False
            if trackkey2 == "track4":
                if x2 >= passstart:
                    atstart2 = False
            if trackkey2 == "track7":
                    atstart = False
            if trackkey == "track8":
                if y <= passstart:
                    atstart = False
        if not atstart:
            if not newlap:
                if not checklap:
                    if not lapcheck:
                        if y >= startneg80x:
                            if y <= start80x:
                                if trackkey == "track3":
                                    if x >= startliney:
                                        score += 2000
                                        lapcount += 1
                                        newlap = True
                                        atstart = False
                                        checklap = True
                                        lapcheck = True
                                if trackkey == "track4":
                                    if x >= startliney:
                                        score += 2000
                                        lapcount += 1
                                        newlap = True
                                        atstart = False
                                        checklap = True
                                        lapcheck = True
                                if trackkey == "track6":
                                    if x >= startliney:
                                        score += 2000
                                        lapcount += 1
                                        newlap = True
                                        atstart = False
                                        checklap = True
                                        lapcheck = True
                                if trackkey == "track8":
                                    if x >= startliney - 20:
                                        score += 2000
                                        lapcount += 1
                                        newlap = True
                                        atstart = False
                                        checklap = True
                                        lapcheck = True
                                if trackkey != "track4":
                                    if trackkey != "track3":
                                        if trackkey != "track6":
                                            if trackkey != "track8":
                                                if x <= startliney:
                                                    score += 2000
                                                    lapcount += 1
                                                    newlap = True
                                                    atstart = False
                                                    checklap = True
                                                    lapcheck = True
        if not atstart:
            laptime += 1
            if y >= checkminus40y:
                if y <= checkplus40y:
                    if x <= checkplus40x:
                        if x >= checkminus40x:
                            atstart = False
                            newlap = False
                            laptime = 0
            if y >= checkminus40y2:
                if y <= checkplus40y2:
                    if x <= checkplus40x2:
                        if x >= checkminus40x2:
                            atstart = False
                            checklap = False
                            laptime = 0
            if y >= checkminus40y3:
                if y <= checkplus40y3:
                    if x <= checkplus40x3:
                        if x >= checkminus40x3:
                            atstart = False
                            lapcheck = False
                            laptime = 0
        if pressed[pygame.K_ESCAPE]:
            pygame.QUIT
            quit()
        if pressed[pygame.K_UP]:
            segment =  0
            segmentneg =  0
            segspeed = 0
            amount = 0
            rot2 = 0
            curspeed = curspeed + accel
            lastdirection = Up
            if curspeed >= topspeed:
                curspeed = topspeed
            if rotater <= 90:
                xnow = x
                if rot2 <= 0:
                    amount = 0
                if rot2 >= 0:
                    amount = rotater / 90
                segspeed = amount * curspeed
                x = xnow - segspeed
            if rotater >= 90:
                if rotater <= 180:
                    xnow = x
                    rot2 = 180 - rotater
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    x = xnow - segspeed
            if rotater >= 90.01:
                if rotater <= 180:
                    ynow = y
                    rot2 = rotater - 90
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    y = ynow + segspeed
            if rotater >= 180:
                if rotater <= 270:
                    ynow = y
                    rot2 = 270 - rotater
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    y = ynow + segspeed
            if rotater >= 180:
                if rotater <= 270:
                    xnow = x
                    rot2 = rotater - 180
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    x = xnow + segspeed
            if rotater >= 270:
                if rotater <= 360:
                    xnow = x
                    rot2 = rotater - 270
                    rot3 = -90 + rot2
                    if rot3 >= 0:
                        amount = 1
                    if rot3 <= 0:
                        amount = rot3 / -90
                    segspeed = amount * curspeed
                    x = xnow + segspeed
            if rotater >= 270:
                if rotater <= 360:
                    ynow = y
                    rot2 = rotater - 270
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    y = ynow - segspeed
            if rotater <= 89.9:
                ynow = y
                rot2 = -90 + rotater
                if rot2 >= 0:
                    amount = 1
                if rot2 <= 0:
                    amount = rot2 / -90
                segspeed = amount * curspeed
                y = ynow - segspeed
        if pressed[pygame.K_LEFT]:
            lastdirection = Left
            if curspeed >= topspeed:
                curspeed = topspeed
            if not pressed [pygame.K_UP]:
                if rotater <= 90:
                    xnow = x
                    if rot2 <= 0:
                        amount = 0
                    if rot2 >= 0:
                        amount = rotater / 90
                    segspeed = amount * curspeed
                    x = xnow - segspeed
                if rotater >= 90:
                    if rotater <= 180:
                        xnow = x
                        rot2 = 180 - rotater
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        x = xnow - segspeed
                if rotater >= 90.01:
                    if rotater <= 180:
                        ynow = y
                        rot2 = rotater - 90
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        y = ynow + segspeed
                if rotater >= 180:
                    if rotater <= 270:
                        ynow = y
                        rot2 = 270 - rotater
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        y = ynow + segspeed
                if rotater >= 180:
                    if rotater <= 270:
                        xnow = x
                        rot2 = rotater - 180
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        x = xnow + segspeed
                if rotater >= 270:
                    if rotater <= 359.9:
                        xnow = x
                        rot2 = rotater - 270
                        rot3 = -90 + rot2
                        if rot3 >= 0:
                            amount = 1
                        if rot3 <= 0:
                            amount = rot3 / -90
                        segspeed = amount * curspeed
                        x = xnow + segspeed
                if rotater >= 270:
                    if rotater <= 360:
                        ynow = y
                        rot2 = rotater - 270
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        y = ynow - segspeed
                if rotater <= 89.9:
                    ynow = y
                    rot2 = -90 + rotater
                    if rot2 >= 0:
                        amount = 1
                    if rot2 <= 0:
                        amount = rot2 / -90
                    segspeed = amount * curspeed
                    y = ynow - segspeed
            if curspeed >= 0.1:
                rotater += handling
            if rotater >= 360:
                rotater = 0
            if rotater <= 0:
                rotater = 0
            carimage2 = pygame.transform.rotate(carimage, rotater)
            if pressed[pygame.K_UP]:
                lastdirection = LeftUp
            if pressed[pygame.K_DOWN]:
                lastdirection = LeftDown
        if pressed[pygame.K_RIGHT]:
            lastdirection = Right
            if not pressed [pygame.K_UP]:
                segment =  0
                segmentneg =  0
                segspeed = 0
                amount = 0
                rot2 = 0
                if rotater <= 90:
                    xnow = x
                    if rot2 <= 0:
                        amount = 0
                    if rot2 >= 0:
                        amount = rotater / 90
                    segspeed = amount * curspeed
                    x = xnow - segspeed
                if rotater >= 90:
                    if rotater <= 180:
                        xnow = x
                        rot2 = 180 - rotater
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        x = xnow - segspeed
                if rotater >= 90.01:
                    if rotater <= 180:
                        ynow = y
                        rot2 = rotater - 90
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        y = ynow + segspeed
                if rotater >= 180:
                    if rotater <= 270:
                        ynow = y
                        rot2 = 270 - rotater
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        y = ynow + segspeed
                if rotater >= 180:
                    if rotater <= 270:
                        xnow = x
                        rot2 = rotater - 180
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        x = xnow + segspeed
                if rotater >= 270:
                    if rotater <= 360:
                        xnow = x
                        rot2 = rotater - 270
                        rot3 = -90 + rot2
                        if rot3 >= 0:
                            amount = 1
                        if rot3 <= 0:
                            amount = rot3 / -90
                        segspeed = amount * curspeed
                        x = xnow + segspeed
                if rotater >= 270:
                    if rotater <= 360:
                        ynow = y
                        rot2 = rotater - 270
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        y = ynow - segspeed
                if rotater <= 89.9:
                    ynow = y
                    rot2 = -90 + rotater
                    if rot2 >= 0:
                        amount = 1
                    if rot2 <= 0:
                        amount = rot2 / -90
                    segspeed = amount * curspeed
                    y = ynow - segspeed
            if curspeed >= topspeed:
                curspeed = topspeed
            if curspeed >= 0.1:
                rotater -= handling
            if rotater >= 360:
                rotater = 0
            if rotater <= 0:
                rotater = 360
            carimage2 = pygame.transform.rotate(carimage, rotater)
            if pressed[pygame.K_UP]:
                lastdirection = RightUp
            if pressed[pygame.K_DOWN]:
                lastdirection = RightDown
        #Getting that nos working!!!
        if pressed[pygame.K_SPACE]:
            if nosleft >= 1:
                nosleft -= 1
                topspeed += 0.2
                nosinuse = True
                if trackkey == "track5":
                    topspeed += 0.2
            else:
               nosinuse = False
               if trackkey == "track5":
                   nosleft += 0.2
               if topspeed >= cartopspeed:
                   topspeed -= 0.1
               if not nosinuse:
                   if nosleft <= mostnos:
                       nosleft += 0.1
                       if trackkey == "track8":
                           nosleft += 0.2
        if pressed[pygame.K_DOWN]:
            curspeed = curspeed - braking
            if curspeed >= -1.6:
                curspeed = curspeed - 0.1
            else:
                curspeed = -1.5
            if rotater <= 90:
                xnow = x
                if rot2 <= 0:
                    amount = 0
                if rot2 >= 0:
                    amount = rotater / 90
                segspeed = amount * curspeed
                x = xnow - segspeed
            if rotater >= 90:
                if rotater <= 180:
                    xnow = x
                    rot2 = 180 - rotater
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    x = xnow - segspeed
            if rotater >= 90.01:
                if rotater <= 180:
                    ynow = y
                    rot2 = rotater - 90
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    y = ynow + segspeed
            if rotater >= 180:
                if rotater <= 270:
                    ynow = y
                    rot2 = 270 - rotater
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    y = ynow + segspeed
            if rotater >= 180:
                if rotater <= 270:
                    xnow = x
                    rot2 = rotater - 180
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    x = xnow + segspeed
            if rotater >= 270:
                if rotater <= 360:
                    xnow = x
                    rot2 = rotater - 270
                    rot3 = -90 + rot2
                    if rot3 >= 0:
                        amount = 1
                    if rot3 <= 0:
                        amount = rot3 / -90
                    segspeed = amount * curspeed
                    x = xnow + segspeed
            if rotater >= 270:
                if rotater <= 360:
                    ynow = y
                    rot2 = rotater - 270
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    y = ynow - segspeed
            if rotater <= 89.9:
                ynow = y
                rot2 = -90 + rotater
                if rot2 >= 0:
                    amount = 1
                if rot2 <= 0:
                    amount = rot2 / -90
                segspeed = amount * curspeed
                y = ynow - segspeed
        if not pressed[pygame.K_SPACE]:
            nosinuse = False
            if topspeed >= cartopspeed:
                topspeed -= 0.1
            if not nosinuse:
                if nosleft <= mostnos:
                    nosleft += 0.1
        if not pressed[pygame.K_RIGHT]:
            if not pressed[pygame.K_LEFT]:
                if not pressed[pygame.K_DOWN]:
                    if not pressed[pygame.K_UP]:
                        if not pressed[pygame.K_SPACE]:
                            if curspeed >= 0.19:
                                curspeed = curspeed - 0.1
                            if curspeed <= -0.1:
                                curspeed = curspeed + 0.1
                            if curspeed >= -0.1:
                                if curspeed <= 0.19:
                                    curspeed = 0
                            segment =  0
                            segmentneg =  0
                            segspeed = 0
                            amount = 0
                            rot2 = 0
                            if rotater <= 90:
                                xnow = x
                                if rot2 <= 0:
                                    amount = 0
                                if rot2 >= 0:
                                    amount = rotater / 90
                                segspeed = amount * curspeed
                                x = xnow - segspeed
                            if rotater >= 90:
                                if rotater <= 180:
                                    xnow = x
                                    rot2 = 180 - rotater
                                    amount = rot2 / 90
                                    segspeed = amount * curspeed
                                    x = xnow - segspeed
                            if rotater >= 90.01:
                                if rotater <= 180:
                                    ynow = y
                                    rot2 = rotater - 90
                                    amount = rot2 / 90
                                    segspeed = amount * curspeed

                                    y = ynow + segspeed
                            if rotater >= 180:
                                if rotater <= 270:
                                    ynow = y
                                    rot2 = 270 - rotater
                                    amount = rot2 / 90
                                    segspeed = amount * curspeed
                                    y = ynow + segspeed
                            if rotater >= 180:
                                if rotater <= 270:
                                    xnow = x
                                    rot2 = rotater - 180
                                    amount = rot2 / 90
                                    segspeed = amount * curspeed
                                    x = xnow + segspeed
                            if rotater >= 270:
                                if rotater <= 360:
                                    xnow = x
                                    rot2 = rotater - 270
                                    rot3 = -90 + rot2
                                    if rot3 >= 0:
                                        amount = 1
                                    if rot3 <= 0:
                                        amount = rot3 / -90
                                    segspeed = amount * curspeed
                                    x = xnow + segspeed
                            if rotater >= 270:
                                if rotater <= 360:
                                    ynow = y
                                    rot2 = rotater - 270
                                    amount = rot2 / 90
                                    segspeed = amount * curspeed
                                    y = ynow - segspeed
                            if rotater <= 89.9:
                                ynow = y
                                rot2 = -90 + rotater
                                if rot2 >= 0:
                                    amount = 1
                                if rot2 <= 0:
                                    amount = rot2 / -90
                                segspeed = amount * curspeed
                                y = ynow - segspeed
        #movement
        #Collision/OOB detection
        if x >=1270:
            x = 1268
        if x <= -1:
            x = 2
        if y >= 710:
            y = 708
        if y <= -1:
            y = 2
        if x2 >=1270:
            x2 = 1268
        if x2 <= -1:
            x2 = 2
        if y2 >= 710:
            y2 = 708
        if y2 <= -1:
            y2 = 2
        score -= 1
        if players == "2":
            if lapcount2 >= maxlaps + 1:
                lapcount2 -= 1
                score2 -= 2000
            if lapcount2 >= maxlaps:
                score2 += 1
            if lapcount >= maxlaps + 1:
                lapcount -= 1
                score -= 2000
            if lapcount >= maxlaps:
                score += 1
        lapstogo = maxlaps - lapcount
        lapstogo2 = maxlaps - lapcount2
        if players == "2":
            if lapstogo2 <= lapstogo:
                lapstogo = lapstogo2
            else:
                lapstogo = lapstogo
        if lapstogo == 0:
            lapstogo = 1
        if lapstogo2 == 0:
            lapstogo2 = 1
        #Getting the placing
        if score <= p10 / lapstogo:
            place = 11
            togo = p10 - score
        if score >= p10 / lapstogo:
            place = 10
            togo = p10 - score
        if score >= p9 / lapstogo:
            place = 9
            togo = p10 - score
        if score >= p8 / lapstogo:
            place = 8
            togo = p10 - score
        if score >= p7 / lapstogo:
            place = 7
            togo = p10 - score
        if score >= p6 / lapstogo:
            place = 6
            togo = p10 - score
        if score >= p5 / lapstogo:
            place = 5
            togo = p10 - score
        if score >= p4 / lapstogo:
            place = 4
            togo = p10 - score
        if score >= p3 / lapstogo:
            place = 3
            togo = p10 - score
        if score >= p2 / lapstogo:
            place = 2
            togo = p10 - score
        if score >= p1 / lapstogo:
            place = 1
            togo = p10 - score
        if players == "2":
            if score2 <= p10 / lapstogo:
                place2 = 11
                togo = p10 - score
            if score2 >= p10 / lapstogo:
                place2 = 10
                togo = p10 - score
            if score2 >= p9 / lapstogo:
                place2 = 9
                togo = p10 - score
            if score2 >= p8 / lapstogo:
                place2 = 8
                togo = p10 - score
            if score2 >= p7 / lapstogo:
                place2 = 7
                togo = p10 - score
            if score2 >= p6 / lapstogo:
                place2 = 6
                togo = p10 - score
            if score2 >= p5 / lapstogo:
                place2 = 5
                togo = p10 - score
            if score2 >= p4 / lapstogo:
                place2 = 4
                togo = p10 - score
            if score2 >= p3 / lapstogo:
                place2 = 3
                togo = p10 - score
            if score2 >= p2 / lapstogo:
                place2 = 2
                togo = p10 - score
            if score2 >= p1 / lapstogo:
                place2 = 1
                togo = p10 - score
            if lapstogo >= 2:
                if place2 == place:
                    if score >= score2:
                        place2 += 1
                    if score2 >= score:
                        place += 1
        #Finishing!
        if players == "1":
            if lapcount >= maxlaps:
                #Passoff scprit goes here
                finished = True
                sendtopost()
        if players == "3":
            if lapcount >= maxlaps:
                #Passoff scprit goes here
                finished = True
                sendtopost()        
        if players == "2":
            if lapcount >= maxlaps:
                if lapcount2 >= maxlaps:
                    #Passoff script goes here
                    finished = True
                    sendtopost()
        #Setting Up the labels
        laplabel = lap + str(lapcount) + "/" + str(maxlap)
        if lapcount >= maxlaps:
            laplabel = "Done!"
        lapl = font.render(laplabel, 10 ,black)
        nosleftround = round(nosleft, 1)
        noslabel = "Nos Left: " + str(nosleftround)
        nosl = font.render(noslabel, 30, black)
        scorelabel = "Score: " + str(round(score, 1))
        scorel = font.render(scorelabel, 30 , black)
        speedlabel = curspeed * 41
        currentlabel = "Speed: " + str(round(speedlabel, 2)) + " Km/h"
        curspeedl = font.render(currentlabel, 30, black)
        placelabel = "Place: " + str(place)
        placel = font.render(placelabel, 30, black)
        playerl = font.render(playername + ":", 30, black)
        if trackkey == "track2":
            placel = font.render(placelabel, 30, white)
            playerl = font.render(playername + ":", 30, white)
            curspeedl = font.render(currentlabel, 30, white)
            scorel = font.render(scorelabel, 30 , white)
            nosl = font.render(noslabel, 30, white)
            lapl = font.render(laplabel, 10 ,white)
        if trackkey == "track5":
            placel = font.render(placelabel, 30, white)
            playerl = font.render(playername + ":", 30, white)
            curspeedl = font.render(currentlabel, 30, white)
            scorel = font.render(scorelabel, 30 , white)
            nosl = font.render(noslabel, 30, white)
            lapl = font.render(laplabel, 10 ,white)
        if players == "2":
            laplabel = str(lapcount2) + "/" + str(maxlap)
            if lapcount2 >= maxlaps:
                laplabel = "Done!"
            lapl2 = font.render(laplabel, 10 ,black)
            nosleftround = round(nosleft2, 1)
            noslabel = str(nosleftround)
            nosl2 = font.render(noslabel, 30, black)
            scorelabel = str(round(score2, 1))
            scorel2 = font.render(scorelabel, 30 , black)
            speedlabel = curspeed2 * 41
            currentlabel = str(round(speedlabel, 2)) + " Km/h"
            curspeedl2 = font.render(currentlabel, 30, black)
            placelabel = str(place2)
            placel2 = font.render(placelabel, 30, black)
            player2l = font.render("Player 2:", 30, black)
            if trackkey == "track2":
                lapl2 = font.render(laplabel, 10 ,white)
                nosl2 = font.render(noslabel, 30, white)
                player2l = font.render("Player 2:", 30, white)
                placel2 = font.render(placelabel, 30, white)
                curspeedl2 = font.render(currentlabel, 30, white)
                scorel2 = font.render(scorelabel, 30 , white)
            if trackkey == "track5":
                lapl2 = font.render(laplabel, 10 ,white)
                nosl2 = font.render(noslabel, 30, white)
                player2l = font.render("Player 2:", 30, white)
                placel2 = font.render(placelabel, 30, white)
                curspeedl2 = font.render(currentlabel, 30, white)
                scorel2 = font.render(scorelabel, 30 , white)
            if trackkey == "track8":
                placel2 = font.render(placelabel, 30, white)
                curspeedl2 = font.render(currentlabel, 30, white)
                scorel2 = font.render(scorelabel, 30 , white)
        donelabel = "Finsihed!  ANd more because this is cool!"
        donel = font.render(donelabel, 30, black)
        if trackkey == "track4":
            changetr -= 1
            if trackpath == "res/Camelback Pass (1).png":
                if changetr <= 0:
                    trackimage = pygame.image.load("res/Camelback Pass (2).png")
                    trackpath = "res/Camelback Pass (2).png"
                    changetr = 6
            if trackpath == "res/Camelback Pass (2).png":
                if changetr <= 0:
                    trackimage = pygame.image.load("res/Camelback Pass (3).png")
                    trackpath = "res/Camelback Pass (3).png"
                    changetr = 6
            if trackpath == "res/Camelback Pass (3).png":
                if changetr <= 0:
                    trackimage = pygame.image.load("res/Camelback Pass (1).png")
                    trackpath = "res/Camelback Pass (1).png"
                    changetr = 6
        if trackkey == "track6":
            changetr -= 1
            if trackpath == "res/Not An Animal This Time (1).png":
                if changetr <= 0:
                    trackimage = pygame.image.load("res/Not An Animal This Time (2).png")
                    trackpath = "res/Not An Animal This Time (2).png"
                    changetr = 10
            if trackpath == "res/Not An Animal This Time (2).png":
                if changetr <= 0:
                    trackimage = pygame.image.load("res/Not An Animal This Time (1).png")
                    trackpath = "res/Not An Animal This Time (1).png"
                    changetr = 10
        if trackkey == "track7":
            if x >= 1230:
                x = 10
            if x2 >= 1230:
                x2 = 10
            shifttext = ""
            shifttext2 = ""
            if enginecounter >= clockspeed * 6:
                curspeed -= 0.5
                if curspeed <= 0:
                    curspeed = 0
            if enginecounter2 >= clockspeed * 6:
                curspeed2 -= 0.5
                if curspeed2 >= 0:
                    curspeed2 = 0
            if gear == 1:
                if curspeed >= topspeed / 4:
                    shifttext = "Shift Now!"
                    curspeed = topspeed  / 4 + 0.1
                    enginecounter +=  2
                    if pressed[pygame.K_RSHIFT]:
                        gear +=1
                        enginecounter = 0
            if gear == 2:
                if curspeed >= topspeed / 2.5:
                    shifttext = "Shift Now!"
                    curspeed = topspeed / 2.5 + 0.1
                    enginecounter +=  1
                    if pressed[pygame.K_RSHIFT]:
                        gear +=1
                        enginecounter = 0
            if gear == 3:
                if curspeed >= topspeed / 2:
                    curspeed = topspeed / 2 + 0.1
                    shifttext = "Shift Now!"
                    enginecounter +=  1
                    if pressed[pygame.K_RSHIFT]:
                        gear +=1
                        enginecounter = 0
            if gear == 4:
                if curspeed >= topspeed / 1.5:
                    curspeed = topspeed / 1.5 + 0.1
                    shifttext = "Shift Now!"
                    enginecounter +=  1
                    if pressed[pygame.K_RSHIFT]:
                        gear +=1
                        enginecounter = 0
            if gear == 5:
                if curspeed >= topspeed / 1.3:
                    curspeed = topspeed / 1.3 + 0.1
                    shifttext = "Shift Now!"
                    enginecounter +=  1
                    if pressed[pygame.K_RSHIFT]:
                        gear +=1
                        enginecounter = 0
            if gear2 == 1:
                if curspeed2 >= topspeed2 / 4:
                    curspeed2 = topspeed2  / 4 + 0.1
                    shifttext2 = "Shift Now!"
                    enginecounter2 +=  1
                    if pressed[pygame.K_e]:
                        gear2 +=1
                        enginecounter2 = 0
            if gear2 == 2:
                if curspeed2 >= topspeed2 / 2.5:
                    curspeed2 = topspeed2 / 2.5 + 0.1
                    shifttext2 = "Shift Now!"
                    enginecounter2 +=  1
                    if pressed[pygame.K_e]:
                        gear2 +=1
                        enginecounter2 = 0
            if gear2 == 3:
                if curspeed2 >= topspeed2 / 2:
                    curspeed2 = topspeed2 / 2 + 0.1
                    shifttext2 = "Shift Now!"
                    enginecounter2 +=  1

                    if pressed[pygame.K_e]:
                        gear2 +=1
                        enginecounter2 = 0
            if gear2 == 4:
                if curspeed2 >= topspeed2 / 1.5:
                    curspeed2 = topspeed2 / 1.5 + 0.1
                    shifttext2 = "Shift Now!"
                    enginecounter2 +=  1
                    if pressed[pygame.K_e]:
                        gear2 +=1
                        enginecounter2 = 0
            if gear2 == 5:
                if curspeed2 >= topspeed2 / 1.3:
                    curspeed2 = topspeed2 / 1.3 + 0.1
                    shifttext2 = "Shift Now!"
                    enginecounter2 +=  1
                    if pressed[pygame.K_e]:
                        gear2 +=1
                        enginecounter2 = 0
            shiftl = font.render(shifttext, 30, black)
            shiftl2 = font.render(shifttext2, 30, black)
        if shifting == "Manual":
            shifttext = ""
            shifttext2 = ""
            if enginecounter >= clockspeed * 6:
                curspeed -= 0.5
                if curspeed <= 0:
                    curspeed = 0
            if enginecounter2 >= clockspeed * 6:
                curspeed2 -= 0.5
                if curspeed2 >= 0:
                    curspeed2 = 0
            if gear == 1:
                if curspeed >= topspeed / 4:
                    shifttext = "Shift Now!"
                    curspeed = topspeed  / 4 + 0.1
                    enginecounter +=  2
                    if pressed[pygame.K_RSHIFT]:
                        gear += 1
                        enginecounter = 0
            if gear == 2:
                if curspeed >= topspeed / 2.5:
                    shifttext = "Shift Now!"
                    curspeed = topspeed / 2.5 + 0.1
                    enginecounter +=  1
                    if pressed[pygame.K_RSHIFT]:
                            gear +=1
                            enginecounter = 0
                if curspeed <= topspeed / 2.7:
                    if enginecounter >= 5:
                        gear -= 1
            if gear == 3:
                if curspeed >= topspeed / 2:
                    curspeed = topspeed / 2 + 0.1
                    shifttext = "Shift Now!"
                    enginecounter +=  1
                    if pressed[pygame.K_RSHIFT]:
                            gear +=1
                            enginecounter = 0
                if curspeed <= topspeed / 2.3:
                    if enginecounter >= 5:
                        gear -= 1
            if gear == 4:
                if curspeed >= topspeed / 1.5:
                    curspeed = topspeed / 1.5 + 0.1
                    shifttext = "Shift Now!"
                    enginecounter +=  1
                    if pressed[pygame.K_RSHIFT]:
                            gear +=1
                            enginecounter = 0
                if curspeed <= topspeed / 1.7:
                    if enginecounter >= 5:
                        gear -= 1
            if gear == 5:
                if curspeed >= topspeed / 1.3:
                    curspeed = topspeed / 1.3 + 0.1
                    shifttext = "Shift Now!"
                    enginecounter +=  1
                    if pressed[pygame.K_RSHIFT]:
                            gear +=1
                            enginecounter = 0
                if curspeed <= topspeed / 1.5:
                    if enginecounter >= 5:
                        gear -= 1
        if shifting2 == "Manual":
            if gear2 == 1:
                if curspeed2 >= topspeed2 / 4:
                    curspeed2 = topspeed2  / 4 + 0.1
                    shifttext2 = "Shift Now!"
                    enginecounter2 +=  1
                    if pressed[pygame.K_e]:
                        gear2 +=1
                        enginecounter2 = 0
            if gear2 == 2:
                if curspeed2 >= topspeed2 / 2.5:
                    curspeed2 = topspeed2 / 2.5 + 0.1
                    shifttext2 = "Shift Now!"
                    enginecounter2 +=  1
                    if pressed[pygame.K_e]:
                            gear2 +=1
                            enginecounter2 = 0
                if curspeed2 <= topspeed2 / 2.8:
                    if enginecounter2 >= 5:
                        gear2 -= 1
            if gear2 == 3:
                if curspeed2 >= topspeed2 / 2:
                    curspeed2 = topspeed2 / 2 + 0.1
                    shifttext2 = "Shift Now!"
                    enginecounter2 +=  1
                    if pressed[pygame.K_e]:
                            gear2 +=1
                            enginecounter2 = 0
                if curspeed2 <= topspeed2 / 2.2:
                    if enginecounter2 >= 5:
                        gear2 -= 1
            if gear2 == 4:
                if curspeed2 >= topspeed2 / 1.5:
                    curspeed2 = topspeed2 / 1.5 + 0.1
                    shifttext2 = "Shift Now!"
                    enginecounter2 +=  1
                    if pressed[pygame.K_e]:
                            gear2 +=1
                            enginecounter2 = 0
                if curspeed2 <= topspeed2 / 1.7:
                    if enginecounter2 >= 5:
                        gear2 -= 1
            if gear2 == 5:
                if curspeed2 >= topspeed2 / 1.3:
                    curspeed2 = topspeed2 / 1.3 + 0.1
                    shifttext2 = "Shift Now!"
                    enginecounter2 +=  1
                    if pressed[pygame.K_e]:
                        gear2 +=1
                        enginecounter2 = 0
                if curspeed2 <= topspeed2 / 1.5:
                    if enginecounter2 >= 50:
                        gear2 -= 1
            shiftl = font.render(shifttext, 30, black)
            shiftl2 = font.render(shifttext2, 30, black)
        try:
            shiftl = font.render(shifttext, 30, black)
            shiftl2 = font.render(shifttext2, 30, black)
            if trackkey == "track5":
                shiftl = font.render(shifttext, 30, white)
                shiftl2 = font.render(shifttext2, 30, white)
            if trackkey == "track2":
                shiftl = font.render(shifttext, 30, white)
                shiftl2 = font.render(shifttext2, 30, white)
        except NameError:
            pass
        if showstartcountdown =="True":
            if racestartbol:
                racestartbol = False
                racestart()
        #Drawing and rendering
        screen.blit(trackimage, (0,0))
        screen.blit(placel, (10, 160))
        screen.blit(scorel, (10, 130))
        screen.blit(nosl, (10, 40))
        screen.blit(lapl, (10, 70))
        screen.blit(curspeedl, (10, 100))
        screen.blit(playerl, (10, 10))
        if trackkey == "track7":
            screen.blit(shiftl, (10, 190))
            screen.blit(shiftl2, (205, 190))
        if shifting == "Manual":
            screen.blit(shiftl, (10, 190))
        if shifting2 == "Manual":
            screen.blit(shiftl2, (205, 190))
        if players == "2":
            screen.blit(player2l, (205, 10))
            screen.blit(placel2, (205, 160))
            screen.blit(scorel2, (205, 130))
            screen.blit(nosl2, (205, 40))
            screen.blit(lapl2, (205, 70))
            if trackkey != "track8":
                screen.blit(curspeedl2, (205, 100))
            if trackkey == "track8":
                screen.blit(curspeedl2, (215, 100))
            screen.blit(carimage4, (x2,y2))
        screen.blit(carimage2, (x,y))
        if finished:
            screen.blit(donel, (620, 7340))
        #ANND, GO!
        pygame.display.flip()
        clock.tick(clockspeed)
