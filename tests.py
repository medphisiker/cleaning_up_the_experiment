from cleaning_up_the_experiment import remove_in_place, create_filtered_copy


def test(func):
    # Тест из условия задачи
    assert func([1, 2, -1, 4, 5, -1, 6]) == [1, 2, 4, 5, 6]
    # Тест удаления всех элементов
    assert func([1, 1, 1], 1) == []
    # Тест отсутствия элемента
    assert func([1, 2, 3], 4) == [1, 2, 3]
    # Тест сохранения порядка
    assert func([3, 2, 1], 2) == [3, 1]


if __name__ == "__main__":
    test(remove_in_place)
    test(create_filtered_copy)
