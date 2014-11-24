from PIL import Image

import sys
import getopt
import os

pixel_spacer = None
img_path = None
out_path = None
file_path = None
mode_value = None
# to test encoding
# -p 363 -i test.jpg -o test2.jpg -f test.txt -m encode


def usage():
    return


def load_and_check(img_path, file_path, p):
    img = Image.open(img_path)
    pixels = img.load()

    count = 0

    for pixel in img.getdata():
        count += 1

    bytes_size = os.path.getsize(file_path)


    if (count / int(p)) < (bytes_size / 3):
        raise Exception('Encoding file too large. (get a bigger picture or reduce the spacing)')
    else:
        return True


def get_value(f):
    try:
        x = f.read(1)
        if not x:
            return '\f'
        return x
    except Exception:
        return '\f'


def encode(img_path, file_path, p, out_path):
    img = Image.open(img_path)
    pixels = img.load()

    f = open(file_path, 'r')

    counter = 0

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if counter % int(p) == 0:
                a = get_value(f)
                b = get_value(f)
                c = get_value(f)
                #print str(ord(a)) + str(ord(b)) + str(ord(c))
                if a == '\f' or b == '\f' or c == '\f':
                    pixels[i,j] = (ord(a), ord(b), ord(c))
                    img.save(out_path, quality=100) if out_path else img.save(img_path, quality=100)
                    return
                pixels[i,j] = (ord(a), ord(b), ord(c))
                print 'Counter is: ' + str(counter) + ' Pixel is {0}, {1}'.format(i, j)
            counter += 1
    # If they provide a path to save it to that otherwise overwrite the old image
    img.save(out_path, quality=100) if out_path else img.save(img_path, quality=100)

    return


def decode(img_path, file_path, p):
    img = Image.open(img_path)
    pixels = img.load()
    print pixels[0,363]
    f = open(file_path, 'w+')

    counter = 0
    print p
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if counter % int(p) == 0:
                print chr(pixels[i,j][0]) + chr(pixels[i,j][1]) + chr(pixels[i, j][2])
                if chr(pixels[i, j][0]) == '\f':
                    print 'finished'
                    f.close()
                    return
                elif pixels[i, j][1] == '\f':
                    f.write(chr(pixels[i, j][0]))
                    print 'finished'
                    f.close()
                    return
                elif pixels[i, j][2] == '\f':
                    f.write(chr(pixels[i, j][0]) . chr(pixels[i, j][1]))
                    print 'finished'
                    f.close()
                    return
                else:
                    f.write(chr(pixels[i,j][0]) + chr(pixels[i,j][1]) + chr(pixels[i, j][2]))
            counter += 1
    return


try:
    opts, args = getopt.getopt(sys.argv[1:], 'p:i:o:f:m:h', ['pixel=', 'image=', 'out=', 'file=', 'mode=', 'help'])
except getopt.GetoptError:
    usage()
    sys.exit(2)


for opt, arg in opts:
    if opt in ('-h', '--help'):
        usage()
        sys.exit(0)
    elif opt in ('-p', '--pixel'):
        pixel_spacer = arg
    elif opt in ('-i', '--image'):
        img_path = arg
    elif opt in ('-o', '--out'):
        out_path = arg
    elif opt in ('-f', '--file'):
        file_path = arg
    elif opt in ('-m', '--mode'):
        mode_value = arg
    else:
        usage()
        sys.exit(2)

if not pixel_spacer or not img_path or not file_path:
    usage()
    sys.exit(2)


if mode_value == 'encode':
    load_and_check(img_path, file_path, pixel_spacer)
    encode(img_path, file_path, pixel_spacer, out_path)
else:
    decode(img_path, file_path, pixel_spacer)
