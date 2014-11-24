from PIL import Image
import os


def usage():

    return



def load_and_check(img_path, file_path, p):
    img = Image.open(img_path)

    count = 0

    for pixel in img.getdata():
        count += 1

    bytes_size = os.path.getsize(file_path)


    if (count / int(p)) < (bytes_size / 3):
        raise Exception('Encoding file too large. Provide a larger photo or reduce the p value')
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