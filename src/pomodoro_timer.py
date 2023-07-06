
from time import sleep
from threading import Thread

from src.ui import display, get_pressed_key, destroy_ui


__time_in_seconds = -1
__is_paused = False
__is_timmer_running = False

def __handle_timer_shortcuts():
    global __is_timmer_running
    
    while __is_timmer_running:
        match get_pressed_key():
            case 32: # space
                pause_timer()
            case 113: # q
                destroy_ui()
            case _:
                pass

def start_timer(time_in_seconds):
    global __time_in_seconds
    global __is_timmer_running
    __time_in_seconds = time_in_seconds

    if not __is_timmer_running:
        __is_timmer_running = True
        handler = Thread(target=__handle_timer_shortcuts)
        handler.start()
    
    timer = Thread(target=__countdown)
    timer.start()
    timer.join()
    
def __countdown():
    global __time_in_seconds
    global __is_paused
    
    while __time_in_seconds >= 0:
        if not __is_paused:
            display(get_formatted_time())
            sleep(1)
            __time_in_seconds -= 1

    return 0 
               
def get_formatted_time():
    global __time_in_seconds
    hours = __time_in_seconds // 3600
    minutes = (__time_in_seconds % 3600) // 60
    seconds = __time_in_seconds % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"

def pause_timer():
    global __is_paused

    if not __is_paused:
        __is_paused = True
        display("PAUSED")
    else:
        __is_paused = False

