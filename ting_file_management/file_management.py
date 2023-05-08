import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith('.txt'):
            sys.stderr.write('Formato inválido')

        with open(path_file, "r") as txtfile:
            file_content = txtfile.read().split("\n")

            return file_content

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
