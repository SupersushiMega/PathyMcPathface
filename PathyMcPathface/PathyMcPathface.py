import turtle
import random
import math
#import matplotlib.pyplot as plt

ObjLib = {          #Object coordinate storage
    #objX: (center_X(centX), center_y(centY), X_modifier(modX), Y_modifier(modY), edgeXpositive(Xpos), edgeXnegative(Xneg), edgeYpositive(Xpos), edgeYnegative(Yneg)
}

path_count = 0

angles = [0, 90, 180, 270]

width = 1000
height = 750

turtle.screensize(width,width)
lab = turtle.Screen() #The surroundings                      #Screensetup
lab.colormode(255)
lab.setup(width=1.0, height=1.0, startx=None, starty=None)

steve = turtle.Turtle() #Obstacle drawer
steve.speed(0) #Obstacle drawer speed
Mc = turtle.Turtle() #PathyMcPathface
Mc.penup()
Mc.goto(550, -375)  #PathyMcPathface goes to safety
Mc.speed(0)
Mc.pendown()
food = turtle.Turtle() #PathyMcPathface wants food
food.speed(1)
food.color(0, 200, 0)

pathcounttarget = 10
ObjCount = 0                                                #Variable defenition
foodstate = 0
retry = 0
steps = 0
pathx = round(Mc.xcor())
pathy = round(Mc.ycor())

while(ObjCount != 40):                                       #Obstacle Object generation
    ObjCount = ObjCount + 1
    centX = round(random.uniform((width / 2), -width / 2))
    centY = round(random.uniform((height / 2), -height / 2))
    modX = round(random.uniform(50, 10))
    modY = round(random.uniform(50, 10))
    ObjLib[str(ObjCount)] = [centX, centY, modX, modY, centX + modX, centX - modX, centY + modY, centY - modY]

print (ObjLib)

for x in ObjLib:
    rgbpoint = -1
    rgb=[0, 0, 0]
    for col in rgb:
        rgbpoint = rgbpoint + 1
        rgb[rgbpoint] = round(random.uniform(255, 0))              #randomized obstaclecolor
    print(rgb)
    steve.pencolor(rgb[0], rgb[1], rgb[2])

    coords=ObjLib[x] #List out off Library
    Xpos = coords[4]
    Xneg = coords[5]
    Ypos = coords[6]
    Yneg = coords[7]
    steve.penup()
    steve.setpos (Xpos, Ypos)
    steve.begin_fill()
    steve.pendown()
    steve.setpos (Xneg, Ypos)
    steve.setpos (Xneg, Yneg)
    steve.setpos (Xpos, Yneg)
    steve.setpos (Xpos, Ypos)
    steve.end_fill()
    steve.penup

