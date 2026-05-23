import threading
import time

def correr_caballo(nombre, tiempo_carrera):
    print(f"¡{nombre} ha salida de la meta!")
    time.sleep(tiempo_carrera)
    print(f"¡{nombre} ha cruzado la línea de meta!")

if __name__ == "__main__":
    t1 = threading.Thread(target=correr_caballo, args=("Relámpago", 2))
    t2 = threading.Thread(target=correr_caballo, args=("Tornado", 4))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("La carrera ha terminado, cierren las apuestas!")