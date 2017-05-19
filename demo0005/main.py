from PIL import Image, ImageDraw, ImageFont

def imageThumb():
    im = Image.open('demo0005/header.png')
    w, h = im.size

    if w/h >= 640/1136:
        if w > 640:
            h = 640 * h / w
            w = 640
    else:
        if h > 1136:
            w = 1136 * w / h
            h = 1136            

    im.thumbnail((w, h))
    im.save('demo0005/header+thumbnail.png')

if __name__ == '__main__':
    imageThumb()
