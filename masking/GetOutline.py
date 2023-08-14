from PIL import Image
import pickle, sys, math
# mask = Image.open("mask.png")

WHITE = (255,255,255,255)
BLACK = (0,0,0,255)

# outline = []
# for x in range(mask.size[0]) :
#     for y in range(mask.size[1]) :
#         if mask.getpixel((x,y)) == WHITE :
#             # Only checking orthagonal neighbours
#             if mask.getpixel((x-1,y-1))  == WHITE and mask.getpixel((x-1,y))  == WHITE and mask.getpixel((x-1,y+1))  == WHITE and mask.getpixel((x+1,y))  == WHITE and mask.getpixel((x+1,y-1)) == WHITE and mask.getpixel((x+1,y+1))  == WHITE and mask.getpixel((x,y+1))  == WHITE and mask.getpixel((x,y-1))  == WHITE :
#                 outline.append((x,y))

# for pixel in outline :
#     mask.putpixel(pixel, BLACK)

outline = Image.open("mask.png")
path = []
def countWhiteNeighbours(x,y) :
    neighbours = [outline.getpixel((x-1, y-1)) , outline.getpixel((x-1, y))  , outline.getpixel((x-1, y+1))  , outline.getpixel((x, y+1))  , outline.getpixel((x, y-1)) , outline.getpixel((x+1, y+1))  , outline.getpixel((x+1, y))  , outline.getpixel((x+1, y-1))]    
    return neighbours.count(WHITE) 
def countBlackNeighbours(x,y) :
    neighbours = [outline.getpixel((x-1, y-1)) , outline.getpixel((x-1, y))  , outline.getpixel((x-1, y+1))  , outline.getpixel((x, y+1))  , outline.getpixel((x, y-1)) , outline.getpixel((x+1, y+1))  , outline.getpixel((x+1, y))  , outline.getpixel((x+1, y-1))]    
    return neighbours.count(BLACK) 
def getNeighbours(x,y) :
    return [(x-1, y-1), (x-1, y)  , (x-1, y+1)  , (x, y+1)  , (x, y-1) , (x+1, y+1)  , (x+1, y)  , (x+1, y-1)]
def isOutOfBounds(point):
    return point[0] > outline.size[0] or point[1] > outline.size[1]
def removeBlackPixels(path) :
    retpath = []
    for pixel in path :
        point = (pixel[0], pixel[1])
        if not isOutOfBounds(point) and outline.getpixel(point) == WHITE :

            retpath.append(pixel)
    return retpath
def removeDuplicates(path) :
   for element in path :
       if path.count(element) > 1 :
           path.remove
endpoint = (384, 234)
startpoint = (384, 236)
path = [startpoint]



currentpoint = path[0]
index = 1
while path[len(path)-1] != endpoint:
    for neighbour in getNeighbours(path[len(path)-1][0], path[len(path)-1][1]) :
        if path.count(neighbour) == 0 and outline.getpixel(neighbour) == WHITE and countBlackNeighbours(neighbour[0], neighbour[1]) > 0 :
            path.append(neighbour)
            break

for pixel in path :
    outline.putpixel((pixel[0], pixel[1]), (255,0,0))
outline.show()
# # file_name = 'output.pkl'
# # with open(file_name, 'wb') as file:
# #     pickle.dump(outline, file)
# #     print(f'Object successfully saved to "{file_name}"')
