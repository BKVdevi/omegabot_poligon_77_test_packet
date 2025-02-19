from omegabot_poligon77 import *

name_l = "bot2" #Обяательно 4 символа
name_r = "bot1" #Обяательно 4 символа

lines = [ # Передача линейных препятствий (для нанесения линии на карту робота нужно указать точку начала и конца)
            #Сюда можно запихнуть жд
        ]

obs_med = [ # Точки препятствий диаметром <= 0.54м
    [recalc_points_to_cords(8), recalc_points_to_cords(14)],    #Базы гееоскана удлинение
    [recalc_points_to_cords(8), recalc_points_to_cords(12)],    #Базы гееоскана удлинение
    [recalc_points_to_cords(8), recalc_points_to_cords(10)],    #Базы гееоскана удлинение
    [recalc_points_to_cords(8), recalc_points_to_cords(9)],     #Базы гееоскана удлинение
    [recalc_points_to_cords(10), recalc_points_to_cords(14)],    #Базы гееоскана удлинение
    [recalc_points_to_cords(10), recalc_points_to_cords(12)],    #Базы гееоскана удлинение
    [recalc_points_to_cords(10), recalc_points_to_cords(10)],    #Базы гееоскана удлинение
    [recalc_points_to_cords(10), recalc_points_to_cords(9)],     #Базы гееоскана удлинение

    [recalc_points_to_cords(45), recalc_points_to_cords(42)],    #Базы гееоскана удлинение
    [recalc_points_to_cords(45), recalc_points_to_cords(44)],    #Базы гееоскана удлинение
    [recalc_points_to_cords(45), recalc_points_to_cords(46)],    #Базы гееоскана удлинение
    [recalc_points_to_cords(45), recalc_points_to_cords(48)],     #Базы гееоскана удлинение
]

obs_large = [ # Точки препятствий диаметром < 0.9м
    [recalc_points_to_cords(23), recalc_points_to_cords(23)],   #Площадка зарядки прав
    [recalc_points_to_cords(24), recalc_points_to_cords(23)],   #Площадка зарядки прав
    [recalc_points_to_cords(22), recalc_points_to_cords(23)],   #Площадка зарядки прав
    [recalc_points_to_cords(23), recalc_points_to_cords(24)],   #Площадка зарядки прав
    [recalc_points_to_cords(23), recalc_points_to_cords(22)],   #Площадка зарядки прав
    [recalc_points_to_cords(32), recalc_points_to_cords(31)],   #Площадка зарядки лев
    [recalc_points_to_cords(33), recalc_points_to_cords(31)],   #Площадка зарядки лев
    [recalc_points_to_cords(31), recalc_points_to_cords(31)],   #Площадка зарядки лев
    [recalc_points_to_cords(32), recalc_points_to_cords(30)],   #Площадка зарядки лев
    [recalc_points_to_cords(32), recalc_points_to_cords(32)],   #Площадка зарядки лев
    [recalc_points_to_cords(2), recalc_points_to_cords(47)],    #Гора
]

sklads_l = { #Координаты складов
    "wood" : [recalc_points_to_cords(45), recalc_points_to_cords(32)], # левая сторона
    "kamen" : [recalc_points_to_cords(31), recalc_points_to_cords(48)],  # левая сторона
}

sklads_r = { #Координаты складов
    "wood" : [recalc_points_to_cords(23), recalc_points_to_cords(10)], # Правая сторона
    "kamen" : [recalc_points_to_cords(8), recalc_points_to_cords(26)],  # Правая сторона
}

vzaimosv = {    #Инфа о том, какие метки куда увозить (прописаны для правой и для левой стороны)
    "wood" : [0, 2],
    "kamen" : [4, 3]
}

home_point_r = [recalc_points_to_cords(8), recalc_points_to_cords(18)] #Точка дома прав, сюда бот вернется после выполнения миссии 
home_point_l = [recalc_points_to_cords(45), recalc_points_to_cords(38)] #Точка дома лев, сюда бот вернется после выполнения миссии 