import json
import random

import cv2
import numpy as np


import cv2
import numpy as np
import random

def create_detection_image(detection):
    # get car image
    car_img = cv2.imread(detection['PHOTO_PATH'])
    # resize image
    car_img = cv2.resize(car_img, (700, 500), interpolation=cv2.INTER_AREA)

    # create new info image
    height, width, _ = car_img.shape
    info_img = np.zeros((int(height * 0.5), width, 3), np.uint8)
    info_img[:] = (0, 0, 0)
    info_img_height, info_img_width, _ = info_img.shape
    font_scale = height / 600

    # add info text about car
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(info_img, f"Местоположение: {detection['COORDINATES']}", (10, int(info_img_height * 0.2)), font,
                font_scale, (255, 255, 255), 1)
    cv2.putText(info_img, f"ГРЗ: {detection['GRZ']}", (10, int(info_img_height * 0.4)), font, font_scale,
                (255, 255, 255), 1)
    cv2.putText(info_img, f"Состояние фар: фары выключены", (10, int(info_img_height * 0.6)), font,
                font_scale, (255, 255, 255), 1)
    cv2.putText(info_img, f"Время: {detection['LAST_TIME']}", (10, int(info_img_height * 0.8)), font, font_scale,
                (255, 255, 255), 1)
    # concatenate car and info images
    new_img = np.concatenate((car_img, info_img), axis=0)
    # сохранение картинки, пока что её название - это случайное число, потом нужно поменять
    random_number = random.randint(1, 1000)
    filename = f".created_pictures/{detection['GRZ'][1:4]}.jpg"
    cv2.imwrite(filename, new_img)

