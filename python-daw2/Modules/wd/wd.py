import sys
import time
import shutil
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Clase que organiza los archivos automáticamente
class OrganizadorArchivos(FileSystemEventHandler):

    # Constructor de la clase
    def __init__(self, carpeta_base):
        self.carpeta_base = Path(carpeta_base).resolve()  # Ruta absoluta base

        # Diccionario que relaciona categorías con extensiones
        self.categorias = {
            "PDFs": ["pdf"],
            "Docs": ["odt", "odp", "doc", "docx", "ppt", "pptx", "txt", "rtf"],
            "Imágenes": ["jpg", "jpeg", "png", "gif", "bmp", "webp"],
            "Vídeos": ["mp4", "mkv", "avi", "mov", "wmv"],
            "Audio": ["mp3", "wav", "ogg", "flac"],
            "Aplicaciones": ["exe", "msi", "app", "bat"]
        }

    # Ejecutar cuando se crea un nuevo archivo
    def on_created(self, event):
        if event.is_directory:  # Ignorar si es una carpeta
            return

        archivo = Path(event.src_path)  # Ruta del archivo detectado

        # Ignorar archivos temporales de descarga
        if archivo.suffix.lower() in [".tmp", ".crdownload", ".part"]:
            return

        # Esperar a que el archivo deje de estar en uso
        if not self.esperar_archivo_libre(archivo):
            print(f"[WARNING] {archivo.name} sigue en uso.")
            return

        # Obtener extensión sin punto y en minúsculas
        extension = archivo.suffix.lower().replace(".", "")

        # Determinar categoría correspondiente
        categoria_destino = self.obtener_categoria(extension)

        # Crear carpeta destino si no existe
        carpeta_destino = self.carpeta_base / categoria_destino
        carpeta_destino.mkdir(exist_ok=True)

        # Construir ruta final del archivo
        destino_final = carpeta_destino / archivo.name

        # Evitar sobreescritura si ya existe
        destino_final = self.evitar_colision(destino_final)

        try:
            shutil.move(str(archivo), str(destino_final))  # Mover archivo
            print(f"[OK] {archivo.name} → {categoria_destino}")
        except Exception as e:
            print(f"[ERROR] No se pudo mover {archivo.name}: {e}")

    # Ejecutar cuando un archivo es renombrado o movido
    def on_moved(self, event):

        if event.is_directory:  # Ignorar si es una carpeta
            return

        archivo = Path(event.dest_path)  # Ruta final tras el movimiento/renombrado

        # Ignorar archivos temporales del navegador
        if archivo.suffix.lower() in [".tmp", ".crdownload", ".part"]:
            return

        # Esperar a que el archivo deje de estar en uso
        if not self.esperar_archivo_libre(archivo):
            print(f"[WARNING] {archivo.name} sigue en uso.")
            return

        # Obtener extensión sin punto y en minúsculas
        extension = archivo.suffix.lower().replace(".", "")

        # Determinar categoría correspondiente
        categoria_destino = self.obtener_categoria(extension)

        # Crear carpeta destino si no existe
        carpeta_destino = self.carpeta_base / categoria_destino
        carpeta_destino.mkdir(exist_ok=True)

        # Construir ruta final del archivo
        destino_final = carpeta_destino / archivo.name

        # Evitar sobreescritura si ya existe
        destino_final = self.evitar_colision(destino_final)

        try:
            shutil.move(str(archivo), str(destino_final))  # Mover archivo
            print(f"[OK] {archivo.name} → {categoria_destino}")
        except Exception as e:
            print(f"[ERROR] No se pudo mover {archivo.name}: {e}")

    # Determina la categoría según extensión
    def obtener_categoria(self, extension):
        for categoria, extensiones in self.categorias.items():
            if extension in extensiones:
                return categoria
        return "Otros"  # Categoría por defecto

    # Espera hasta que el archivo no esté bloqueado
    def esperar_archivo_libre(self, archivo, intentos=10):
        for _ in range(intentos):
            try:
                with open(archivo, "rb"):
                    return True
            except PermissionError:
                time.sleep(0.5)
            except FileNotFoundError:
                return False
        return False

    # Evita sobrescribir archivos existentes
    def evitar_colision(self, destino):
        contador = 1
        nuevo_destino = destino

        while nuevo_destino.exists():
            nuevo_destino = destino.parent / f"{destino.stem}_{contador}{destino.suffix}"
            contador += 1

        return nuevo_destino


# Punto de entrada del programa
if __name__ == "__main__":

    # Si se pasa argumento, usar esa ruta
    if len(sys.argv) > 1:
        carpeta = Path(sys.argv[1]).resolve()
    else:
        carpeta = Path.home() / "Downloads"  # Carpeta Descargas del sistema

    # Verificar que la carpeta exista
    if not carpeta.exists():
        print("La carpeta indicada no existe.")
        sys.exit(1)

    event_handler = OrganizadorArchivos(carpeta)  # Crear handler
    observer = Observer()  # Crear monitor

    observer.schedule(event_handler, str(carpeta), recursive=False)  # Asignar carpeta
    observer.start()  # Iniciar monitorización

    print(f"Monitorizando: {carpeta}")

    try:
        while True:  # Mantener programa activo
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()   # Detener monitor
        observer.join()   # Esperar cierre correcto