import numpy as np
import pyscreenshot as ImageGrab
import cv2
import pytesseract

def read_capcha():

    filename = 'Image.png'
    x = 1
    new_value = 0
    while (True):
        screen = np.array(ImageGrab.grab(bbox=(422, 632, 829, 718)))
        cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        cv2.imwrite(filename, screen)
        x = x + 1
        print(x)
        if x == 2:
            cv2.destroyAllWindows()


            img = cv2.imread('Image.png')

            pytesseract.pytesseract.tesseract_cmd = "C:/Users/90531/AppData/Local/Tesseract-OCR/tesseract.exe"
            text = pytesseract.image_to_string(img, lang="eng")



            if text[0].isdigit() and text[2].isdigit():
                new_value = int(text[0]) + int(text[2])
                break
            else:

                continue
        else:
            continue
    return(new_value)