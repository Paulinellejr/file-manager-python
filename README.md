# Python File Manager

## 📖 Sobre o Projeto

O Python File Manager é uma aplicação de linha de comando desenvolvida para praticar manipulação de arquivos e diretórios utilizando a biblioteca `os` do Python.

O projeto permite analisar diretórios, gerar relatórios com informações detalhadas e organizar arquivos automaticamente em categorias com base em suas extensões.

---

## 🚀 Funcionalidades

### 📂 Análise de Diretórios

* Contagem de diretórios.
* Contagem de arquivos.
* Cálculo do tamanho total dos arquivos.
* Identificação do maior arquivo encontrado.

### 📝 Geração de Relatórios

* Criação automática de relatórios em arquivo `.txt`.
* Registro da data e hora da análise.
* Informações detalhadas sobre o diretório analisado.

### 🗂️ Organização de Arquivos

Os arquivos são organizados automaticamente em pastas de acordo com suas extensões.

Categorias suportadas:

| Categoria    | Extensões                                   |
| ------------ | ------------------------------------------- |
| Documents    | .pdf, .docx, .odt                           |
| Images       | .jpg, .jpeg, .png, .bmp, .tiff, .ico, .heic |
| Videos       | .mp4, .avi, .mkv, .mov, .wmv, .webm         |
| Audio        | .mp3, .wav, .flac                           |
| Spreadsheets | .xlsx, .xls, .csv, .ods                     |
| Others       | Arquivos não categorizados                  |

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Biblioteca os
* Biblioteca datetime

---

## 📁 Estrutura do Projeto

```text
python-file-manager/
│
├── main.py
├── scanner.py
├── organizer.py
├── reports.py
├── utils.py
├── search.py
│
├── reports/
│   └── report_YYYY-MM-DD_HH-MM-SS.txt
│
└── README.md
```

---

## ▶️ Como Executar

Clone o repositório:

```bash
git clone <url-do-repositorio>
```

Entre na pasta do projeto:

```bash
cd python-file-manager
```

Execute o programa:

```bash
python main.py
```

---

## 🎯 Objetivos de Aprendizado

Este projeto foi desenvolvido com o objetivo de praticar:

* Manipulação de arquivos e diretórios.
* Tratamento de exceções.
* Organização de código em módulos.
* Estruturas de dados (dicionários).
* Desenvolvimento de aplicações em linha de comando.
* Uso da biblioteca `os`.

---

## 📚 Conceitos Utilizados

Durante o desenvolvimento foram utilizados:

* `os.walk()`
* `os.scandir()`
* `os.path.exists()`
* `os.path.isdir()`
* `os.path.join()`
* `os.path.splitext()`
* `os.path.basename()`
* `os.makedirs()`
* `os.rename()`

---

## 🔮 Melhorias Futuras

* Identificação de arquivos duplicados.
* Backup automático antes da organização.
* Exportação de relatórios em CSV.
* Interface gráfica.
* Testes automatizados.

---

## 👨‍💻 Autor

Desenvolvido por Paulinelle Junior como projeto de estudo para aprofundar conhecimentos em Python e manipulação do sistema de arquivos.
