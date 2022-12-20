import re


def get_coordinates_tuple(coordinates) -> tuple:
    """
    to separate the columns and row index
    :param coordinates:
    :return: x, y
    """
    reg_exp = re.compile(r"([A-Z]+)(\d+)")
    res = re.findall(reg_exp, coordinates)
    if res:
        x, y = res[0]
        return x, int(y)
    return None, None

