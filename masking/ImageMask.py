from PIL import Image


im = Image.open('britain-massive.jpg')

#Pixels that are more green than blue become white, otherwise they become black. 
for x in range(im.size[0]) :
    for y in range(im.size[1]) :
        if im.getpixel((x,y))[1] > im.getpixel((x,y))[2] : 
            im.putpixel((x,y), (255,255,255,255))
        else :
            im.putpixel((x,y), (0,0,0,255))
#This image still needs some manual markup. 
im.save("mask-massive.png")