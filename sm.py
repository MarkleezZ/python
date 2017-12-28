from PIL import Image
import argparse

parser = argparse.ArgumentParser()


parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int, default=100)
parser.add_argument('--height', type=int, default=100)


args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output


ascii_char = list(r"$@&%B#=-. ")
def RGB2char(r, b, g, alpha=256):
    if alpha ==0:
        return ''
    length = len(ascii_char)
    gray = int((19595 * r + 38469 * g + 7472 * b) >> 16)
    unit = (256.0)/length
    return ascii_char[int(gray/unit)]


if __name__ == '__main__':
    img = Image.open(IMG)
    img = img.resize((WIDTH, HEIGHT), Image.NEAREST)
    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += RGB2char(*img.getpixel((j,i))[:3])
        txt +='\n'

    print txt

    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    



