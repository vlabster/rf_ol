from random import randint
# data = ["name", "surname", "burthDate", "Country", "Obl", "date1", "date2", "data3", "country2", "obl2", "categories"]
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








canvas = Image.new(mode = "RGB", size = (900,600))

### working with the main canvas backround

bg = Image.open('bgs/0.jpg')

def random_bg_crop():
    left = randint(0,200)
    upper = randint(0,200)
    right = left + 900
    bottom = upper + 600
    return((left, upper, right, bottom))

newbg = bg.crop(random_bg_crop())



canvas.paste(newbg, (0,0))
canvas.save('canvas.png')