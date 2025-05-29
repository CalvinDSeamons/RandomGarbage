import time
import threading
from random_word import RandomWords
import pyautogui
from pynput import keyboard

kill_switch = False
r = RandomWords()

# Kill switch listener
def on_press(key):
    global kill_switch
    try:
        if key.char == 'q':  # Press 'q' to quit
            print("Kill switch activated!")
            kill_switch = True
            return False
    except AttributeError:
        pass

def listen_for_kill_switch():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Send word to Messages
def send_random_word():
    word = r.get_random_word()
    print(f"Sending: {word}")
    pyautogui.typewrite(word)
    pyautogui.press('enter')

if __name__ == '__main__':
    listener_thread = threading.Thread(target=listen_for_kill_switch)
    listener_thread.start()

    print("Switch to Messages window. Starting in 5 seconds...")
    time.sleep(5)

    while not kill_switch:
        send_random_word()
        time.sleep(2)  # Wait 2 seconds between messages
