from PIL import Image, ImageDraw
import math
import sys
import numpy as np
mask = Image.open("mask-massive.png")
# def estimateCoastline(radius) :
#The length of our "measuring stick", per the coastline paradox. 
radius = (int)(sys.argv[1])
startpoint = (1760, 1064)
    # startpoint = (8, 1225)
allPoints = [startpoint]

BLACK = (0,0,0, 255)
WHITE = (255, 255, 255, 255)
ONE_DEGREE = (2*math.pi) / 360
MAX_POINTS = 2571

def rotate(point, center, delta_radians) :
    ROTATION = [[math.cos(delta_radians), -math.sin(delta_radians)], [math.sin(delta_radians), math.cos(delta_radians)]]
    point_origin = [point[0] - center[0], point[1] - center[1]]
    point_rotated = np.matmul(point_origin, ROTATION)
    return (point_rotated[0] + center[0], point_rotated[1] + center[1])
def toInteger(point):
    return (math.trunc(point[0]), math.trunc(point[1]))
savePoints = []
def isOutOfBounds(point):
    return point[0] > mask.size[0] or point[1] > mask.size[1]
currentpoint = (startpoint[0] - radius, startpoint[1])


    # allPoints needs two points in the array for the loop to work properly. 
initialcolor = mask.getpixel(currentpoint) 
    
while mask.getpixel(toInteger(currentpoint)) == initialcolor :
    currentpoint = rotate(currentpoint, allPoints[len(allPoints)-1], ONE_DEGREE)
    savePoints.append(currentpoint)
    
allPoints.append((currentpoint)) 

while math.dist(currentpoint, startpoint) > radius :  
    currentpoint = rotate(allPoints[len(allPoints)-2], allPoints[len(allPoints)-1], ONE_DEGREE*180)
    #We're searching for the edge. Therefore, we're always looking for the OPPOSITE color of the initial point.
    if not isOutOfBounds(currentpoint) :
        initialcolor = mask.getpixel(currentpoint) 
    else :
        initialcolor = BLACK
    direction = 1 if initialcolor == WHITE else -1
    
    while isOutOfBounds(currentpoint) or mask.getpixel(toInteger(currentpoint)) == initialcolor :
        currentpoint = rotate(currentpoint, allPoints[len(allPoints)-1], ONE_DEGREE*direction)
        if not isOutOfBounds(currentpoint):
            savePoints.append(currentpoint)
       
        
    allPoints.append((currentpoint))
    if len(allPoints) > MAX_POINTS:
        break

print ((len(allPoints)-1)*30 + math.dist(allPoints[0], allPoints[1]))

# for i in range(len(savePoints)):
#     point = toInteger(savePoints[i])
#     mask.paste((255, 0, 0, 255), (point[0], point[1], point[0] + 1, point[1] + 1))

draw = ImageDraw.Draw(mask)
draw.polygon(allPoints, None, (255,0,0), 10)
for i in range(len(allPoints)):
    point = toInteger(allPoints[i])
    mask.paste((0, 0, 255, 255), (point[0], point[1], point[0] + 5, point[1] + 5))
mask.show()