foodstate = 0
while(1):
    while(foodstate == 0):
        steps = 0
        exception_count = 0
        stepsize = 1
        food.clear()
        coordbuffer = []
        foodx = round(random.uniform(-width/2,width/2),0)
        foody = round(random.uniform(-height/2,height/2),0)
        food.setpos(foodx,foody)
        for x in ObjLib:
            coords = ObjLib[x]  # List out off Library
            Xpos = coords[4]
            Xneg = coords[5]
            Ypos = coords[6]
            Yneg = coords[7]
            if((foodx <= Xpos and foodx >= Xneg) and (foody <= Ypos and foody >= Yneg)):
                retry = 1

        if(retry == 0):
            foodstate = 1
        else:
            retry = 0
    checksize = 0
    paths = []
    curhead = Mc.heading()
    while(foodstate == 1):
        steps = steps + 1
        if(steps > 1000000):
            foodstate = 0
            print("steps to high")
        exception_occurred = 0
        dist_0 = math.sqrt((foodx - (pathx + 1))**2 + (foody - pathy)**2)
        dist_90 = math.sqrt((foodx - pathx)**2 + (foody - (pathy + 1))**2)
        dist_180 = math.sqrt((foodx - (pathx - 1))**2 + (foody - pathy)**2)
        dist_270 = math.sqrt((foodx - pathx)**2 + (foody - (pathy - 1))**2)
        curdist = math.sqrt((foodx - pathx)**2 + (foody - pathy )**2)
        useList =[]
        useLib = {
            "use0": [1, dist_0, "0"],
            "use90": [1, dist_90, "90"],
            "use180": [1, dist_180, "180"],
            "use270": [1, dist_270, "270"]
        }
        for x in ObjLib:
            checksize = 0
            while(checksize <= stepsize):
                checksize = checksize + 1
                coords = ObjLib[x]  # List out off Library
                Xpos = coords[4]
                Xneg = coords[5]
                Ypos = coords[6]
                Yneg = coords[7]
        #=======================================================================================================================
                if(not((pathx + checksize <= Xpos and pathx + checksize >= Xneg) and (pathy <= Ypos and pathy >= Yneg)) and curhead != 180 and useLib["use0"][0] == 1):
                    useLib["use0"] = [1, dist_0, "0"]
                else:
                    useLib["use0"] = [0, dist_0, "0"]
        #=======================================================================================================================
                if (not((pathx <= Xpos and pathx >= Xneg) and (pathy + checksize <= Ypos and pathy + checksize >= Yneg)) and curhead != 270 and useLib["use90"][0] == 1):
                    useLib["use90"] = [1, dist_90, "90"]
                else:
                    useLib["use90"] = [0, dist_90, "90"]
        #=======================================================================================================================
                if (not((pathx - checksize <= Xpos and pathx - checksize >= Xneg) and (pathy <= Ypos and pathy >= Yneg)) and curhead != 0 and useLib["use180"][0] == 1):
                    useLib["use180"] = [1, dist_180, "180"]
                else:
                    useLib["use180"] = [0, dist_180, "180"]
        #=======================================================================================================================
                if (not((pathx <= Xpos and pathx >= Xneg) and (pathy - checksize <= Ypos and pathy - checksize >= Yneg)) and curhead != 90 and useLib["use270"][0] == 1):
                    useLib["use270"] = [1, dist_270, "270"]
                else:
                    useLib["use270"] = [0, dist_270, "270"]
        for x in useLib:
            if(useLib[x][0] == 1):
                useList.append(useLib[x])
        useList.sort()
        decicion_randomiser = round(random.uniform(0, 27))
        if (len(paths) != pathcounttarget):
            try:
                if(int(useList[0][2]) == 0 or decicion_randomiser == 5 and useLib["use0"][0] == 1):
                    pathx = pathx + stepsize
                    curhead = 0

                if(int(useList[0][2]) == 90 or decicion_randomiser == 9 and useLib["use90"][0] == 1):
                    pathy = pathy + stepsize
                    curhead = 90

                if(int(useList[0][2]) == 180 or decicion_randomiser == 18 and useLib["use180"][0] == 1):
                    pathx = pathx - stepsize
                    curhead = 180

                if(int(useList[0][2]) == 270 or decicion_randomiser == 21 and useLib["use270"][0] == 1):
                    pathy = pathy - stepsize
                    curhead = 270
            except:
                pathx = round(Mc.xcor())
                pathy = round(Mc.ycor())
                exception_count = exception_count + 1
                exception_occurred = 1
                if(exception_count + 1 > pathcounttarget):
                    foodstate = 0
                    Mc.penup()
                    Mc.goto(550, -375)  # PathyMcPathface goes to safety
                    Mc.speed(0)
                    Mc.pendown()
            for x in coordbuffer:
                if ([round(pathx), round(pathy)] == x):
                    if(decicion_randomiser != 5 and decicion_randomiser != 9 and decicion_randomiser != 18 and decicion_randomiser != 21):
                        stepsize = stepsize + 1
                        equalfound = 1
                elif(equalfound !=1):
                    stepsize = 1
            equalfound = 0
            coordbuffer.append([round(pathx), round(pathy)])
        if(round(pathx) == foodx and round(pathy) == foody):
            path_count = path_count + 1
            paths.append(coordbuffer)
            coordbuffer = []
            pathx = round(Mc.xcor())
            pathy = round(Mc.ycor())
            if(pathcounttarget <= path_count):
                coordbuffer = []
                path_count = 0
                paths.sort(key=len)
                for x in paths[0]:
                    X = x[0]
                    Y = x[1]
                    Mc.goto(X, Y)
                foodstate = 0
                pathx = round(Mc.xcor())
                pathy = round(Mc.ycor())
        elif(exception_occurred == 1):
            coordbuffer = []
            pathx = round(Mc.xcor())
            pathy = round(Mc.ycor())