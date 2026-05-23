import threading
import time

def hervir_agua():
    print("Encendiendo el fuego\n")
    time.sleep(3)
    print("El agua está lista!")

if __name__ == "__main__":
    thread = threading.Thread(target=hervir_agua)
    thread.start()
    print("Me voy a ver la tele mientras tanto.")
