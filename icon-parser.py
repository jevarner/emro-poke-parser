from PIL import Image

imageName = 'pokemonicons-sheet.png'
#40w 30h
with Image.open(imageName) as im:
    left = 0
    upper = 0
    right = 40
    lower = 30

    id = 1

    while lower <= 3990:
        im_crop = im.crop((left, upper, right, lower))

        im_crop.save(f'icons/{id}.png')

        id += 1

        if (right + 40 <= 480):
            left += 40
            right += 40
        else:
            left = 0
            upper += 30
            right = 40
            lower += 30