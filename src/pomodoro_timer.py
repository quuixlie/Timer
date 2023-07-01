
from time import sleep
from threading import Thread
import threading


lock = threading.Lock()
__time_in_seconds = -1
__is_alive = False

def start_timer(time_in_seconds):
    global __time_in_seconds
    global __is_alive
    __is_alive = True
    __time_in_seconds = time_in_seconds
    
    timer = Thread(target=__countdown)
    timer.start()
    
def __countdown():
    global __time_in_seconds
    global __is_alive
    
    while __time_in_seconds > 0:
        sleep(1)
        lock.acquire()
        try:
            __time_in_seconds -= 1
        finally:
            lock.release()
            
    __is_alive = False
               
def get_formatted_time():
    global __time_in_seconds
    hours = __time_in_seconds // 3600
    minutes = (__time_in_seconds % 3600) // 60
    seconds = __time_in_seconds % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"

def get_timer_status():
    return __is_alive