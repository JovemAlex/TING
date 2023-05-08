from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    file_text = txt_importer(instance._files[0])

    for line in file_text:
        if word.lower() not in line.lower():
            return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
