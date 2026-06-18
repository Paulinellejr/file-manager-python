import os
from utils import progress_bar


def move_file(entry, folder_name, path):
    os.makedirs(folder_name, exist_ok=True)
    source = os.path.join(path, entry.name)
    destination = os.path.join(folder_name, entry.name)
    os.rename(source, destination)
    return 1


def organize_directory(path):

    if not os.path.exists(path):
        raise FileNotFoundError("O caminho informado não existe.")

    if not os.path.isdir(path):
        raise NotADirectoryError("O caminho informado não é um diretório.")
    categories = {
                    ".pdf":  "Documents",
                    ".docx": "Documents",
                    ".odt":  "Documents",

                    ".jpg":  "Images",
                    ".png":  "Images",
                    ".tiff": "Images",
                    ".bmp":  "Images",
                    ".ico":  "Images",
                    ".heic": "Images",

                    ".mp4":  "Videos",
                    ".avi":  "Videos",
                    ".mkv":  "Videos",
                    ".mov":  "Videos",
                    ".webm": "Videos",
                    ".wmv":  "Videos",

                    ".mp3":  "Audio",
                    ".wav":  "Audio",
                    ".flac": "Audio",

                    ".deb": "Packaged",
                    ".rpm": "Packaged", 
                }
    moved_files = 0
    with os.scandir(path) as entries:
        files = [
            entry
            for entry in os.scandir(path)
            if entry.is_file()
        ]

        total_files = len(files)

        for index, entry in enumerate(files, start=1):
            if entry.is_file():
                _, extension  = os.path.splitext(entry.name)
                folder_name = categories.get(extension.lower(), "Others")
                target_folder = os.path.join(path, folder_name)
                moved_files += move_file(entry, target_folder, path)
                progress_bar(index, total_files)
    return  moved_files
