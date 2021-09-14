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
from threading import Thread
import sys
from flask_cors import CORS, cross_origin
import base64
import shutil
from werkzeug.utils import secure_filename

import shutil
import time
import requests
from lxml import html
from bs4 import BeautifulSoup
import json
import io
from PIL.ExifTags import TAGS

from proxy_checker_1 import ProxyChecker


import os
here = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

context = SSL.Context(SSL.SSLv23_METHOD)
cer = os.path.join(os.path.dirname(__file__), '/var/www/httpd-cert/www-root/liontracts.ru_le1.crt')
key = os.path.join(os.path.dirname(__file__), '/var/www/httpd-cert/www-root/liontracts.ru_le1.key')

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
symbolsMap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"


def generate_random_id(first_name = "RANDOM", middle_name = "RANDOM", second_name = "RANDOM", birthdate = "RANDOM", country = "RANDOM", imgurl=None, filename = "result", path = "RANDOM", param = 0, fonts = "RANDOM", flags = "RANDOM", docname = "RANDOM", bgrandomization = "WEAK"):
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

    if (imgurl != None):
        url = imgurl
    else:
        url = 'https://thispersondoesnotexist.com/image'


    current_datetime = str(time.time())
        
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',

    }
    responce = requests.get(url, headers=headers, stream=True)
    # print(url)
    if (param == 0):
        img2 = ''
        try:
            with open(str(here) + '/result/' + current_datetime + '.jpg', 'wb') as out_file:
                shutil.copyfileobj(responce.raw, out_file)
            del responce
            img2 = Image.open(str(here) + '/result/' + current_datetime + '.jpg')  
        # img2 = Image.open(io.BytesIO(responce.content))   
        except:
            dir = str(here) + '/photos/'
            img2 = Image.open(os.path.join(dir, random.choice(os.listdir(dir))))
        # img2 = Image.open(str(here) + '/photos/' + str(randPhoto) + '.png')
    else:
        img2 = Image.open(path)


    img3 = img2.resize((142, 188))

    # img2.thumbnail((142, 188), Image.ANTIALIAS)

    img1.paste(img3, (118, 192))

    finImg = ImageDraw.Draw(img1)


    # set font
    fontDir = str(here) + '/fonts/'
    if (fonts == "RANDOM"):
        font = ImageFont.truetype(os.path.join(fontDir, random.choice(os.listdir(fontDir))), size=22)
        phrase_font = ImageFont.truetype(os.path.join(fontDir, random.choice(os.listdir(fontDir))), size=30)
    else:
        font = ImageFont.truetype(str(here) + '/fonts/18799.TTF', size=22)
        phrase_font = ImageFont.truetype(str(here) + '/fonts/18799.TTF', size=30)


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
    randcrop = (randint(0,200), randint(0, 200), randint(800, 1100), randint(800, 1100))
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
    if (flags == "RANDOM"):
        randpath_flag = choice(os.listdir(str(here) + '/flags'))
        flag = Image.open(str(here) + '/flags/' + randpath_flag)
    else:
        flag = Image.open(str(here) + '/resourses/04.png').convert("RGBA")

    numbers = Image.open(str(here) + '/resourses/numbers.png')

    card.paste(flag, (70,10), flag)

    if (docname == "RANDOM"):
        phrases = open(str(here) + '/resourses/phrases.txt')
        phrase = random_line(phrases).upper()
    else:
        phrase = 'WORLD RESIDENT ID'

    random0_255 = lambda: random.randint(0,120)

    randomhex = '#%02X%02X%02X' % (random0_255(),random0_255(),random0_255())

    cardDraw = ImageDraw.Draw(card)

    cardDraw.text(
        (220, 50),
        str(phrase),
        font=phrase_font,
        fill='#1C0606'
        # fill=str(randomhex)
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

    im = Image.open(str(here) + '/result/' + str(filename) + '.png')
    rgb_im = im.convert('RGB')
    rgb_im.save(str(here) + '/result/' + str(filename) + '.jpg')
    os.remove(str(here) + '/result/' + str(filename) + '.png')

    dir = str(here) + '/exifs/'

    imgExif = Image.open(os.path.join(dir, random.choice(os.listdir(dir))))

    imgResultExifs = Image.open(str(here) + '/result/' + str(filename) + '.jpg')

    try:
        exif = imgExif.info['exif']
        imgResultExifs.save(str(here) + '/result/' + str(filename) + '.jpg', exif=exif)
    except:
        print(1)
# generate_random_id(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])


def generate_random_id_test(first_name = "RANDOM", middle_name = "RANDOM", second_name = "RANDOM", birthdate = "RANDOM", country = "RANDOM", imgurl=None, filename = "result", path = "RANDOM", param = 0, fonts = "RANDOM", flags = "RANDOM", docname = "RANDOM", bgrandomization = "WEAK"):
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

    if (imgurl != None):
        url = imgurl
    else:
        url = 'https://thispersondoesnotexist.com/image'


    current_datetime = str(time.time())
        
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',

    }
    responce = requests.get(url, headers=headers, stream=True)
    # print(url)
    if (param == 0):
        img2 = ''
        try:
            with open(str(here) + '/result/' + current_datetime + '.jpg', 'wb') as out_file:
                shutil.copyfileobj(responce.raw, out_file)
            del responce
            img2 = Image.open(str(here) + '/result/' + current_datetime + '.jpg')  
        # img2 = Image.open(io.BytesIO(responce.content))   
        except:
            dir = str(here) + '/photos/'
            img2 = Image.open(os.path.join(dir, random.choice(os.listdir(dir))))
        # img2 = Image.open(str(here) + '/photos/' + str(randPhoto) + '.png')
    else:
        img2 = Image.open(path)


    img3 = img2.resize((142, 188))

    # img2.thumbnail((142, 188), Image.ANTIALIAS)

    img1.paste(img3, (118, 192))

    finImg = ImageDraw.Draw(img1)


    # set font
    fontDir = str(here) + '/fonts/'
    if (fonts == "RANDOM"):
        font = ImageFont.truetype(os.path.join(fontDir, random.choice(os.listdir(fontDir))), size=22)
        phrase_font = ImageFont.truetype(os.path.join(fontDir, random.choice(os.listdir(fontDir))), size=30)
    else:
        font = ImageFont.truetype(str(here) + '/fonts/18799.TTF', size=22)
        phrase_font = ImageFont.truetype(str(here) + '/fonts/18799.TTF', size=30)


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
    randcrop = (randint(0,200), randint(0, 200), randint(800, 1100), randint(800, 1100))
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
    if (flags == "RANDOM"):
        randpath_flag = choice(os.listdir(str(here) + '/flags'))
        flag = Image.open(str(here) + '/flags/' + randpath_flag)
    else:
        flag = Image.open(str(here) + '/resourses/04.png').convert("RGBA")

    numbers = Image.open(str(here) + '/resourses/numbers.png')

    card.paste(flag, (70,10), flag)

    if (docname == "RANDOM"):
        phrases = open(str(here) + '/resourses/phrases.txt')
        phrase = random_line(phrases).upper()
    else:
        phrase = 'WORLD RESIDENT ID'

    random0_255 = lambda: random.randint(0,120)

    randomhex = '#%02X%02X%02X' % (random0_255(),random0_255(),random0_255())

    cardDraw = ImageDraw.Draw(card)

    cardDraw.text(
        (220, 50),
        str(phrase),
        font=phrase_font,
        fill='#1C0606'
        # fill=str(randomhex)
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

    im = Image.open(str(here) + '/result/' + str(filename) + '.png')
    rgb_im = im.convert('RGB')
    rgb_im.save(str(here) + '/result/' + str(filename) + '.jpg')
    os.remove(str(here) + '/result/' + str(filename) + '.png')

    dir = str(here) + '/exifs/'

    imgExif = Image.open(os.path.join(dir, random.choice(os.listdir(dir))))

    imgResultExifs = Image.open(str(here) + '/result/' + str(filename) + '.jpg')

    try:
        exif = imgExif.info['exif']
        imgResultExifs.save(str(here) + '/result/' + str(filename) + '.jpg', exif=exif)
    except:
        print(1)

# global res_proxy
def checker(arr):
    res_proxy = {}
    threads = []

    def checkProxy(value):
        checker = ProxyChecker()
        proxy = value.split(':')

        ip = proxy[0]
        port = proxy[1]
        user = ''
        password = ''

        if len(proxy) >= 3:
            user = proxy[2]
        
        if len(proxy) >= 4:
            password = proxy[3]
        
        result = checker.check_proxy(ip + ':' + port, True, False, user, password)
        res_proxy[value] = result

        return result

    for val in arr:
        th = Thread(target=checkProxy, args=(val,))
        th.start()
        threads.append(th)

    for val in threads:
        val.join()

    return res_proxy

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
    
@app.route('/get_fb', methods=['POST', 'GET'])
@cross_origin()
def get_fb():
    # return 'Hello world'
    postUrl = request.form.get('link')
    
    url = requests.get(postUrl)
    # return url.text
    soup = BeautifulSoup(url.text,  features="html5lib")
    # return str(postUrl)
    a = soup.findAll('a', {"class": "_2nlw _2nlv"})
    
    # print(a[0].text)
    photo = soup.findAll('img', {"class": "_11kf img"})
    fullName = a[0].text
    src = photo[0].attrs['src']
    splitFullName = fullName.split(' ')
    name = splitFullName[0]
    surname = splitFullName[1]
    # res.first_name = name
    # res.second_name = surname
    # res.img = src
    res = {
        'first_name': name,
        'second_name': surname,
        'img': src
    }
    js = json.dumps(res)
    # print(src)
    return js
    
def detect(url):
    try:
        r = requests.get(url, allow_redirects=True)
        obj = []
        for x in r.history:
            obj.append({"url": x.url, "headers": x.headers['Location'], "status_code": x.status_code})
        return obj
    except:
        return "Error"

@app.route('/url_detective', methods=['get'])
@cross_origin()
def url_detective():
    url = request.args.get('url')
    res = detect(url)
    try:
        res = json.dumps(res)
        return res
    except:
        return res

@app.route('/proxy_checker', methods=['POST'])
@cross_origin()
def proxy_checker():
    data = request.data
    jsonData = json.loads(data)
    res = checker(jsonData['data'])
    return res
    # try:
    #     return jsonData['data'][0]
    # except Exception:
    #     return 1


@app.route('/get_image', methods=['POST'])
@cross_origin()
def get_image():
    random_shit = str(randint(10000000,99999999))
    first_name = request.args.get('first_name')
    middle_name = request.args.get('middle_name')
    second_name = request.args.get('second_name')
    birthdate = request.args.get('birthdate')
    country = request.args.get('country')
    imgurl = request.form.get('imgurl')
    fonts = request.args.get('fonts')
    flags = request.args.get('flags')
    docname = request.args.get('docname')
    bgrandomization = request.args.get('bgrandomization')

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

    generate_random_id(first_name, middle_name, second_name, birthdate, country, imgurl, random_shit, str(path), param, fonts, flags, docname, bgrandomization)
    filename = str(here) + '/result/' + random_shit + '.jpg'
    if (param == 1):
        os.remove(path)

    return send_file(filename, mimetype='image/jpeg')
 
@app.route('/')
def hello_world():
    return 'Hello World!'


#################
# Test endpoint #
#################

@app.route('/get_image_test', methods=['POST'])
@cross_origin()
def get_image_test():
    random_shit = str(randint(10000000,99999999))
    first_name = request.args.get('first_name')
    middle_name = request.args.get('middle_name')
    second_name = request.args.get('second_name')
    birthdate = request.args.get('birthdate')
    country = request.args.get('country')
    imgurl = request.form.get('imgurl')
    fonts = request.args.get('fonts')
    flags = request.args.get('flags')
    docname = request.args.get('docname')
    bgrandomization = request.args.get('bgrandomization')

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

    generate_random_id_test(first_name, middle_name, second_name, birthdate, country, imgurl, random_shit, str(path), param, fonts, flags, docname, bgrandomization)
    filename = str(here) + '/result/' + random_shit + '.jpg'
    if (param == 1):
        os.remove(path)

    return send_file(filename, mimetype='image/jpeg')
 
if __name__ == '__main__':
    context = (cer, key)
    app.run( host='0.0.0.0', ssl_context=context)