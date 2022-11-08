from functools import reduce


def process_matrix(matrix):
    """
    Recibe una matriz y devuelve una nueva con los elementos cambiados. 
    Cada elemento dentro de la nueva matriz será el promedio del valor antiguo y el de sus 
    vecinos.
    """
    new_matrix = []
    for i, column in enumerate(matrix):
        sublists = []
        for j, value in enumerate(column):
            new_value = process_elements(i, j, matrix)
            sublists.append(new_value)
        new_matrix.append(sublists)
    return new_matrix


def process_elements(i, j, matrix):
    """
    Recibe los indices de los elementos y la matríz en la que están.
    Calcula su promedio con sus vecinos y devuelve el promedio.
    """
    indices = get_neighbour_indices(i, j, matrix)
    values = get_neighbour_values(indices, matrix)
    average = get_average(values)

    return average


def get_neighbour_indices(i, j, matrix):
    """
    Devuelve la lista de indices de los vecinos, incluído el propio elemento.
    (Primero consigue todos los índices y luego usando una función filter, filtra aquellos que son imposibles)
    """
    indices = []

    indices.append([i, j])
    indices.append([i, j + 1])
    indices.append([i, j - 1])
    indices.append([i + 1, j])
    indices.append([i - 1, j])

    def remove_invalid(coordenate):
        if coordenate[0] < 0 or coordenate[1] < 0:
            return False
        elif coordenate[0] > len(matrix) - 1 or coordenate[1] > len(matrix) - 1:
            return False
        else:
            return True

    indices = filter(remove_invalid, indices)

    return indices


def get_neighbour_values(indices, matrix):
    """
    Recibe los índices de los vecinos y propio, y devuelve sus valores.
    """
    values = []
    for index in indices:
        values.append(matrix[index[0]][index[1]])
    return values


def get_average(numbers):
    """"
    Recibe los valores de los vecinos y el propio, y devuelve su promedio.
    """
    return reduce(lambda accum, b: accum + b, numbers, 0) / len(numbers)
