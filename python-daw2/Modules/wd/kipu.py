import shutil
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, DirModifiedEvent, FileModifiedEvent

PATH = Path("C:/Users/Sergio/Downloads")

class EventHandler(FileSystemEventHandler):
    def __init__(self):
        self._categories = {
            "PDFs": ["pdf"],
            "Docs": ["odt", "odp", "doc", "docx", "ppt", "pptx", "txt", "rtf"],
            "Imágenes": ["jpg", "jpeg", "png", "gif", "bmp", "webp"],
            "Vídeos": ["mp4", "mkv", "avi", "mov", "wmv"],
            "Audio": ["mp3", "wav", "ogg", "flac"],
            "Aplicaciones": ["exe", "msi", "app", "bat"]
        }

    def on_created(self, event):
        file = Path(event.src_path)
        extension = file.suffix[1:]
        dest_dir = self.get_category(extension)

        print(f"Archivo creado: {event.src_path}")

    def on_deleted(self, event):
        print(f"Archivo eliminado: {event.src_path}")

    def on_modified(self, event):
        print(f"Archivo modificado: {event.src_path}")

    def get_category(self, extension):
        for category, extensions in self._categories.items():
            if extension in extensions:
                return category
        return "Otros"

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(EventHandler(),PATH, recursive=False)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()