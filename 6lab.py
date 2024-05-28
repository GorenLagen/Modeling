def solve_cable_production(p, q):
    # Исходные данные из задачи
    a = [
        [12, 18, 16, 24],  # Волочение
        [10, 4, 8, 7],     # Наложение изоляции
        [64, 56, 60, 80],  # Скручивание
        [30, 0, 18, 24],   # Освинцовывание
        [21, 15, 8, 30]    # Испытание и контроль
    ]
    
    b = [
        72000 * (1 + 2 * p + q),
        56000 * (1 + 2 * p + q),
        111760 * (1 + 2 * p + q),
        36000 * (1 + 2 * p + q),
        42000 * (1 + 2 * p + q)
    ]
    
    c = [
        -12 * (10 + p + 0.5 * q),
        -8 * (10 + p + 0.4 * q),
        -10 * (10 + p + 0.3 * q),
        -13 * (10 + p + 0.2 * q)
    ]
    
    d = [
        1000 * (1 + 2 * p + q),
        200 * (1 + 2 * p + q),
        20 * (1 + 2 * p + q),
        10 * (1 + 2 * p + q)
    ]
    
    # Создание симплекс-таблицы
    table = [
        [0] + c + [0] * len(b),
        *[[b[i]] + a[i] + [1 if j == i else 0 for j in range(len(b))] for i in range(len(b))]
    ]
    
    print("Исходная симплекс-таблица:")
    print_table(table)
    
    while True:
        # Проверка оптимальности
        if all(x >= 0 for x in table[0][1:]):
            break
        
        # Выбор разрешающего столбца
        col = table[0][1:].index(min(table[0][1:])) + 1
        
        # Выбор разрешающей строки
        ratios = [table[i][0] / table[i][col] if table[i][col] > 0 else float('inf') for i in range(1, len(table))]
        row = ratios.index(min(ratios)) + 1
        
        # Выполнение шага симплекс-метода
        pivot_on(table, row, col)
        
        print(f"Симплекс-таблица после шага с разрешающим элементом ({row}, {col}):")
        print_table(table)
    
    # Извлечение решения
    solution = [0] * len(c)
    for i in range(1, len(table)):
        if table[i][1:len(c)+1].count(1) == 1:
            j = table[i][1:len(c)+1].index(1)
            solution[j] = table[i][0]
    
    return solution

def print_table(table):
    for row in table:
        print(" | ".join(f"{v:.2f}" for v in row))
    print("-" * 50)

def pivot_on(table, row, col):
    j = table[row][col]
    table[row] = [e / j for e in table[row]]
    for r in range(len(table)):
        if r != row:
            j = table[r][col]
            table[r] = [table[r][i] - j * table[row][i] for i in range(len(table[r]))]

# Пример использования
p = 0
q = 0
solution = solve_cable_production(p, q)
print("Оптимальное решение:")
print(f"x1 = {solution[0]:.2f}")
print(f"x2 = {solution[1]:.2f}")
print(f"x3 = {solution[2]:.2f}")
print(f"x4 = {solution[3]:.2f}")