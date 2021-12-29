from PIL import Image
import sys
import os


base_directory = sys.argv[1]
new_directory = sys.argv[2]

os.makedirs(new_directory, exist_ok=True)

for file in os.listdir(base_directory):
    image = Image.open(base_directory + '/' + file)
    image.save(new_directory + "/" + file.split(".")[0] + ".png", 'png')