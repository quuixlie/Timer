from src.ui import init_ui, destroy_ui, display
from src.pomodoro_timer import get_formatted_time, start_timer, get_timer_status
from src.input_handler import get_user_input
from time import sleep
import keyboard

stdscr = init_ui()
work_time_in_seconds, break_time_in_seconds = get_user_input()
    
while True:
    start_timer(work_time_in_seconds)
    while get_timer_status():
        try:
            sleep(0.1)
            display(stdscr, get_formatted_time(), "green")  
        except:
            destroy_ui()
            
    start_timer(break_time_in_seconds)
    while get_timer_status():
        try:
            sleep(0.1)
            display(stdscr, get_formatted_time(), "green")  
        except:
            destroy_ui()
    sleep(0.1)