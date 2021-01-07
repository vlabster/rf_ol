from random import randint, choice
import os
from PIL import Image, ImageFont, ImageDraw

data = ["name", "surname", "burthDate", "Country", "Obl", "date1", "date2", "data3", "country2", "obl2", "categories"]


img1 = Image.open('sample.png')
img2 = Image.open('photos/1.png')

img1.paste(img2, (70, 170))
img1.save('result.png')

finImg = ImageDraw.Draw(img1)


# set font
font = ImageFont.truetype('fonts/20051.ttf', size=50)

# draw text
finImg.text(
    (500, 150),
    'Name',
    font=font,
    fill='#1C0606'
)

img1.save('result.png')

img1.paste(img2, (70, 170))








