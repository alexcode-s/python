import threading
import time


def descargar_archivo(nombre, tiempo):
    print(f"Descargando: {nombre}")
    time.sleep(tiempo)
    print(f"Tiempo estimado: {tiempo}")

if __name__ == "__main__":
    archivos_a_descargar = [
        ("Pelicula.mp4", 5),
        ("Cancion.mp3", 2),
        ("Libro.pdf", 1),
        ("Juego.exe", 4)
    ]
    threads = []

    for nombre, tiempo in archivos_a_descargar:
        t = threading.Thread(target=descargar_archivo, args=(nombre, tiempo))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

