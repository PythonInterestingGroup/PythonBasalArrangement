from PIL import Image, ImageDraw, ImageFont

def imageChange():
    im = Image.open('demo0000/header.png')
    w, h = im.size

    font = ImageFont.truetype('SourceCodePro-Regular.ttf', 50)

    draw = ImageDraw.Draw(im)
    draw.text((w-60, 10), '44', font=font, fill='#FF9000')
    im.save('demo0000/header+text.png')


if __name__ == '__main__':
    imageChange()
