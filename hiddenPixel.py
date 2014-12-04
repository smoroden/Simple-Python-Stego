from utils import*
from stego import*
import sys
import getopt


pixel_spacer = None
img_path = None
out_path = None
file_path = None
mode_value = None
# to test encoding
# -p 363 -i test.jpg -o test2.bmp -f test.txt -m encode
# -p 363 -i test2.bmp  -f dnsspoof2.rb -m decode

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

# Did the user provide a p value, an image and a file to encode/decode?
if not pixel_spacer or not img_path or not file_path:
    usage()
    sys.exit(2)


if mode_value == 'encode':
    load_and_check(img_path, file_path, pixel_spacer)
    encode(img_path, file_path, pixel_spacer, out_path)
else:
    decode(img_path, file_path, pixel_spacer)
