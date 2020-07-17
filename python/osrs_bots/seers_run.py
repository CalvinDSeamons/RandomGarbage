"""I am new to bots, this I wouldn't even classify as such. I consider this
an advanced auto clicker that's very VERY easy to break. Nevertheless it
automates my tasks, specifcally the agility course around seers village in osrs.
Use at your own discression this may or may not result in a permaban. I use rng
combined with static pixel coor(X,Y) to determine the auto clicking for the
tasks.
"""

import pyautogui as gui
import sys
import errno

coords = []

def main():
    choice=input("Crap Autoclicker Bot V1.0\n"
                 "1.) Execute autoclicker script.\n"
                 "2.) Activate pixel locater/click location.\n"
                 "3.) Quit\n"
                 "---\nPress Ctrl-C at anytime to quit\n")
    if choice == 1:
       run_bot()
    elif choice == 2:
        get_location()
    elif choice == 3:
        print("cya l8r Nerd!")
    else:
        return errno.EINVAL
                 
    

def get_location():
    #  Straight up copied this from pyautogui.com aka Not Mine.
    try:
        while True:
            x,y = gui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            
            #print(positionStr, end='')
            #print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

def get_screen_size():

    return gui.size()


main()

gui.moveTo(883,715)
gui.click(clicks=2)
