# Исходные данные
p = 0
q = 0
n = 5


# Функция для расчета объема выпуска продукции по формуле (2.1)
def calc_output(k):
    return 10 + 0.05 * k + 0.01 * k**2 + 0.02 * (-1) ** k


# Функция для расчета линейного тренда
def linear_trend(t, c1, c2):
    return c1 + c2 * t


# Функция для расчета квадратичного тренда
def quadratic_trend(t, c1, c2, c3):
    return c1 + c2 * t + c3 * t**2


# Расчет объема выпуска продукции по месяцам
output = [calc_output(k) for k in range(1, n + 1)]

# Расчет коэффициентов для линейного тренда
sum_t = sum(range(1, n + 1))
sum_t2 = sum(t**2 for t in range(1, n + 1))
sum_y = sum(output)
sum_ty = sum(t * y for t, y in zip(range(1, n + 1), output))

a11 = n
a12 = sum_t
a22 = sum_t2
b1 = sum_y
b2 = sum_ty

det = a11 * a22 - a12**2
c1 = (b1 * a22 - b2 * a12) / det
c2 = (a11 * b2 - a12 * b1) / det

# Расчет коэффициентов для квадратичного тренда
sum_t3 = sum(t**3 for t in range(1, n + 1))
sum_t4 = sum(t**4 for t in range(1, n + 1))
sum_t2y = sum(t**2 * y for t, y in zip(range(1, n + 1), output))

a11 = n
a12 = sum_t
a13 = sum_t2
a22 = sum_t2
a23 = sum_t3
a33 = sum_t4
b1 = sum_y
b2 = sum_ty
b3 = sum_t2y

det = (
    a11 * a22 * a33
    + a12 * a23 * a13
    + a13 * a12 * a23
    - a13 * a22 * a13
    - a11 * a23 * a23
    - a12 * a12 * a33
)
c1 = (
    b1 * a22 * a33
    + b2 * a23 * a13
    + b3 * a12 * a23
    - b3 * a22 * a13
    - b1 * a23 * a23
    - b2 * a12 * a33
) / det
c2 = (
    a11 * b2 * a33
    + a13 * b3 * a13
    + b1 * a12 * a23
    - b1 * a22 * a13
    - a11 * b3 * a23
    - a13 * b2 * a13
) / det
c3 = (
    a11 * a22 * b3
    + a12 * a23 * b1
    + a13 * b2 * a12
    - a13 * a22 * b1
    - a11 * a23 * b2
    - a12 * b2 * a12
) / det

# Расчет значений линейного и квадратичного трендов
linear_trend_values = [linear_trend(t, c1, c2) for t in range(1, n + 1)]
quadratic_trend_values = [quadratic_trend(t, c1, c2, c3) for t in range(1, n + 1)]

# Расчет погрешностей приближения
linear_errors = [
    abs(y - y_trend) / y for y, y_trend in zip(output, linear_trend_values)
]
quadratic_errors = [
    abs(y - y_trend) / y for y, y_trend in zip(output, quadratic_trend_values)
]

max_linear_error = max(linear_errors)
max_quadratic_error = max(quadratic_errors)

# Прогнозирование объема выпуска на 6-й месяц
linear_forecast = linear_trend(6, c1, c2)
quadratic_forecast = quadratic_trend(6, c1, c2, c3)

# Вывод результатов
print("Объем выпуска продукции по месяцам:")
for t, y in enumerate(output, start=1):
    print(f"Месяц {t}: {y}")

print("\nЛинейный тренд:")
for t, y in enumerate(linear_trend_values, start=1):
    print(f"Месяц {t}: {y}")

print("\nКвадратичный тренд:")
for t, y in enumerate(quadratic_trend_values, start=1):
    print(f"Месяц {t}: {y}")

print(f"\nПогрешность линейного приближения: {max_linear_error}")
print(f"Погрешность квадратичного приближения: {max_quadratic_error}")

print(f"\nПрогноз на 6-й месяц (линейный тренд): {linear_forecast}")
print(f"Прогноз на 6-й месяц (квадратичный тренд): {quadratic_forecast}")
