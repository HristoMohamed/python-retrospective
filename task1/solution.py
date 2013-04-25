#!/usr/bin/env python


def what_is_my_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 20):
        print('Овен')
        return 'Овен'
    if (month == 4 and day >= 21) or (month == 5 and day <= 20):
        print('Телец')
        return 'Телец'
    if (month == 5 and day >= 21) or (month == 6 and day <= 20):
        print('Близнаци')
        return 'Близнаци'
    if (month == 6 and day >= 21) or (month == 7 and day <= 21):
        print('Рак')
        return 'Рак'
    if (month == 7 and day >= 22) or (month == 8 and day <= 22):
        print('Лъв')
        return 'Лъв'
    if (month == 8 and day >= 23) or (month == 9 and day <= 22):
        print('Дева')
        return 'Дева'
    if (month == 9 and day >= 23) or (month == 10 and day <= 22):
        print('Везни')
        return 'Везни'
    if (month == 10 and day >= 23) or (month == 11 and day <= 21):
        print('Скорпион')
        return 'Скорпион'
    if (month == 11 and day >= 22) or (month == 12 and day <= 21):
        print('Стрелец')
        return 'Стрелец'
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        print('Козирог')
        return 'Козирог'
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        print('Водолей')
        return 'Водолей'
    if (month == 2 and day >= 19) or (month == 3 and day <= 20):
        print('Риби')
        return 'Риби'
