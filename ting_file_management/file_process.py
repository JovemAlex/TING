import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file not in instance._files:
        file_lines = txt_importer(path_file)
        instance.enqueue(path_file)
        value_enqueued = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_lines),
            "linhas_do_arquivo": file_lines,
        }
        print(f"{value_enqueued}", file=sys.stdout)


def remove(instance):
    try:
        files = instance._files
        file_name = instance._files[0]

        if not len(files):
            print("Não há elementos", file=sys.stdout)

        instance.dequeue()

        print(
            f"Arquivo {file_name} removido com sucesso",
            file=sys.stdout,
        )

    except IndexError:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    try:
        files = instance._files
        file_exact = files[position]

        if position not in files:
            print("Posição inválida", file=sys.stderr)

        file_lines = txt_importer(file_exact)

        meta = {
            "nome_do_arquivo": file_exact,
            "qtd_linhas": len(file_lines),
            "linhas_do_arquivo": file_lines,
        }

        print(meta, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
