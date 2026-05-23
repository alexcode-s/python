import threading
import time
from threading import Thread

ahorros = 0

def depositar_dinero():
    global ahorros
    ahorros += 100
    print(ahorros)

if __name__ == "__main__":
    for _ in range(5):
        t = threading.Thread(target=depositar_dinero())
        t.start()
        time.sleep(1)