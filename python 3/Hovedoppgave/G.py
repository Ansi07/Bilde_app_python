from PIL import Image, ImageOps #importerer pil og Imageops
#henter bilde og ramme, resizer til rammen og deretter setter rammen bak bilde og lagrer med nytt navn.
def apply_polaroid_frame(): 
    img = Image.open('sample.jpg')
    img2 = Image.open('polaroid.png')
    img1 = ImageOps.fit(img, size=(760, 760))
    img2.paste(img1, box=(64, 64))
    img2.save("polaroid-bilde.png")
apply_polaroid_frame()

    