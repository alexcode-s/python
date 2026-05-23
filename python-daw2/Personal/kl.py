from pynput.keyboard import Key, Listener

def show(key):
    if key == Key.space:
        print(" ", end="", flush=True)

    elif key == Key.backspace or key == Key.shift:
        print("", end="", flush=True)

    elif key == Key.enter:
        print()

    elif hasattr(key, 'char') and key.char is not None:
        print(key.char, end="", flush=True)

    else:
        print(f'[{key}]', end="", flush=True)

with Listener(on_press=show) as listener:
    listener.join()