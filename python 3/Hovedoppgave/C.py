from PIL import Image
print("1: roter høyre 90 grader")
print("2: roter venstre 90 grader")
print("3: roter 180 grader")
user_input = int(input("Skriv in handling:"))

#----------------------------------------------------------------

def rotate_image(user_input):
    # Henter bilde
    img = Image.open('sample.jpg')

    # Utfør rotasjon basert på brukerens valg
    if user_input == 1:
        # Roterer bilde 90 grader til høyre
        image_rotate = img.rotate(-90)
        output_filename = 'bilde-rotert-høyre.jpg'
        
    elif user_input == 2:
        # Roterer bilde 90 grader til venstre
        image_rotate = img.rotate(90)
        output_filename = 'bilde-rotert.venstre.jpg'
        
    elif user_input == 3:
        # Roterer bilde 180 grader
        image_rotate = img.rotate(180)
        output_filename = 'bilde-rotert-180.jpg'
        
    else:
        # Ugyldig valg
        print("Ugyldig valg. Vennligst velg mellom 1, 2 eller 3.")
        return 

    # Lagrer det roterte bildet
    image_rotate.save(output_filename)

# kaller funksjonen
rotate_image(user_input)
