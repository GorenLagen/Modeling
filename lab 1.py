import matplotlib
import matplotlib.pyplot as plt

# ГИПЕРПАРАМЕТРЫ
p = 0
q = 0
z_0 = 100 + 4 * p + 3 * q + 1  # сумма вклада
i = p + q + 1  # процент
rate_0 = i / 100  # приращение
rate_1 = rate_0 + 1
rate_2 = (1 + 1 / (10 * rate_0)) / rate_0
h_rate = z_0 * (1 + 11 * rate_0) / (10 * rate_0**2)  # сложный процент
z_2 = z_0 * 2
z_5 = z_0 * 5
t = 1


# года
num = []
x1_vector = []
y1_vector = []
x2_vector = []
y2_vector = []
t1_vector = []
t2_vector = []
yt1_k = 0
yt2_k = 0
while True:
    yt_1 = z_0 * rate_1**t
    yt_2 = z_0 * rate_2 * rate_1 ** (t + 1) - z_0 * t / (10 * rate_0) - h_rate
    t += 1
    if yt1_k == 0:
        x1_vector.append(yt_1)
        t1_vector.append(t - 1)
    if yt2_k == 0:
        x2_vector.append(yt_2)
        t2_vector.append(t - 1)
    if z_5 <= yt_2 and yt2_k == 0:
        num.append(t - 1)
        yt2_k += 1
    if z_2 <= yt_1 and yt1_k == 0:
        num.append(t - 1)
        yt1_k += 1
    if yt1_k + yt2_k == 2:
        break


# Доп. расчеты

t = 5
yt = 10 * (100 + 4 * p + 3 * q + 1)
coef = (
    rate_2 * rate_1 ** (t + 1)
    - t / (10 * rate_0)
    - (1 + 11 * rate_0) / (10 * rate_0**2)
)
vklad = yt / coef

# графики

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(x1_vector, t1_vector)
ax1.set_title("yt - 1")
ax2.plot(x2_vector, t2_vector)
ax2.set_title("yt - 2")

ax1.grid()
ax2.grid()

# вывод

print("-" * 10)
print(f"Вклад увеличится в два раза при расчете в условиях первого случая - {num[1]}\n")
print(f"Вклад увеличится в пять раз при расчете в условиях второго случая - {num[0]}\n")
print(
    f"Необходимо разместить на вкладе, чтобы через 5 лет наращенная сумма превысила {yt} ден. средств - {vklad}"
)
print("-" * 10)
plt.show()
