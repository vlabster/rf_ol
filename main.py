from PIL import Image, ImageFont, ImageDraw, ImageOps
import random

data = ["name", "surname", "burthDate", "Country", "Obl", "date1", "date2", "data3", "country2", "obl2", "categories"]

symbolsMap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

def generateToken():
    global symbolsMap
    str = ''
    for i in range(0, 13):
        r = random.randint(0, len(symbolsMap) - 1)
        str = str + symbolsMap[r]

    return str

img1 = Image.open('sample.png')
img2 = Image.open('photos/1.png')

img1.paste(img2, (70, 170))

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

tokenTxt = Image.new('L', (500,50))
d = ImageDraw.Draw(tokenTxt)

token = generateToken()
d.text( (0, 0), token,  font=font, fill=255)

w=tokenTxt.rotate(90,  expand=1)

img1.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (940,0),  w)

# finImg.text(
#     (200, 10),
#     token,
#     font=font,
#     fill='#1C0606'
# )

img1.save('result.png')
