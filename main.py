#!/usr/bin/python3.6
from PIL import Image, ImageFont, ImageDraw, ImageOps, ImageFilter
import random
from random import randint, choice
import os
import datetime
from flask import Flask
from flask import send_file, request
import sys
symbolsMap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"


def generate_random_id(first_name = "RANDOM", middle_name = "RANDOM", second_name = "RANDOM", birthdate = "RANDOM", country = "RANDOM", filename = "result"):
    data = ["name", "surname", "burthDate", "Country", "Obl", "date1", "date2", "data3", "country2", "obl2", "categories"]

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
    randPhoto = randint(1, 30)
    img2 = Image.open('photos/' + str(randPhoto) + '.png')
    img2.thumbnail((142, 188), Image.ANTIALIAS)

    img1.paste(img2, (118, 192))

    finImg = ImageDraw.Draw(img1)


    # set font
    font = ImageFont.truetype('fonts/18799.TTF', size=22)


    def random_line(afile):
        line = next(afile)
        for num, aline in enumerate(afile, 2):
            if random.randrange(num):
                continue
            line = aline
        return line

    if (first_name == "RANDOM"):
        first_names = open('resourses/names.txt')
        first_name = random_line(first_names).upper()

    if (middle_name == "RANDOM"):
        middle_names = open('resourses/names.txt')
        middle_name = random_line(middle_names).upper()

    if (second_name == "RANDOM"):
        second_names = open('resourses/families.txt')
        second_name = random_line(second_names).upper()

    if (country == "RANDOM"):
        countries = open('resourses/countries.txt')
        country = random_line(countries).upper()


    def get_random_date(start_year, end_year):
        start_date = datetime.date(start_year, 1, 1)
        end_date = datetime.date(end_year, 1, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)

        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return random_date

    if (birthdate == "RANDOM"):
        birthdate = get_random_date(1940, 2002)

    card_given = get_random_date(2010, 2020)
    card_expires = get_random_date(2022, 2030)

    # draw text
    finImg.text(
        (380, 147),
        first_name,
        font=font,
        fill='#1C0606'
    )

    finImg.text(
        (380, 181),
        middle_name,
        font=font,
        fill='#1C0606'
    )

    finImg.text(
        (380, 208),
        second_name,
        font=font,
        fill='#1C0606'
    )

    finImg.text(
        (380, 241),
        str(birthdate) + ' ' + country,
        font=font,
        fill='#1C0606'
    )

    finImg.text(
        (380, 277),
        str(card_given),
        font=font,
        fill='#1C0606'
    )

    finImg.text(
        (380, 313),
        str(card_expires),
        font=font,
        fill='#1C0606'
    )

    token = generateToken()

    finImg.text(
        (380, 347),
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

    card.paste(flag, (-30,-40), flag)
    card.paste(numbers, (-25,-22), numbers)

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

    canvas.save('result/' + str(filename) + '.png')



# generate_random_id(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])


### define a flask endpoint

app = Flask(__name__)

@app.route('/get_image')
def get_image():
    random_shit = str(randint(10000000,99999999))
    first_name = request.args.get('first_name')
    middle_name = request.args.get('middle_name')
    second_name = request.args.get('second_name')
    birthdate = request.args.get('birthdate')
    country = request.args.get('country')
    generate_random_id(first_name, middle_name, second_name, birthdate, country, filename = random_shit)
    filename = 'result/' + random_shit + '.png'
    return send_file(filename, mimetype='image/png')

@app.route('/')
def h():
    return 'hello world'

app.run(host='0.0.0.0', port=81)