from PIL import Image
data = ["name", "surname", "burthDate", "Country", "Obl", "date1", "date2", "data3", "country2", "obl2", "categories"]

img1 = Image.open('sample.png')
img2 = Image.open('photos/1.png')

img1.paste(img2, (70, 170))
img1.save('result.png')
