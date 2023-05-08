def exists_word(word, instance):

    message = list()
    ocurrences = list()

    for file in instance._files:

        for index, linha in enumerate(file["linhas_do_arquivo"], start=1):
            if word.lower() in linha.lower():
                ocurrences.append({"linha": index + 1})

        result = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": ocurrences,
        }

        message.append(result)

    return message


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
