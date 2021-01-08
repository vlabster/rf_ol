from PIL import Image, ImageFont, ImageDraw, ImageOps
import random
from random import randint, choice
import os

data = ["name", "surname", "burthDate", "Country", "Obl", "date1", "date2", "data3", "country2", "obl2", "categories"]

symbolsMap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

def generateToken():
    global symbolsMap
    str = ''
    for i in range(0, 3):
        r = random.randint(0, 25)
        str += symbolsMap[r]

    str += '-'
    
    for i in range(0, 6):
        r = random.randint(26, 34)
        str += symbolsMap[r]
        if i == 2:
            str += '-'

    str += '-'

    for i in range(0, 2):
        r = random.randint(0, 25)
        str += symbolsMap[r]

    str += ' '

    for i in range(0, 2):
        r = random.randint(26, 34)
        str = str + symbolsMap[r]
    
    # for i in range(0, 13):
    #     r = random.randint(0, len(symbolsMap) - 1)
    #     str = str + symbolsMap[r]

    return str

img1 = Image.new(mode = "RGBA", size = (780,480), color = (255, 0, 0, 0))

img2 = Image.open('photos/1.png')
img2.thumbnail((142, 191), Image.ANTIALIAS)

img1.paste(img2, (121, 195))

finImg = ImageDraw.Draw(img1)


# set font
font = ImageFont.truetype('fonts/18799.ttf', size=23)

# draw text
finImg.text(
    (380, 148),
    'OOO',
    font=font,
    fill='#1C0606'
)

finImg.text(
    (380, 183),
    'SENSEY',
    font=font,
    fill='#1C0606'
)

finImg.text(
    (380, 208),
    'RAF',
    font=font,
    fill='#1C0606'
)

finImg.text(
    (380, 244),
    '10.10.2020 ' + 'RUSSIA',
    font=font,
    fill='#1C0606'
)

finImg.text(
    (380, 282),
    '10.12.2020',
    font=font,
    fill='#1C0606'
)

finImg.text(
    (380, 318),
    '10.10.2021',
    font=font,
    fill='#1C0606'
)

token = generateToken()

finImg.text(
    (380, 353),
    token,
    font=font,
    fill='#1C0606'
)

tokenTxt = Image.new('L', (500,50))
d = ImageDraw.Draw(tokenTxt)


d.text( (0, 0), token,  font=font, fill=255)

w=tokenTxt.rotate(90,  expand=1)

img1.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (730,-125),  w)

# finImg.text(
#     (200, 10),
#     token,
#     font=font,
#     fill='#1C0606'
# )

# img1.save('result.png')



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


### adding the static elements

flag = Image.open('resourses/flag.png')
numbers = Image.open('resourses/numbers.png')
photo_shadow = Image.open('resourses/photo_shadow.png')

card.paste(flag, (-30,-40), flag)
card.paste(numbers, (-25,-22), numbers)
card.paste(photo_shadow, (-25,-22), photo_shadow)

### resizing the image for proper placement

def changeImageSize(maxWidth, 
                    maxHeight, 
                    image):
    
    widthRatio  = maxWidth/image.size[0]
    heightRatio = maxHeight/image.size[1]

    newWidth    = int(widthRatio*image.size[0])
    newHeight   = int(heightRatio*image.size[1])

    newImage    = image.resize((newWidth, newHeight))
    return newImage

final_shit = changeImageSize(830,520, img1)

card.paste(final_shit, (-30,-40), final_shit)

canvas.paste(card, (50,50), card)

### adding the shadow
card_shadow = Image.open('resourses/card_shadow.png')
canvas.paste(card_shadow, (-10,-10), card_shadow)

canvas.save('result/canvas.png')



