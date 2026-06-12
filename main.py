from scanner import scan_directory




def menu():
    print("\n")
    print("Welcome to the menu!")
    print("1 - Analisar pasta ")
    print("2 - Gerar relatório")
    print("3 - Sair")
    input_option = input("Please select an option: ")
    return input_option


def main():
    while True:
        option = menu()
        match option:
            case "1":
                try:
                    path = input("Informe o caminho: ")
                    directory_count, files_count, total_size, largest_file, largest_size = scan_directory(path)

                    print(f"Diretorios: {directory_count}")
                    print(f"Arquivos: {files_count}")
                    print(f"Tamanho total em bytes: {total_size}")
                    print(f"Maior arquivo: {largest_file}")
                    print(f"Tamanho: {largest_size}\n")
                    input("Enter para continuar....")

                except (FileNotFoundError, NotADirectoryError) as e:
                    print(f"Erro: {e}")

            case "2":
                print("You selected option 2")

            case "3":
                print("Saindo do programa...")
                break
            case _:
                print("Opção Invalida. Por favor Selecione uma opção valida.")



if __name__ == "__main__":
    main()
