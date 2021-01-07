from random import randint, choice
import os
from PIL import Image, ImageFont, ImageDraw

canvas = Image.new(mode = "RGBA", size = (900,600))

### working with the main canvas backround

randpath_bg = choice(os.listdir('bgs'))

bg = Image.open('bgs/' + randpath_bg)

def random_bg_crop():
    left = randint(0,200)
    upper = randint(0,200)
    right = left + 900
    bottom = upper + 600
    return((left, upper, right, bottom))

newbg = bg.crop(random_bg_crop())

canvas.paste(newbg, (0,0))

### working with the card obj

card = Image.new(mode = "RGBA", size = (780,480))
randpath_card = choice(os.listdir('cardbgs'))
cardbg = Image.open('cardbgs/' + randpath_card)

def random_card_crop():
    left = randint(0,200)
    upper = randint(0,200)
    right = left + 780
    bottom = upper + 480
    return((left, upper, right, bottom))

newcardbg = cardbg.crop(random_card_crop())

### add border radius

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

croppedbg = add_corners(newcardbg, 20)

### assembling the image

card.paste(croppedbg, (0,0))

canvas.paste(card, (50,50), card)

canvas.save('canvas.png')