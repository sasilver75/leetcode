from UCSC.easy.118_pascals_triangle import 118_pascals_triangle
# This doesn't work becaause modules in python can't start with numbres.


def get_row(rowIndex: int) -> list[int]:
    return generate(rowIndex)[rowIndex]