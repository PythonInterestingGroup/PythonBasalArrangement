from PIL import Image, ImageDraw, ImageFont
import random
import string

def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def generateVerificationCode():
    chars = string.ascii_letters + string.digits
    im = Image.new('RGB', (240, 60), '#FFFFFF')
    font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 45)
    draw = ImageDraw.Draw(im)

    for x in range(240):
        for y in range(60):
            draw.point((x, y), fill=rndColor())

    for t in range(5):
        draw.text((50*t+10, 10), random.choice(chars), font=font, fill=rndColor2())

    im.save('demo0010/codes.png')


if __name__ == '__main__':
    generateVerificationCode()
