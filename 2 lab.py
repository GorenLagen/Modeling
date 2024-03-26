# Функция для расчета объема выпуска
def calculate_output(k):
    return 10 + 0.05 * k + 0.01 * k**2 + 0.02 * (-1) ** k


# Функция для расчета коэффициентов линейного тренда методом наименьших квадратов
def calculate_linear_coefficients(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x2 = sum(xi**2 for xi in x)

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    b = (sum_y - a * sum_x) / n

    return a, b


# Функция для расчета коэффициентов квадратичного тренда методом наименьших квадратов
def calculate_quadratic_coefficients(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum(xi**2 for xi in x)
    sum_x3 = sum(xi**3 for xi in x)
    sum_x4 = sum(xi**4 for xi in x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x2y = sum(xi**2 * yi for xi, yi in zip(x, y))

    a11 = n
    a12 = sum_x
    a13 = sum_x2
    a21 = sum_x
    a22 = sum_x2
    a23 = sum_x3
    a31 = sum_x2
    a32 = sum_x3
    a33 = sum_x4
    b1 = sum_y
    b2 = sum_xy
    b3 = sum_x2y

    det = (
        a11 * (a22 * a33 - a23 * a32)
        - a12 * (a21 * a33 - a23 * a31)
        + a13 * (a21 * a32 - a22 * a31)
    )
    det1 = (
        b1 * (a22 * a33 - a23 * a32)
        - a12 * (b2 * a33 - a23 * b3)
        + a13 * (b2 * a32 - a22 * b3)
    )
    det2 = (
        a11 * (b2 * a33 - a23 * b3)
        - b1 * (a21 * a33 - a23 * a31)
        + a13 * (a21 * b3 - b2 * a31)
    )
    det3 = (
        a11 * (a22 * b3 - b2 * a32)
        - a12 * (a21 * b3 - b2 * a31)
        + b1 * (a21 * a32 - a22 * a31)
    )

    c1 = det1 / det
    c2 = det2 / det
    c3 = det3 / det

    return c1, c2, c3


# Функция для расчета погрешности тренда
def calculate_error(actual, predicted):
    return [abs((yi - yi_pred) / yi) for yi, yi_pred in zip(actual, predicted)]


# Главная функция программы
def main():
    p = 0
    q = 0
    n = 5

    x = list(range(1, n + 1))  # Создание списка месяцев (t_k)
    y = [calculate_output(k) for k in x]  # Расчет объемов выпуска (y_k)

    a, b = calculate_linear_coefficients(x, y)  # Расчет коэффициентов линейного тренда
    linear_trend = [a * xi + b for xi in x]  # Расчет значений линейного тренда

    c1, c2, c3 = calculate_quadratic_coefficients(
        x, y
    )  # Расчет коэффициентов квадратичного тренда
    quadratic_trend = [
        c1 + c2 * xi + c3 * xi**2 for xi in x
    ]  # Расчет значений квадратичного тренда

    linear_error = calculate_error(
        y, linear_trend
    )  # Расчет погрешности линейного тренда
    quadratic_error = calculate_error(
        y, quadratic_trend
    )  # Расчет погрешности квадратичного тренда

    linear_errors = calculate_error(y, linear_trend)
    quadratic_errors = calculate_error(y, quadratic_trend)

    # Вывод результатов
    print("Месяц (t_k):", x)
    print("Объем выпуска (y_k):", y)
    print("Линейный тренд:", linear_trend)
    print("Квадратичный тренд:", quadratic_trend)
    print("Погрешность линейного тренда:", linear_error)
    print("Погрешность квадратичного тренда:", quadratic_error)

    print("Погрешности линейного тренда в точках:", end=" ")
    print(", ".join(f"{error:.6f}" for error in linear_errors))

    print("Погрешности квадратичного тренда в точках:", end=" ")
    print(", ".join(f"{error:.6f}" for error in quadratic_errors))

    print("")
    linear_forecast = a * 6 + b
    quadratic_forecast = c1 + c2 * 6 + c3 * 6**2

    print(
        f"Прогнозируемый объем выпуска в 6-м месяце (линейный тренд): {linear_forecast:.4f}"
    )
    print(
        f"Прогнозируемый объем выпуска в 6-м месяце (квадратичный тренд): {quadratic_forecast:.4f}"
    )


# Запуск главной функции программы
if __name__ == "__main__":
    main()
