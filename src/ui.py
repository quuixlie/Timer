import curses
from src.font import font
import os

def display(stdscr, text, text_color = "green"):
    __set_color(text_color)
    __display_text(stdscr, text)

def __set_color(text_color):
    match text_color:
        case "black":
            curses.init_pair(1, curses.COLOR_BLACK, -1)
        case "red":
            curses.init_pair(1, curses.COLOR_RED, -1)
        case "green":
            curses.init_pair(1, curses.COLOR_GREEN, -1)
        case "yellow":
            curses.init_pair(1, curses.COLOR_YELLOW, -1)
        case "blue":
            curses.init_pair(1, curses.COLOR_BLUE, -1)
        case "magenta":
            curses.init_pair(1, curses.COLOR_MAGENTA, -1)
        case "cyan":
            curses.init_pair(1, curses.COLOR_CYAN, -1)
        case "white":
            curses.init_pair(1, curses.COLOR_WHITE, -1)        
        case _:
            curses.init_pair(1, -1, -1) # default terminal colors

def __display_text(stdscr, text):
    stdscr.clear()
    
    formatted_text = [font[char] for char in text]
    height, width = stdscr.getmaxyx()
    start_x = (width // 2)
    x_offset = 0
    
    for char in text: 
        x_offset += len(font[char][0])
        
    start_x = start_x - (x_offset - 1) // 2
    start_y = (height // 2) - (len(font["0"]) - 2) // 2
    
    for i, digit_ascii in enumerate(formatted_text):
        __display_char(stdscr, digit_ascii, start_y, start_x)
        start_x += (len(font[text[i]][0])) # Add additional letter spacing here if you want

def __display_char(stdscr, text, start_y, start_x):
    try:
        for i, line in enumerate(text):
            stdscr.addstr(start_y + i, start_x, line, curses.color_pair(1))
    except: 
        pass
    stdscr.refresh()
    
def init_ui():
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    __set_color("default")
    
    return stdscr

def destroy_ui():
    curses.endwin()

    os._exit(0)
