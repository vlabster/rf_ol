from random import randint, choice
import os
from PIL import Image, ImageFont, ImageDraw, ImageFilter

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


### adding the waves

waves = Image.new(mode = "RGBA", size = (780,480))
randpath_waves = choice(os.listdir('waves'))
wavesbg = Image.open('waves/' + randpath_waves)
randcrop = (randint(0,200), randint(0, 200), randint(300, 600), randint(300, 600))
newwavesbg = wavesbg.crop(randcrop)
#resize the waves
aspect_ratio = 780/480
sizeval = randint(200,500)
newsize = (780, 480)
newwavesbg = newwavesbg.resize(newsize)
waves = add_corners(newwavesbg, 20)

### assembling the image

card.paste(waves, (0,0))

canvas.paste(card, (50,50), card)

canvas.save('canvas.png')