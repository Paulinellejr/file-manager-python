import os
import time
from InquirerPy import inquirer
from scanner import scan_directory
from reports import generate_report
from organizer import organize_directory
from utils import clean_terminal, format_size
from search import search_files

def analyze_path():
    path = input("Informe o caminho: ")
    return scan_directory(path)



def banner():
    print(r"""
███████╗███╗   ███╗   ██████╗ ██╗   ██╗
██╔════╝████╗ ████║   ██╔══██╗╚██╗ ██╔╝
█████╗  ██╔████╔██║   ██████╔╝ ╚████╔╝
██╔══╝  ██║╚██╔╝██║   ██╔═══╝   ╚██╔╝
██║     ██║ ╚═╝ ██║██╗██║        ██║
╚═╝     ╚═╝     ╚═╝╚═╝╚═╝        ╚═╝""")
    print("           Python File Manager v1.0")
    print("=" * 50)



def pause():
    input("\nEnter para continuar....")

def menu():
    banner()
    option = inquirer.select(
    message="O que deseja fazer?",
    choices=[
        "Analisar pasta",
        "Gerar relatório",
        "Organizar arquivos",
        "Buscar arquivo",
        "Sair"
    ],).execute()
    return option

def analyze_directory_option():
    directory_count, files_count, total_size, largest_file, largest_size = analyze_path()
    print("\n===== RESULTADO DA ANÁLISE =====\n")

    print(f"Diretórios: {directory_count}")
    print(f"Arquivos: {files_count}")
    print(f"Tamanho total: {format_size(total_size)}")
    print(f"Maior arquivo: {largest_file}")
    print(f"Tamanho do maior arquivo: {format_size(largest_size)}")

    report = inquirer.confirm(message="Gerar relatório?", default=True).execute()
    if report:
        generate_report(directory_count, files_count, total_size, largest_file, largest_size )
    pause()

def generate_report_option():
    directory_count, files_count, total_size, largest_file, largest_size =  analyze_path()
    generate_report(directory_count, files_count, total_size, largest_file, largest_size)
    pause()


def organize_directory_option():
    path = input("Informe o caminho: ")
    moved_files = organize_directory(path)
    print(f"\n{moved_files} organizado(s) com sucesso!")
    pause()

def search_file_option():
    path = input("Informe o caminho: ")
    filename = input("Informe o arquivo: ")
    results, total_file = search_files(path, filename)
    if results:
        print(f"{total_file} Arquivo(s) encontrado(s).")
        for folder, files in results.items():
            print(f"\n{os.path.basename(folder)}/")
            for index, file in enumerate(files):
                if index == len(files) - 1:
                    print(f"└── {file}")
                else:
                    print(f"├── {file}")
    else:
        print("Nenhum arquivo encontrado.")
    pause()



def main():
    while True:
        try:
            clean_terminal()
            option = menu()
            match option:
                case "Analisar pasta":
                    analyze_directory_option()
                case "Gerar relatório":
                    generate_report_option()
                case "Organizar arquivos":
                    organize_directory_option()
                case "Buscar arquivo":
                    search_file_option()
                case "Sair":
                    print("Saindo do programa...")
                    time.sleep(0.3)
                    clean_terminal()
                    break
                case _:
                    print("Opção Invalida. Por favor Selecione uma opção valida.")
        except (FileNotFoundError, NotADirectoryError) as e:
            print(f"\nErro: {e}")
            pause()

        except Exception as e:
            print(f"\nErro inesperado: {e}")
            pause()
            break

if __name__ == "__main__":
    main()
