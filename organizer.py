import os
from utils import progress_bar


CATEGORIES = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".odt": "Documents",

    ".jpg": "Images",
    ".png": "Images",
    ".tiff": "Images",
    ".bmp": "Images",
    ".ico": "Images",
    ".heic": "Images",

    ".mp4": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".webm": "Videos",
    ".wmv": "Videos",

    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",

    ".deb": "Packaged",
    ".rpm": "Packaged",
}


def move_file(entry, folder_name, path):
    os.makedirs(folder_name, exist_ok=True)

    source = os.path.join(path, entry.name)
    destination = os.path.join(folder_name, entry.name)

    os.rename(source, destination)


def organize_directory(path):
    organized_files = {}

    if not os.path.exists(path):
        raise FileNotFoundError("O caminho informado não existe.")

    if not os.path.isdir(path):
        raise NotADirectoryError("O caminho informado não é um diretório.")

    files = [
        entry
        for entry in os.scandir(path)
        if entry.is_file()
    ]

    total_files = len(files)

    if total_files == 0:
        return 0

    moved_files = 0

    for index, entry in enumerate(files, start=1):
        _, extension = os.path.splitext(entry.name)

        folder_name = CATEGORIES.get(extension.lower(), "Others")
        organized_files[folder_name] = (organized_files.get(folder_name, 0) + 1)
        target_folder = os.path.join(path, folder_name)

        move_file(entry, target_folder, path)

        moved_files += 1
        progress_bar(index, total_files)

    print()

    return moved_files, organized_files
