from PIL import Image
import pilgram

def blackandwhite():
#henter bilde
    img = Image.open('sample.jpg')
 #setter en filter og lagrer bilde med et annet navn
    filter_image = pilgram.willow(img)
    return filter_image
filtered_image = blackandwhite()
filtered_image.save('bilde-B&W.jpg')
