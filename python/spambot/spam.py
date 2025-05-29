import time
import threading
from random_word import RandomWords
import pyautogui
from pynput import keyboard
import hashlib


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
def send_random_word(key):
    word = r.get_random_word()
    hashing = md5_hash(key,word)
    print(f"Sending: {word}")
    pyautogui.typewrite(hashing)
    pyautogui.press('enter')

def md5_hash(key: str, word: str) -> str:
    combined = (key + word).encode('utf-8')
    return hashlib.md5(combined).hexdigest()


if __name__ == '__main__':
    listener_thread = threading.Thread(target=listen_for_kill_switch)
    listener_thread.start()

    print("Switch to Messages window. Starting in 5 seconds...")
    time.sleep(5)

    key = '95468401-5567-452E-A56B-E6255C34F7C9'
    phrase = ("MD5-Hashing: " +"["+key+"]")
    pyautogui.typewrite(phrase)
    pyautogui.press('enter')
    time.sleep(2)

    while not kill_switch:
        send_random_word(key)
        time.sleep(1)  # Wait 2 seconds between messages
