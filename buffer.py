from typing import Any, Iterable
from abc import ABC

import sys
sys.setrecursionlimit(10000)


class Cycle_buffer_FIFO_intrface(ABC):
    '''
    Интерфейс взаимодействия с классом буфера
    '''
    def __init__(self) -> None:
        pass

    def append(self, value: Any) -> None:
        '''
        Добавляем в конец буфера объект
        '''
        pass

    def get(self) -> Any:
        '''
        Забираем из начала буфера объект
        '''
        pass


class Cycle_buffer_FIFO(Cycle_buffer_FIFO_intrface):
    '''
    Циклический буфер First In First Out
    '''
    def __init__(self, size: int) -> None:
        self._size: int = size
        self._container: list[Any] = [].copy()

    def __str__(self) -> str:
        print(len(self._container))
        return str(self._container)

    def _is_full(self) -> bool:
        '''
        Переполнен ли контейнер
        '''
        if len(self._container) >= self._size:
            return True
        return False

    def append(self, value: Any) -> int or None:
        '''
        Добавляем в конец буфера объект
        '''
        if self._is_full():
            # Если переполнен выгружаем первый элемент
            self._container.append(value)
            return self._container.pop(0)
        else:
            self._container.append(value)

    def get(self) -> Any:
        '''
        Забираем из начала буфера объект
        '''
        return self._container.pop(0)


class Cycle_buffer_FIFO_child_of_list(list):
    '''
    Альтернативный буфер основанный на структуре list
    '''
    def __init__(self, _iterable: Iterable[Any] = []) -> None:
        super().__init__(_iterable)
        self._size: int = 6

    def _is_full(self) -> bool:
        '''
        Переполнен ли контейнер
        '''
        if len(self) >= self._size:
            return True
        return False

    def __add__(self, __x: Any) -> Any:
        self.append(__x)

    def __sub__(self, __x: Any) -> Any:
        super().pop(0)

    def append(self, __object: Any) -> None:
        '''
        Добавляем в конец буфера объект
        '''
        if self._is_full():
            # Если переполнен выгружаем первый элемент
            super().append(__object)
            return super().pop(0)
        return super().append(__object)

    def get(self) -> Any:
        '''
        Забираем из начала буфера объект
        '''
        return super().pop(0)


if __name__ == "__main__":
    pass