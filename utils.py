import os



def clean_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def format_size(size):
    units = ["B", "KB", "MB", "GB"]
    unit_index = 0

    while size >= 1024 and unit_index < len(units) -1:
        size /= 1024
        unit_index += 1


    return f"{size:.2f} {units[unit_index]}"



def progress_bar(index, total_files):
    progress = index / total_files
    bar = "█" * int(progress * 20)
    print(f"\r[{bar:<20}] {progress:.0%}",end="")
