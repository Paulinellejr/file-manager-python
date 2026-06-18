import os
import time
from scanner import scan_directory
from reports import generate_report
from organizer import organize_directory
from utils import clean_terminal, format_size


def analyze_path():
    path = input("Informe o caminho: ")
    return scan_directory(path)

def menu():
    print("Bem-vindo ao menu!")
    print("1 - Analisar pasta ")
    print("2 - Gerar relatório")
    print("3 - Organizador de diretorios")
    print("4 - Sair")
    input_option = input("Por favor, selecione uma opção: ")
    return input_option


def main():
    while True:
        clean_terminal()
        option = menu()
        match option:
            case "1":
                try:
                    directory_count, files_count, total_size, largest_file, largest_size = analyze_path()
                    print('\n')
                    print(f"Diretorios: {directory_count}")
                    print(f"Arquivos: {files_count}")
                    print(f"Tamanho total em bytes: {total_size}")
                    print(f"Maior arquivo: {largest_file}")
                    print(f"Tamanho: {format_size(largest_size)} \n")
                    op = input("Gera Relatorio? (s/n) ")
                    if op.lower() in ["s", "sim"]:
                        generate_report(directory_count, files_count, total_size, largest_file, largest_size )

                    input("Enter para continuar....")

                except (FileNotFoundError, NotADirectoryError) as e:
                    print(f"Erro: {e}")

            case "2":
                try:
                    directory_count, files_count, total_size, largest_file, largest_size =  analyze_path()
                    generate_report(directory_count, files_count, total_size, largest_file, largest_size)
                except (FileNotFoundError, NotADirectoryError) as e:
                    print(f"Erro: {e}")
            case "3":
                try:
                    path = input("Informe o caminho: ")
                    moved_files = organize_directory(path)
                    print(f"{moved_files} organizados com sucesso!\n")
                    input("Enter para continuar....")
                except (FileNotFoundError, NotADirectoryError) as e:
                    print(f"Erro: {e}")
            case "4":
                print("Saindo do programa...")
                time.sleep(0.3)
                clean_terminal()
                break
            case _:
                print("Opção Invalida. Por favor Selecione uma opção valida.")

if __name__ == "__main__":
    main()
