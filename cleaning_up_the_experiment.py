def remove_in_place(numbers: list, to_remove: int) -> list:
    """
    Удаляет все вхождения заданного элемента из массива in-place.

    Args:
        numbers (list): Исходный массив чисел, который будет изменен.
        to_remove (int): Элемент, который необходимо удалить.

    Returns:
        list: Измененный массив (исходный массив с удаленными элементами).

    Примечание:
        Временная сложность: O(n)
        Пространственная сложность: O(1)
    """
    write_index = 0
    for number in numbers:
        if number != to_remove:
            numbers[write_index] = number
            write_index += 1

    del numbers[write_index:]
    return numbers


def create_filtered_copy(numbers: list, to_remove: int) -> list:
    """
    Создает новый массив без элементов, равных заданному.

    Args:
        numbers (list): Исходный массив чисел.
        to_remove (int): Элемент, который необходимо исключить.

    Returns:
        list: Новый массив без указанного элемента.

    Примечание:
        Временная сложность: O(n)
        Пространственная сложность: O(n)
    """
    return [number for number in numbers if number != to_remove]


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    to_remove = int(input())

    remove_in_place(numbers, to_remove)
    print(" ".join(map(str, numbers)))
