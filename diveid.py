# -*- coding: utf-8 -*-
import cv2

def main():

    '''
    # 2点(x1,y1),(x2,y2)を通る矩形部分を切り抜き
    clp = img[x1:x2, y1:y2]
    # クリッピングした箇所を保存
    cv2.imwrite("test-tl.png", clp)   
    '''

    img = cv2.imread("test.png")
    height, width, channels = img.shape

    clp = img[0:width/2]     
    cv2.imwrite("test-tl.png", clp)


if __name__ == '__main__':
    main()
