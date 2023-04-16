import cv2
import json

# this function converts image from cv2-image to string format
# first two numbers are size of image, other numbers after grouping by three wil be a pixels in Blue-Green-Red
def img_to_str(image):
    s = ''
    s += str(image.shape[0]) + " "
    s += str(image.shape[1]) + " "
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for k in range(3):
                s += str(image.item(i, j, k))
                s += " "
    return s

# this function converts image from string to cv2-image format
def str_to_img(s):
    pass

# this function makes place under the picture and place informational text there
def make_bottom_and_text(image, date, time, cam_number, direction, real_speed, allowed_speed, adress):
    new_img = cv2.copyMakeBorder(image, 0, 100, 0, 0, cv2.BORDER_CONSTANT, value = (0,0,0))
    first_str = "Дата- " + date + "  Время- " + time + "  Скорость- " + real_speed + "  Разрешенная скорость- " + allowed_speed
    second_str = "Прибор №- " + cam_number + "  Направление контроля- " + direction + "  Адрес- "
    third_str = adress
    cv2.putText(new_img, first_str, (image.shape[0]+10, 5), cv2.FONT_HERSHEY_SIMPLEX, 8, (255, 255, 255))
    cv2.putText(new_img, second_str, (image.shape[0]+10, 5), cv2.FONT_HERSHEY_SIMPLEX, 8, (255, 255, 255))
    cv2.putText(new_img, third_str, (image.shape[0]+10, 5), cv2.FONT_HERSHEY_SIMPLEX, 8, (255, 255, 255))
    return new_img

# this function read 1 tuple from .json file and convert it into dict format
def read_json(json_file):
    pass