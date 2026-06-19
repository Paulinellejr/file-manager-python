import os
import datetime

from utils import format_size

def generate_report(directory_count, files_count, total_size, largest_file, largest_size ):
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = f"reports/report_{timestamp}.txt"
    with open(path, "w") as report:
        report.write("===== RELATÓRIO =====\n\n")

        report.write(f"Diretórios: {directory_count}\n")
        report.write(f"Arquivos: {files_count}\n")
        report.write(f"Tamanho Total: {format_size(total_size)}\n\n")

        report.write("Maior Arquivo:\n")
        report.write(f"{os.path.basename(largest_file)}\n")
        report.write("Tamanho:\n")
        report.write(f"{format_size(largest_size)}\n\n")

    print(f"Relatório salvo em: {path}")
