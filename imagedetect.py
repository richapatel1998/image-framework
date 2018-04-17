
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def Frame_Name(img, name_on_image):
width, height = img.size
font = ImageFont.truetype("arial.ttf",40)
text = "Sample Text"
tcolor = (255,255,0)
text_pos = (100,100)

img = Image.open("Ninja.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 30)
draw.text((225, 350), "hello", font=font, fill = (255,255,25))
del draw

img.show("Ninja_new.jpg")






# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import os.path
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'family.png')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 1)
# Show the image data in the first subplot
ax.imshow(img)
ax.imshow(img, interpolation='none') # Override the default
ax.set_xlim(25, 575)
ax.set_ylim(400, 25)


font = ImageFont.truetype("arial.ttf",40)
text = "Sample Text"
tcolor = (255,255,0)
text_pos = (100,100)

img = Image.open('family.png')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 30)
draw.text((225, 350), "hello", font=font, fill = (255,255,25))
del draw

fig.show()
