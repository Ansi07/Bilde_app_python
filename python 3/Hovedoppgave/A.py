from PIL import Image
import pilgram

def filter():
#henter bilde
    img = Image.open('sample.jpg')
#setter en filter og lagrer bilde med et annet navn
    filter_img = pilgram._1977(img)
    return filter_img
#kaller funksjonen
filtered_image = filter()
#lagrer bilde med navnet i parantensen
filtered_image.save('sample-filter-bilde.jpg')