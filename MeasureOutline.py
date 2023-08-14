import pickle, sys, math
from PIL import Image, ImageDraw

outline = pickle.load(open('output.pkl', 'rb'))
outline.pop(0)
outline.pop(0)
outline.pop(0)
radius = (int)(sys.argv[1])
points = [outline[0]]
for i in range(len(outline)) : 
    for point in outline: 
        if math.dist(point, points[0]) == 1 and points.count(point) == 0 :
            points.insert(0, point)

mask = Image.open("mask-small.png")
draw = ImageDraw.Draw(mask)
# draw.polygon(points, None, (255,0,0), 10)
for point in points:
    mask.paste((0, 0, 255, 255), (point[0], point[1], point[0] + 5, point[1] + 5))
mask.show()