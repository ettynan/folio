import sys, os
from PIL import Image, ImageFilter

# grab 1st and 2nd arg
path = sys.argv[1]
new_folder = sys.argv[2]


# check if new/exists; create if not there
if not os.path.exists(new_folder):
    os.makedirs(new_folder)


# loop through pokedex folder, convert images, save to the new folder
for filename in os.listdir(path):
    name = os.path.splitext(filename)[0]
    img = Image.open(f'{path}{filename}')

    img.save(f'{new_folder}/{name}.png', 'png')

print('complete')