import sys
import re


def __get_work_time():
    DAY = 86_400
    hours, minutes, seconds = (0, 0, 0)
    
    try:
        hours = re.search("[0-9]+[h]", sys.argv[1]).group(0)
        hours = int(hours[:len(hours) - 1])
    except AttributeError:
        pass # It's okey if the user will not specify this param
    try:
        minutes = re.search("[0-9]+[m]", sys.argv[1]).group(0)
        minutes = int(minutes[:len(minutes) - 1])
    except AttributeError:
        pass # It's okey if the user will not specify this param
    try:
        seconds = re.search("[0-9]+[s]", sys.argv[1]).group(0)
        seconds = int(seconds[:len(seconds) - 1])
    except AttributeError:
        pass # It's okey if the user will not specify this param
    
    total_in_seconds = hours * 3600 + minutes * 60 + seconds
    if (total_in_seconds == 0):
        print("Get to work! Working for such a short time will not bring you any results!") 
        print("Example usage: pomodorotimer 25m3s 1h2s")
        print("Where 25m3s is a work time and 1h2s is a break time")
        exit(1)
    elif (total_in_seconds > DAY):
        print("You fuc**** robot! The total working time cannot exceed 24 hours!")
        exit(1)
    else:
        return total_in_seconds
    
def __get_break_time():
    DAY = 86_400
    hours, minutes, seconds = (0, 0, 0)
    
    try:
        hours = re.search("[0-9]+[h]", sys.argv[2]).group(0)
        hours = int(hours[:len(hours) - 1])
    except AttributeError:
        pass # It's okey if the user will not specify this param
    try:
        minutes = re.search("[0-9]+[m]", sys.argv[2]).group(0)
        minutes = int(minutes[:len(minutes) - 1])
    except AttributeError:
        pass # It's okey if the user will not specify this param
    try:
        seconds = re.search("[0-9]+[s]", sys.argv[2]).group(0)
        seconds = int(seconds[:len(seconds) - 1])
    except AttributeError:
        pass # It's okey if the user will not specify this param
    
    total_in_seconds = hours * 3600 + minutes * 60 + seconds
    if (total_in_seconds == 0):
        print("You fuc**** robot! break time must be greater than 0!")
        print("Example usage: pomodorotimer 25m3s 1h2s")
        print("Where 25m3s is a work time and 1h2s is a break time")
        exit(1)
    elif (total_in_seconds > DAY):
        print("Get to work! Working for such a long time will not bring you any results!")
        exit(1)
    else:
        return total_in_seconds
    
def get_user_input():
    if (len(sys.argv) == 2 + 1): # 1 because sys.argv[0] returns "main.py" in this project
        return (__get_work_time(), __get_break_time())
    else:
        print("You must enter the working time and break time respectively!")
        print("Example usage: pomodorotimer 25m3s 1h2s")
        print("Where 25m3s is a work time and 1h2s is a break time")
        exit(1)
