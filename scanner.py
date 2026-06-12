import os


def scan_directory(path):
    directory_count = 0
    files_count = 0
    total_size = 0
    largest_size = 0
    largest_file  = ''


    if not os.path.exists(path):
        raise FileNotFoundError("O caminho informado não existe.")

    if not os.path.isdir(path):
        raise NotADirectoryError("O caminho informado não é um diretório.")

    for root, dirs, files in os.walk(path):
        directory_count += len(dirs)
        files_count += len(files)
        for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                if largest_size < file_size:
                    largest_size = file_size
                    largest_file = file_path

                total_size += file_size

    return (directory_count, files_count, total_size, largest_file, largest_size)
