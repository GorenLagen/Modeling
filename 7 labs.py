# Функция для создания исходной матрицы данных
def create_origin_data(p, q):
    matrix = []
    for i in range(3):
        row = []
        for j in range(5):
            if i == 0:
                row.append((10 if j % 2 == 0 else 5) * (p + q + 1 + 0.1 * (j + 1)))
            elif i == 1:
                row.append((0.5 if j % 2 == 0 else 1) * (p + q + 1 + 0.1 * (j + 1)))
            else:
                row.append((0.8 if j % 2 == 0 else 0.4) * (p + q + 1 + 0.1 * (j + 1)))
        matrix.append(row)
    return matrix

# Функция для вычисления коэффициентов целевой функции
def render_coefficients_function_table(matrix):
    a = matrix[0]
    b = matrix[1]
    w = matrix[2]
    coefficients = [[], []]
    for i in range(5):
        coefficients[0].append(round(-1 / b[i], 2))
        coefficients[1].append(round(a[i] / b[i] - w[i], 2))
    return coefficients

# Целевая функция
def objective_function(data, x):
    sum = 0
    for i in range(5):
        sum += -(1 / data[1][i]) * x[i]**2 + (data[0][i] / data[1][i] - data[2][i]) * x[i]
    return sum

# Функция для вычисления частной производной
def partial_derivative(axis, x, data):
    return (-data[2][axis] + (data[0][axis] / data[1][axis]) - (2 * x[axis] / data[1][axis]))

# Функция для вычисления градиента
def gradient(x, data):
    gradient = []
    for i in range(5):
        gradient.append(partial_derivative(i, x, data))
    return gradient

# Функция для создания случайного массива чисел
def create_random_number_array(min_val, max_val, dimensions):
    import random
    return [random.randint(min_val, max_val) for _ in range(dimensions)]

# Функция для проверки ограничения
def limitation(x):
    return sum(x)

# Метод градиентного подъема
def gradient_ascent(p, q):
    step_size = 0.05  # Размер шага
    dimensions = 5  # Количество переменных
    matrix_data = create_origin_data(p, q)  # Создание исходной матрицы данных
    count = 0  # Счетчик итераций

    # Шаг 1: Случайная стартовая точка
    x = create_random_number_array(0, 10, dimensions)

    while count < 1000:
        # Шаг 2: Вычисление частных производных
        gradient_values = gradient(x, matrix_data)

        # Шаг 3: Сделать небольшой шаг в направлении градиента
        for i in range(dimensions):
            x[i] = x[i] + step_size * gradient_values[i]

        count += 1

    return x, objective_function(matrix_data, x)


p = 0
q = 0
x, solve = gradient_ascent(p, q)
print("-----------------------------------------------------------")
print("Начальное значение точки xj:", [round(x_val, 2) for x_val in x])
print("x^2:", [round(x_val**2, 2) for x_val in x])
print("Решение:", round(solve, 2))