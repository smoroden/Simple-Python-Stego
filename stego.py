from PIL import Image
from utils import*


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
                if a == '\f' or b == '\f' or c == '\f':
                    pixels[i,j] = (ord(a), ord(b), ord(c))
                    img.save(out_path, quality=100) if out_path else img.save(img_path, quality=100)
                    return
                pixels[i,j] = (ord(a), ord(b), ord(c))
                # print 'Counter is: ' + str(counter) + ' Pixel is {0}, {1}'.format(i, j)
            counter += 1
    # If they provide a path to save it to that otherwise overwrite the old image
    img.save(out_path, quality=100) if out_path else img.save(img_path, quality=100)

    return


def decode(img_path, file_path, p):
    img = Image.open(img_path)
    pixels = img.load()
    #print pixels[0,363]
    f = open(file_path, 'w+')

    counter = 0
    #print p
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if counter % int(p) == 0:
                # print chr(pixels[i,j][0]) + chr(pixels[i,j][1]) + chr(pixels[i, j][2])
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