import curses
from font import font


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
    start_x = (width // 2) - (len(font["0"][0])) * (len(formatted_text) + 2) // 2
    start_y = (height // 2) - (len(font["0"]) - 2) // 2
    
    for i, digit_ascii in enumerate(formatted_text):
        start_x += (len(font["0"][0]))
        __display_char(stdscr, digit_ascii, start_y, start_x)

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
    exit(0)
