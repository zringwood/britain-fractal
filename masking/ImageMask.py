from PIL import Image, ImageEnhance


im = Image.open('britain-huge.jpg')
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(10)
im.show()
# #Pixels that are more green than blue become white, otherwise they become black. 
# for x in range(im.size[0]) :
#     for y in range(im.size[1]) :
#         if im.getpixel((x,y))[1] > im.getpixel((x,y))[2] and im.getpixel((x,y))[2] < 40: 
#             im.putpixel((x,y), (255,255,255,255))
#         else :
#             im.putpixel((x,y), (0,0,0,255))
# #This image still needs some manual markup. 
# im.save("mask-huge.png")