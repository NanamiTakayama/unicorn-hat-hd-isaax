#!/usr/bin/env python

# The MIT License (MIT)
#
# Copyright (c) 2016 LoveBootCaptain
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
import time
from sys import exit, argv

try:
    from PIL import Image
except ImportError:
    exit('This script requires the pillow module\nInstall with: sudo pip install pillow')

import unicornhathd as unicorn


unicorn.brightness(0.3)
unicorn.rotation(0)
folder_path = '/home/pi/project/examples/icons/'
icon_extension = '.png'
width, height = unicorn.get_shape()
cycle_time = 0.25


def draw_animation(image):
    try:
        for o_x in range(int(image.size[0] / width)):
            for o_y in range(int(image.size[1] / height)):
                valid = False
                for x in range(width):
                    for y in range(height):
                        pixel = image.getpixel(((o_x * width) + y, (o_y * height) + x))
                        r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
                        if r or g or b:
                            valid = True
                        unicorn.set_pixel(x, y, r, g, b)
                if valid:
                    unicorn.show()
                    time.sleep(cycle_time)

    except KeyboardInterrupt:
        unicorn.off()

def main():
    if argv[1] in os.listdir(folder_path):
        print('Drawing Image: {}'.format(argv[1]))

        img = Image.open(folder_path + argv[1])
        draw_animation(img)
    else:
        print('You need to give an argument.')


if __name__ == '__main__':
    main()
