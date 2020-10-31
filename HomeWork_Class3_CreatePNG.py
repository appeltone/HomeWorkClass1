# challenge image create using pillow
import os
from os import path

from PIL import Image, ImageFont, ImageDraw

img_path = "E:\\temp\\words.png"

my_image = Image.new('RGBA', (800, 800), 'blue')
str = "Appel was here"
fnt = ImageFont.truetype("C:\\Windows\\Fonts\\tahoma.ttf", 75)
w, h = fnt.getsize(str)  # get the Width and Higth of the text and the fonts size
drawing = ImageDraw.Draw(my_image)  # draw image
# write text to image (location, text, font, font color)
drawing.text(((800-w)/2, (800-h)/2), str, font=fnt, fill=(255, 245, 0))  # location of the text, image size - text&font size / 2 :-)

# remove the image if it exists
if (path.exists(img_path)):
    os.remove(img_path)

my_image.save(img_path)
