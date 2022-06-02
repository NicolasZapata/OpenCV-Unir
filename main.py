# This is a sample Python script.

# Base Libraries
import cv2
import numpy as np



# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Recolored Image to Gray
def convert_gray_img(image):
    filepath = 'src/doc/gray_img.jpg'
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    img = cv2.imread(image)
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05)
    cv2.imwrite(filepath, img)

# Rezise and open image in local storage
def dispay_img(title, image):
    filepath = 'gray_img.png'
    img = cv2.imread(image, cv2.IMREAD_COLOR)
    cv2.imshow(title, img)
    cv2.waitKey(2)
    cv2.destroyAllWindows()
    cv2.imwrite(filepath, img)

# Rotate Images
def rotate_img(window_title, image):
    src = cv2.imread(image)
    img = cv2.rotate(src, cv2.cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow(window_title, src)
    cv2.imwrite('rotate_img.png', img)
    cv2.waitKey(10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unir_logo = 'src/unircol.png'
    my_title = "Unir Logo"
    rotate_img(my_title, unir_logo)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
