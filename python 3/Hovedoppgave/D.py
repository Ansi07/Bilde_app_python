from PIL import Image

img = Image.open('sample.jpg')

def image_resize():
    if img.width < 1080 or img.height < 1350:
        new_width = max(img.width, 1080)
        new_height = max(img.height, 1350)
    # Resize bildet
        resize_img = img.resize((new_width, new_height))
        return resize_img
    else:
        print("Bildet er allerede stort nok")
resized_img = image_resize()
resized_img.save('bilde-resized.jpg')
