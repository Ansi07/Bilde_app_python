import requests
from PIL import Image

img = Image.open('sample.jpg')
print("1: bruke egen bilde fra nettet")
print("2: bruke lagret bildet")
img.show('sample.jpg')
option = int(input("velg 1 eller 2: "))

#---------------------------------------------

if option == 1:
    
    image_url = input("lim inn bildeadressen til bilde du vil redigere: ")
        
        # Hent bildet fra nettet
    response = requests.get(image_url)
    
    filnavn = "sample.jpg"

        # Lagre bildet lokalt
    filbane = ("./" + filnavn)
    with open(filbane, "wb") as f:
     f.write(response.content)
     
    #gir en meny på bruker kan velge mellom 
    print("Velg en handling:")
    print("1: Instagram filter")    
    print("2: black and white filter")
    print("3: rotere bilde")
    print("4: resize bilde")
    print("5: apply Sepia tone ")
    print("6: polaroidebilde ")
    user_input = int(input("Skriv in handling: ")) 

#kjører kode fra en annen fil basert på brukerens input
    if user_input == 1:
        from A import filter
        
    if user_input == 2:
        from B import blackandwhite

    if user_input == 3:
        from C import rotate_image

    if user_input == 4:
        from D import image_resize

    if user_input == 5:
        from F import apply_sepia_tone
        
    if user_input == 6:
        from G import apply_polaroid_frame

#---------------------------------------------------------------------

if option == 2:
    #gir en meny på bruker kan velge mellom 
    print("Velg en handling:")
    print("1: Instagram filter")    
    print("2: black and white filter")
    print("3: rotere bilde")
    print("4: resize bilde")
    print("5: apply Sepia tone ")
    print("6: polaroidebilde ")

    user_input = int(input("Skriv in handling: "))

#kjører kode fra en annen fil basert på brukerens input
    if user_input == 1:
        from A import filter
        
    if user_input == 2:
        from B import blackandwhite

    if user_input == 3:
        from C import rotate_image

    if user_input == 4:
        from D import image_resize

    if user_input == 5:
        from F import apply_sepia_tone
        
    if user_input == 6:
        from G import apply_polaroid_frame

