from omegabot_poligon77 import *
import multiprocessing
from omegabot_basic import *


if __name__ == "__main__":
   
    try: # Пример задания для 1 омеги

        ip = "10.1.100.22"
        targets = { # Если оставить пустым, то бот сразу отправится домой
            "box" : [recalc_points_to_cords(26), recalc_points_to_cords(33)], # Для левой стороны
            "something" : [recalc_points_to_cords(33), recalc_points_to_cords(25)],  # Для левой стороны
        }
        process1_bot = multiprocessing.Process(target=bot_process, daemon=True, args=[ip, name_l, targets, lines, obs_med, obs_large, home_point_l, sklads_l, vzaimosv])
        process1_bot.start()

        ip = "10.1.100.39"
        targets = { # Если оставить пустым, то бот сразу отправится домой
            "box" : [recalc_points_to_cords(12), recalc_points_to_cords(42)], # Для правой стороны
            "something" : [recalc_points_to_cords(17), recalc_points_to_cords(37)],  # Для правой стороны
        }
        process2_bot = multiprocessing.Process(target=bot_process, daemon=True, args=[ip, name_r, targets, lines, obs_med, obs_large, home_point_r, sklads_r, vzaimosv])
        process2_bot.start()

        while True:
            pass

    except KeyboardInterrupt:
        print("END")

