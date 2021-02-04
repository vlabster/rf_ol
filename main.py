#!/usr/bin/python3.6
from flask import Flask
from OpenSSL import SSL
from PIL import Image, ImageFont, ImageDraw, ImageOps, ImageFilter
import random
from random import randint, choice
import os
import datetime
from flask import Flask
from flask import send_file, request
import sys
from flask_cors import CORS, cross_origin
import base64
import shutil
from werkzeug.utils import secure_filename

import shutil
import time
import requests

import os
here = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

# context = SSL.Context(SSL.SSLv23_METHOD)
# cer = os.path.join(os.path.dirname(__file__), '/var/www/httpd-cert/www-root/liontracts.ru_le1.crt')
# key = os.path.join(os.path.dirname(__file__), '/var/www/httpd-cert/www-root/liontracts.ru_le1.key')

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
symbolsMap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"


def generate_random_id(first_name = "RANDOM", middle_name = "RANDOM", second_name = "RANDOM", birthdate = "RANDOM", country = "RANDOM", filename = "result", path = "RANDOM", param = 0):
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
    randPhoto = randint(1, 59)

    url = 'https://thispersondoesnotexist.com/image'
    current_datetime = str(time.time())

    responce = requests.get(url, stream=True)
    if (param == 0):
        img2 = ''
        try:
            with open(str(here) + '/result/' + current_datetime + '.png', 'wb') as out_file:
                shutil.copyfileobj(responce.raw, out_file)
            del responce
            img2 = Image.open(str(here) + '/result/' + current_datetime + '.png')   
        except:
            dir = str(here) + '/photos/'
            img2 = Image.open(os.path.join(dir, random.choice(os.listdir(dir))))
        # img2 = Image.open(str(here) + '/photos/' + str(randPhoto) + '.png')
    else:
        img2 = Image.open(path)

    img2.thumbnail((142, 188), Image.ANTIALIAS)

    img1.paste(img2, (118, 192))

    finImg = ImageDraw.Draw(img1)


    # set font
    fontDir = str(here) + '/fonts/'
    font = ImageFont.truetype(os.path.join(fontDir, random.choice(os.listdir(fontDir))), size=22)
    phrase_font = ImageFont.truetype(os.path.join(fontDir, random.choice(os.listdir(fontDir))), size=30)
    # font = ImageFont.truetype(str(here) + '/fonts/18799.TTF', size=22)


    def random_line(afile):
        line = next(afile)
        for num, aline in enumerate(afile, 2):
            if random.randrange(num):
                continue
            line = aline
        return line

    if (first_name == "RANDOM"):
        first_names = open(str(here) + '/resourses/names.txt')
        first_name = random_line(first_names).upper()

    if (middle_name == "RANDOM"):
        middle_names = open(str(here) + '/resourses/names.txt')
        middle_name = random_line(middle_names).upper()

    if (second_name == "RANDOM"):
        second_names = open(str(here) + '/resourses/families.txt')
        second_name = random_line(second_names).upper()

    if (country == "RANDOM"):
        countries = open(str(here) + '/resourses/countries.txt')
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

    randpath_bg = choice(os.listdir(str(here) + '/bgs'))

    bg = Image.open(str(here) + '/bgs/' + randpath_bg)

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
    randpath_waves = choice(os.listdir(str(here) + '/waves'))
    wavesbg = Image.open(str(here) + '/waves/' + randpath_waves)
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
    randpath_flag = choice(os.listdir(str(here) + '/flags'))
    flag = Image.open(str(here) + '/flags/' + randpath_flag)



    numbers = Image.open(str(here) + '/resourses/numbers.png')

    card.paste(flag, (30,10), flag)

    phrases = open(str(here) + '/resourses/phrases.txt')
    phrase = random_line(phrases).upper()

    random0_255 = lambda: random.randint(0,120)

    randomhex = '#%02X%02X%02X' % (random0_255(),random0_255(),random0_255())

    cardDraw = ImageDraw.Draw(card)

    cardDraw.text(
        (180, 50),
        str(phrase),
        font=phrase_font,
        fill=str(randomhex)
    )

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
    card_shadow = Image.open(str(here) + '/resourses/card_shadow.png')
    canvas.paste(card_shadow, (-10,-10), card_shadow)

    canvas.save(str(here) + '/result/' + str(filename) + '.png')



# generate_random_id(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])


### define a flask endpoint
 
# @app.route('/clear')
# @cross_origin()
# def clear():
#     folder = str(here) + '/result/'
#     for the_file in os.listdir(folder):
#         file_path = os.path.join(folder, the_file)
#         try:
#             if os.path.isfile(file_path):
#                 os.unlink(file_path)
#             #elif os.path.isdir(file_path): shutil.rmtree(file_path)
#         except Exception as e:
#             return 'false'
#     return 'true'
    

@app.route('/get_image', methods=['get'])
@cross_origin()
def get_image():
    random_shit = str(randint(10000000,99999999))
    first_name = request.args.get('first_name')
    middle_name = request.args.get('middle_name')
    second_name = request.args.get('second_name')
    birthdate = request.args.get('birthdate')
    country = request.args.get('country')
    param = -1
    path = ''
    try:
        img = request.files.get('file')
        img.save(os.path.join(str(here) + '/saved', secure_filename(img.filename)))
        path = os.path.join(str(here) + '/saved', secure_filename(img.filename))
        param = 1
    except:
        param = 0
        path = ''

    generate_random_id(first_name, middle_name, second_name, birthdate, country, random_shit, str(path), param)
    filename = str(here) + '/result/' + random_shit + '.png'
    if (param == 1):
        os.remove(path)

    return send_file(filename, mimetype='image/png')
 
@app.route('/')
def hello_world():
    return 'Hello World!'
 
if __name__ == '__main__':
    app.run()