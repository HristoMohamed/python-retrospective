#!/usr/bin/env python

def what_is_my_sign(day,month):

    HOROSCOPE_SIGNS = (
        (1,19, 'Козирог'),
        (2,18, 'Водолей'),
        (3,20, 'Риби'),
        (4,20, 'Овен'),
        (5,20, 'Телец'),
        (6,20, 'Близнаци'),
        (7,21, 'Рак'),
        (8,22, 'Лъв'),
        (9,22, 'Дева'),
        (10,22, 'Везни'),
        (11,21, 'Скорпион'),
        (12, 21, 'Стрелец')
    )
    
    for month_in_the_year in range(0,13):
        if HOROSCOPE_SIGNS[month_in_the_year][0] == month:
            if HOROSCOPE_SIGNS[month_in_the_year][1] >= day:
                return HOROSCOPE_SIGNS[month_in_the_year][2]
            if HOROSCOPE_SIGNS[month_in_the_year][1] < day:
                return HOROSCOPE_SIGNS[month_in_the_year+1][2]        


