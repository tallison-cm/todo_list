from enum import IntEnum

class StatusTarefa(IntEnum):
    CONCLUIDA = 1
    NAO_CONCLUIDA = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]