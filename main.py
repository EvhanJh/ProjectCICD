"""App de test Project CI CD"""

def main(elem_x, elem_y):
    """

    :param elem_x: int
    :param elem_y: int
    :return: int
    """
    result_x = elem_x - elem_y
    return result_x + 1


def test_answer():
    assert main(3, 2) == 2


main(5, 2)
