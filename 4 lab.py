import math

p = 0
q = 0
alfa = 1.2 
A = 0.2 
B = 5 
l = 10 
n = 20
ro = 0.00785 

def f(x):
    return (A * x**alfa + B)**2

# Вычисление объема по формуле прямоугольников
def rect_integral(a, b, n):
    h = (b - a) / n
    integral_sum = 0
    for i in range(1, n+1):
        integral_sum += f(a + i*h)
    return integral_sum * h

# Вычисление объема по формуле трапеций  
def trap_integral(a, b, n):
    h = (b - a) / n
    integral_sum = (f(a) + f(b)) / 2
    for i in range(1, n):
        integral_sum += f(a + i*h)
    return integral_sum * h

# Вычисление объемов и масс
V_rect = math.pi * rect_integral(0, l, n)
V_trap = math.pi * trap_integral(0, l, n)

m_rect = V_rect * ro
m_trap = V_trap * ro

R = (f(l))**0.5
r = (f(0))**0.5

V_cyl = math.pi * R**2 * l
V_con = math.pi * l * (R**2 + R*r + r**2) / 3

m_cyl = V_cyl * ro  
m_con = V_con * ro

# Вычисление отходов
waste_rect_cyl = m_cyl - m_rect
waste_rect_cone = m_con - m_rect
waste_trap_cyl = m_cyl - m_trap  
waste_trap_cone = m_con - m_trap

# Вычисление уменьшения отходов в %
decrease_rect = (waste_rect_cyl - waste_rect_cone) / waste_rect_cyl * 100
decrease_trap = (waste_trap_cyl - waste_trap_cone) / waste_trap_cyl * 100

print(f"Объем детали (формула прямоугольников): {V_rect:.2f} см^3")
print(f"Объем детали (формула трапеций): {V_trap:.2f} см^3")
print(f"Масса детали (формула прямоугольников): {m_rect:.3f} кг") 
print(f"Масса детали (формула трапеций): {m_trap:.3f} кг")
print(f"Объем цилиндрической заготовки: {V_cyl:.2f} см^3")
print(f"Объем конусообразной заготовки: {V_con:.2f} см^3") 
print(f"Масса цилиндрической заготовки: {m_cyl:.3f} кг")
print(f"Масса конусообразной заготовки: {m_con:.3f} кг")
print(f"Масса отходов (прямоуг, цилиндр): {waste_rect_cyl:.3f} кг")
print(f"Масса отходов (прямоуг, конус): {waste_rect_cone:.3f} кг")
print(f"Масса отходов (трапеции, цилиндр): {waste_trap_cyl:.3f} кг") 
print(f"Масса отходов (трапеции, конус): {waste_trap_cone:.3f} кг")
print(f"Уменьшение отходов при исп. конуса (прямоуг): {decrease_rect:.2f}%")
print(f"Уменьшение отходов при исп. конуса (трапеции): {decrease_trap:.2f}%")