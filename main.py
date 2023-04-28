# Часть функций написаны с допущением, что список whole_data не пустой
# При сборке системы воедино следует перед активацией функций check и checking_for_left убедиться в том, что whole_data не пуст

whole_data = [
    {"GRZ":"AA000A96", "LAST_TIME":"12:43:55", "DATE":"15.04.2023", "LIGHTS":[0,1,1,1,1,0,1]},
    {"GRZ":"AA001A96", "LAST_TIME":"12:43:54", "DATE":"15.04.2023", "LIGHTS":[0,0,1,0,1,0,0,0,0,1]},
    {"GRZ":"AA002A96", "LAST_TIME":"12:43:55", "DATE":"15.04.2023", "LIGHTS":[0,1,1]},
    {"GRZ":"AA003A96", "LAST_TIME":"12:43:55", "DATE":"15.04.2023", "LIGHTS":[1,1,1,0,1]},
    {"GRZ":"AA004A96", "LAST_TIME":"12:43:55", "DATE":"15.04.2023", "LIGHTS":[0,1,1,0,0,1]},
    {"GRZ":"AA005A96", "LAST_TIME":"12:43:55", "DATE":"15.04.2023", "LIGHTS":[1,1,1,1,1,1,1]},
    {"GRZ":"AA006A96", "LAST_TIME":"12:43:55", "DATE":"15.04.2023", "LIGHTS":[0]}
]
dct = {"GRZ":"AA000A96", "TIME":"12:43:56", "DATE":"15.04.2023", "LIGHTS":1}
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

# Не забыть когда-нибудь прописать эту функцию
def fixate_violation(dct):
    pass

def check(dct, whole_data):
    for i in range(len(whole_data)):
        if whole_data[i]["GRZ"]==dct["GRZ"]:
            return i
        else:
            return -1

# Данная функция должна активироваться только если функция check вернула не -1
def new_data(dct, whole_data):
    place = check(dct, whole_data)
    whole_data[place]["LIGHTS"].append(dct["LIGHTS"])
    whole_data[place]["LAST_TIME"] = dct["TIME"]
    whole_data[place]["DATE"] = dct["DATE"]

# Данная функция должна активироваться только если функция check вернула -1
def new_car(dct, whole_data):
    new_dct = dct
    new_dct["LIGHTS"] = [dct["LIGHTS"]]
    whole_data.append(new_dct)

# В данной функции мы прогоняем все элементы нашего списка по циклу
# Если какого-то из автомобилей не было больше 10-ти секунд, то определяем, присутствовало ли нарушение
# Если присутствовало, то выписываем штраф
# (функция выписки штрафа не реализована)
# В самом конце удаляем данные об автомобиле из локальной базы
def checking_for_left(REAL_TIME, whole_data):
    timestamp0 = REAL_TIME.split(":")
    timestamp = []
    for i in range(3):
        timestamp.append(int(timestamp0[i]))
    for i in range(len(whole_data)):
        if whole_data[i]["LAST_TIME"] != REAL_TIME:
            last_time0 = whole_data[i]["LAST_TIME"].split(":")
            last_time = []
            res = ""
            for j in range(3):
                last_time.append(int(last_time0[j]))
            if last_time[2]+10 < timestamp[2]:
                res = "ABSENT"
            elif last_time[2] > timestamp[2]:
                if last_time[2]+10 < timestamp[2]+60:
                    res = "ABSENT"
            else:
                res = "PRESENT"

            if res == "ABSENT":
                violation = deside(whole_data[i]["LIGHTS"])
                if violation == 1:
                    fixate_violation(whole_data[i])
                whole_data.pop(i)
