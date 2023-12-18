from PIL import Image, ImageOps

def apply_sepia_tone():
    # Åpne bildet
    image = Image.open('sample.jpg')

    # Konverter bildet til sepia tone ved å bruke ImageOps.colorize
    sepia_image = ImageOps.colorize(image.convert("L"), "#704214", "#C0A080")
    return sepia_image
new_image = apply_sepia_tone()
new_image.save('image-sepia.jpg')
# Lagre det endrede bildet