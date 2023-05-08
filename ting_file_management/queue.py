from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._files = list()

    def __len__(self):
        return len(self._files)

    def enqueue(self, value):
        self._files.append(value)

    def dequeue(self):
        if len(self._files) == 0:
            return None
        return self._files.pop(0)

    def search(self, index):
        try:
            if index < 0 or index > len(self._files):
                raise IndexError
            return self._files[index]
        except IndexError:
            raise IndexError("Índice Inválido ou Inexistente")
