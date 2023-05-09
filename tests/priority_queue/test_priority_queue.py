from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    mock = [
        {
            "nome_do_arquivo": "file 1",
            "qtd_linhas": 6,
            "linhas_do_arquivo": [1, 2, 3, 4, 5, 6],
        },
        {
            "nome_do_arquivo": "file 2",
            "qtd_linhas": 3,
            "linhas_do_arquivo": [1, 2, 3],
        },
    ]

    priority_class = PriorityQueue()

    for file in mock:
        priority_class.enqueue(file)

    # testa se o length é do mesmo tamanho do mock após ser
    # adicionado os arquivos
    assert len(mock) == priority_class.__len__()

    # testa prioridade dos arquivos
    assert priority_class.is_priority(mock[0]) is False
    assert priority_class.is_priority(mock[1]) is True

    # testa a função search
    assert (
        priority_class.search(1)["nome_do_arquivo"]
        == mock[0]["nome_do_arquivo"]
    )
    assert (
        priority_class.search(0)["nome_do_arquivo"]
        == mock[1]["nome_do_arquivo"]
    )

    # testa a função dequeue e verifica se ao fazer o dequeue o
    # length é o mesmo
    priority_class.dequeue()
    assert len(priority_class) == 1
    priority_class.dequeue()
    assert len(priority_class) == 0

    # testa a exceção da class ao passar um índice inválido
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_class.search(8000)
