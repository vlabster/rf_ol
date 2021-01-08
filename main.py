from PIL import Image, ImageFont, ImageDraw, ImageOps
import random

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

img1 = Image.open('sample.png')

img2 = Image.open('photos/1.png')
img2.thumbnail((142, 191), Image.ANTIALIAS)

img1.paste(img2, (121, 195))
img1.save('result.png')

finImg = ImageDraw.Draw(img1)


# set font
font = ImageFont.truetype('fonts/20051.ttf', size=21)

# draw text
finImg.text(
    (380, 138),
    'OOO',
    font=font,
    fill='#1C0606'
)

finImg.text(
    (380, 175),
    'SENSEY',
    font=font,
    fill='#1C0606'
)

finImg.text(
    (380, 200),
    'RAF',
    font=font,
    fill='#1C0606'
)

finImg.text(
    (380, 240),
    '10.10.2020 ' + 'RUSSIA',
    font=font,
    fill='#1C0606'
)

finImg.text(
    (380, 279),
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
    (380, 355),
    token,
    font=font,
    fill='#1C0606'
)

tokenTxt = Image.new('L', (500,50))
d = ImageDraw.Draw(tokenTxt)


d.text( (0, 0), token,  font=font, fill=255)

w=tokenTxt.rotate(90,  expand=1)

img1.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (800,-125),  w)

# finImg.text(
#     (200, 10),
#     token,
#     font=font,
#     fill='#1C0606'
# )

img1.save('result.png')

# img1.paste(img2, (70, 170))








