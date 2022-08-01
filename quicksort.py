
import sys
sys.setrecursionlimit(10000)


def sort(array: list[int]) -> list[int]:
    """
    Сортировка массива с помощью quicksort.
    """

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot: int = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)  
    else:
        return array


if __name__ == "__main__":
    pass