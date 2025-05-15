def calc_bmi(hei:int,wei:int)->float: #指定型態
    if hei < 120 or hei > 220:
        raise Exception(f'輸入的身高: {hei} 公分 不在 120 ~ 220 範圍內')
    hei /= 1000
    if wei < 30.0 or wei > 200.0:
        raise Exception(f'輸入的體重: {wei:.2f} 公斤 不在 30 ~ 200 範圍內')
    return wei / hei ** 2

def check_bmi(bmi:float)->str:
    if bmi < 18.5:
        return '你的體重過輕'
    elif bmi < 24:
        return '你的體重正常'
    elif bmi < 27:
        return '你的體重稍微過重'
    elif bmi < 30:
        return '你已經輕度肥胖'
    elif bmi < 35:
        return '你已經中度肥胖'
    else:
        return '你已經重度肥胖'