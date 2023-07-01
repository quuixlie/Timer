from curses import *
from time import sleep
from font import font

def __init_ui():
    stdscr = initscr()
    curs_set(0)
    start_color()
    use_default_colors()
    __set_color("default")
    
    return stdscr
    
def __set_color(text_color):
    match text_color:
        case "black":
            init_pair(1, COLOR_BLACK, -1)
        case "red":
            init_pair(1, COLOR_RED, -1)
        case "green":
            init_pair(1, COLOR_GREEN, -1)
        case "yellow":
            init_pair(1, COLOR_YELLOW, -1)
        case "blue":
            init_pair(1, COLOR_BLUE, -1)
        case "magenta":
            init_pair(1, COLOR_MAGENTA, -1)
        case "cyan":
            init_pair(1, COLOR_CYAN, -1)
        case "white":
            init_pair(1, COLOR_WHITE, -1)        
        case _:
            init_pair(1, -1, -1) # default terminal colors

def __destroy_ui():
    endwin()
    exit(0)

def __display_char(stdscr, text, start_y, start_x):
    # if user will resize the terminal, then we can't write a char on non existing position
    # but it's okey, just wait to again resize from user
    try:
        for i, line in enumerate(text):
            stdscr.addstr(start_y + i, start_x, line, color_pair(1))
    except: 
        pass
    stdscr.refresh()
    
def __display_text(stdscr, text):
    stdscr.clear()
    
    formatted_text = [font[char] for char in text]
    
    height, width = stdscr.getmaxyx()
    start_x = (width // 2) - (len(font["0"][0])) * (len(formatted_text) + 2) // 2
    start_y = (height // 2) - (len(font["0"]) - 2) // 2
    
    for i, digit_ascii in enumerate(formatted_text):
        start_x += (len(font["0"][0]))
        __display_char(stdscr, digit_ascii, start_y, start_x)

def display(stdscr, text, text_color = "green"):
    __set_color(text_color)
    __display_text(stdscr, text)

stdscr = __init_ui()
while True:
    display(stdscr, "23:45:12:43:12", "red")
    
    sleep(0.01)

__destroy_ui()