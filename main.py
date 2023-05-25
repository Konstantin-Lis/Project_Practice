# Часть функций написаны с допущением, что список whole_data не пустой
# При сборке системы воедино следует перед активацией функций check и checking_for_left убедиться в том, что whole_data не пуст

global whole_data
whole_data = [
    {"GRZ": "AA000A96", "LAST_TIME": "12:43:55", "LIGHTS": [0, 1, 1, 1, 1, 0, 1]},
    {"GRZ": "AA001A96", "LAST_TIME": "12:43:54", "LIGHTS": [0, 0, 1, 0, 1, 0, 0, 0, 0, 1]},
    {"GRZ": "AA002A96", "LAST_TIME": "12:43:55", "LIGHTS": [0, 1, 1]},
    {"GRZ": "AA003A96", "LAST_TIME": "12:43:55", "LIGHTS": [1, 1, 1, 0, 1]},
    {"GRZ": "AA004A96", "LAST_TIME": "12:43:55", "LIGHTS": [0, 1, 1, 0, 0, 1]},
    {"GRZ": "AA005A96", "LAST_TIME": "12:43:55", "LIGHTS": [1, 1, 1, 1, 1, 1, 1]},
    {"GRZ": "AA006A96", "LAST_TIME": "12:43:55", "LIGHTS": [0]}
]

dct = {"photo_path": "src/photo3.jpg", "license_plate": "АБВ654", "lights_on": True, "timestamp": "2023-04-12T10:00:15Z", "coordinates": "55.998768, 37.204968", "address": "Центральный проспект. Д.1, г.Зеленоград, г.Москва"}
REAL_TIME = "12:43:56"
REAL_DATE = "15.04.2023"

def deside(lst):
    num = len(lst)
    sum = 0
    for i in lst:
        sum += i
    res = round(sum/num, 3)
    if res > 0.5:
        return 0
    else:
        return 1

# Функция выписки штрафа
def fixate_violation(dct):
    pass

def check(dct):
    for i in range(len(whole_data)):
        if whole_data[i]["GRZ"]==dct["license_plate"]:
            return i
        else:
            return -1

# Данная функция должна активироваться только если функция check вернула не -1
def new_data(dct):
    global whole_data
    place = check(dct)
    if dct["lights_on"]:
        whole_data[place]["LIGHTS"].append(1)
    else:
        whole_data[place]["LIGHTS"].append(0)
    whole_data[place]["LAST_TIME"] = dct["timestamp"].split('T')[1][:-1]

# Данная функция должна активироваться только если функция check вернула -1
def new_car(dct):
    global whole_data
    new_dct = {"GRZ": '', "LAST_TIME": "", "LIGHTS": []}
    new_dct["GRZ"] = dct["license_plate"]
    new_dct["LAST_TIME"] = dct["timestamp"].split('T')[1][:-1]
    if dct["lights_on"]:
        new_dct["LIGHTS"].append(1)
    else:
        new_dct["LIGHTS"].append(0)
    whole_data.append(new_dct)

# В данной функции мы прогоняем все элементы нашего списка по циклу
# Если какого-то из автомобилей не было больше 10-ти секунд, то определяем, присутствовало ли нарушение
# Если присутствовало, то выписываем штраф
# (функция выписки штрафа не реализована)
# В самом конце удаляем данные об автомобиле из локальной базы
def checking_for_left(REAL_TIME):
    global whole_data
    timestamp0 = REAL_TIME.split(":")
    timestamp = []
    absent_cars = []
    for i in range(3):
        timestamp.append(int(timestamp0[i]))
    for i in range(len(whole_data)):
        if whole_data[i]["LAST_TIME"] != REAL_TIME:
            last_time0 = whole_data[i]["LAST_TIME"].split(":")
            last_time = []
            for j in range(3):
                last_time.append(int(last_time0[j]))
            if last_time[2]+10 < timestamp[2]:
                absent_cars.append(i)
            elif last_time[2] > timestamp[2]:
                if last_time[2]+10 < timestamp[2]+60:
                    absent_cars.append(i)

    for i in absent_cars:
        violation = deside(whole_data[i]["LIGHTS"])
        if violation == 1:
            fixate_violation(whole_data[i])
    for i in absent_cars:
        whole_data.pop(i)
