from PIL import Image
mask = Image.open("mask.png")

WHITE = (255,255,255,255)
BLACK = (0,0,0,255)
markedfordeletion = []
for x in range(mask.size[0]) :
    for y in range(mask.size[1]) :
        if mask.getpixel((x,y)) == WHITE :
            if mask.getpixel((x-1,y-1)) == WHITE and mask.getpixel((x-1,y))  == WHITE and mask.getpixel((x-1,y+1))  == WHITE and mask.getpixel((x+1,y))  == WHITE and mask.getpixel((x+1,y-1)) == WHITE and mask.getpixel((x+1,y+1))  == WHITE and mask.getpixel((x,y+1))  == WHITE and mask.getpixel((x,y-1))  == WHITE :
                markedfordeletion.append((x,y))
for pixel in markedfordeletion :
    mask.putpixel(pixel, BLACK)
mask.show()
