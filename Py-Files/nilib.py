import literales as msg


def validate(missage, ini, fin):  # Funció que valida nombres enters segons el rang a trobar
    if fin is None:
        num = int(input(missage))
        while num < ini:
            num = int(input(missage))
    elif ini is None:
        num = int(input(missage))
        while num > fin:
            num = int(input(missage))
    elif ini is not None and fin is not None:
        num = int(input(missage))
        while num < ini or num > fin:
            num = int(input(missage))
    else:
        num = int(input(missage))
    return num


def val_month(num):  # Funcio que retorna el mes (str) introduïnt el seu nombre (int)
    if num == 1:
        return msg.MONTH1
    elif num == 2:
        return msg.MONTH2
    elif num == 3:
        return msg.MONTH3
    elif num == 4:
        return msg.MONTH4
    elif num == 5:
        return msg.MONTH5
    elif num == 6:
        return msg.MONTH6
    elif num == 7:
        return msg.MONTH7
    elif num == 8:
        return msg.MONTH8
    elif num == 9:
        return msg.MONTH9
    elif num == 10:
        return msg.MONTH10
    elif num == 11:
        return msg.MONTH11
    elif num == 12:
        return msg.MONTH12
