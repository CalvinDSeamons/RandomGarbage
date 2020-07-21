"""I am new to bots, this I wouldn't even classify as such. I consider this
an advanced auto clicker that's very VERY easy to break. Nevertheless it
automates my tasks, specifcally the agility course around seers village in osrs.
Use at your own discression this may or may not result in a permaban. I use rng
combined with static pixel coor(X,Y) to determine the auto clicking for the
tasks.
"""

import errno
import json
import random
import sys
import time
import pynput
from pynput.mouse import Button, Controller, Listener 


coords = {}
coor_num = 0

def main():
    choice=input("Crap Autoclicker Bot V1.0\n"
                 "1.) Execute autoclicker script.\n"
                 "2.) Activate pixel locater/click location.\n"
                 "3.) Quit\n"
                 "---\nPress Ctrl-C at anytime to quit\n")
    if choice == "1":
        run_bot()
        # test()
    elif choice == "2":
        get_location()
    elif choice == "3":
        print("cya l8r Nerd!")
    else:
        return errno.EINVAL

                 
def on_click(x, y, button, pressed):
    global coor_num
    key = 'coord' + str(coor_num)
    print('x1: Y1{0} at {1}'.format(
        'x1' if pressed else 'Released',
        (x, y)))
    if str(button) == 'Button.right':
        return False
    coors = [x,y]
    if key in coords:
        coords[key].append(coors)
    else:
        coords.setdefault(key,[])
        coords[key].append(coors)
    if len(coords[key]) == 2:
        coor_num += 1
    


def test():
    mouse = Controller()
    #mouse.move(1019.50390625,157.23828125)
    mouse.position = (0,0)
    print(mouse.position)
    mouse.press(Button.right)
    mouse.release(Button.right)
    
def get_location():
    with Listener(
        on_move=False,
        on_click=on_click,
        on_scroll=False) as listener:
        listener.join()

    with open('coordiante_file', 'w+') as outfile:
        json.dump(coords,outfile)

        

def get_screen_size():

    return gui.size()

def setup_coor(x1,y1,x2,y2):
    xmin=-1
    xmax=-1
    ymin=-1
    ymax=-1
    coordinates = []
    if x1 < x2:
        xmin = x1
        xmax = x2
    else:
        xmax = x1
        xmin = x2
    if y1 < y2:
        ymin = y1
        ymax = y2
    else:
        ymin = y2
        ymax = y1

    final_x = random.randint(xmin,xmax)
    final_y = random.randint(ymin,ymax)
    coordinates = [final_x, final_y]

    return coordinates 
    
    

def run_bot():
    data = {}
    mouse = Controller()
    with open('coordiante_file') as input_file:
        data = json.load(input_file)

    time_interval = []
    while True:
        for key in data:
            time.sleep(2)
            coords = data[key]
            final_coor = setup_coor(int(coords[0][0]),
                                    int(coords[0][1]),
                                    int(coords[1][0]),
                                    int(coords[1][1]))
            
            mouse.position = (final_coor[0],final_coor[1])
            time.sleep(.2)
            mouse.press(Button.left)
            mouse.release(Button.left)
            sleepy = float(random.randint(700,900))/100
            time.sleep(sleepy)
              
    

main()
