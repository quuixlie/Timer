import curses
import os
import signal
import random
from time import sleep
from multiprocessing import Process
import pygame

from src.font import font


__stdscr = None
__text_to_display = None
__sound_process = None
__default_color = "white"
__sound_was_played = False

def get_pressed_key():
    global __stdscr
    return __stdscr.getch()

def handle_terminal_resize(signal, frame):
    global __text_to_display
    
    curses.endwin()
    init_ui()
    __display_text()

def init_ui():
    global __stdscr
    global __default_color
    __stdscr = curses.initscr()
    __stdscr.clear()
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    set_color(__default_color)
    signal.signal(signal.SIGWINCH, handle_terminal_resize)

def destroy_ui():
    curses.nocbreak()
    curses.echo()
    curses.endwin()
    os._exit(0)

def display(text):
    global __text_to_display
    __text_to_display = text
    
    __display_text()

def __display_text():
    global __text_to_display
    global __stdscr
    formatted_text = [font[char] for char in __text_to_display]
    height, width = __stdscr.getmaxyx()
    x_offset = 0
    
    for char in __text_to_display: 
        x_offset += len(font[char][0])
        
    start_x = (width // 2) - (x_offset - 1) // 2
    start_y = (height // 2) - (len(font["0"]) - 2) // 2
    
    __stdscr.clear()
    
    for i, digit_ascii in enumerate(formatted_text):
        __display_char(digit_ascii, start_y, start_x)
        start_x += (len(font[__text_to_display[i]][0])) # Add additional letter spacing here if you want

def __display_char(text, start_y, start_x):
    global __stdscr
    
    try:
        for i, line in enumerate(text):
            __stdscr.addstr(start_y + i, start_x, line, curses.color_pair(1))
    except: 
        pass
    __stdscr.refresh()
    
def set_color(text_color):
    global __default_color
    __default_color = text_color
    
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

def play_sound(sound_name, duration):
    global __sound_process

    pygame.mixer.init()
    pygame.mixer.music.load(sound_name)
    pygame.mixer.music.play()
    sleep(duration)
  
    return 0
             
def play_confetti_animation():
    global __stdscr
    global __sound_process
    global __sound_was_played
    height, width = __stdscr.getmaxyx()
    confetti_speed = []
    confetti_positions = []
    confetti_directions = []
    for i in range(2, curses.COLORS):
        curses.init_pair(i, i, -1)
    off_screen = False
    total_off_screan = 0
    total_confetti = 0
    
    if not __sound_was_played:
        __sound_was_played = True
        __sound_process = Process(target=play_sound, args=(r"assets/success.mp3", 4))
        __sound_process.start()
    
    while True:
        if not off_screen:
            for i in range(10):
                x = width // 2
                y = random.uniform(-2, 0)
                angle = random.uniform(-5, 5)
                confetti_positions.append([x, y])
                confetti_directions.append(angle)
                total_confetti += 1
                if i > 80:
                    confetti_speed.append(random.uniform(2, 3))
                elif i <= 80:
                    confetti_speed.append(random.uniform(0.3,2))
        
        __stdscr.clear()
        
        for i in range(len(confetti_positions)):
            x, y = confetti_positions[i]
            angle = confetti_directions[i]
            x += confetti_speed[i] * angle
            y += confetti_speed[i]
            confetti_positions[i] = [x, y]
            
            if x > width and y > height:
                off_screen = True
            if y > height * 10:
                total_off_screan += 1

            confetti_char = "█"
            confetti_color = random.randint(1, curses.COLORS)
            try:
                __stdscr.addstr(int(y), int(x), confetti_char, curses.color_pair(confetti_color))
            except:
                pass
            
        if total_off_screan >= total_confetti:
            break
            
        __stdscr.refresh()
        sleep(0.01)
