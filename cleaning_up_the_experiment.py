def filter_arr1(arr: list, element: int) -> list:
    """
    Удаляет все вхождения заданного элемента из массива in-place.

    Args:
        arr (list): Исходный массив, который будет изменен.
        element (int): Элемент, который необходимо удалить.

    Returns:
        list: Измененный массив (исходный массив с удаленными элементами).

    Примечание:
        Временная сложность: O(n)
        Пространственная сложность: O(1)
    """
    idx = 0
    for value in arr:
        if value != element:
            arr[idx] = value
            idx += 1

    del arr[idx:]
    return arr


def filter_arr2(arr: list, element: int) -> list:
    """
    Создает новый массив без элементов, равных заданному.

    Args:
        arr (list): Исходный массив.
        element (int): Элемент, который необходимо исключить.

    Returns:
        list: Новый массив без указанного элемента.

    Примечание:
        Временная сложность: O(n)
        Пространственная сложность: O(n)
    """
    return [x for x in arr if x != element]


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    element = int(input())

    filter_arr1(arr, element)
    print(" ".join(str(value) for value in arr))
