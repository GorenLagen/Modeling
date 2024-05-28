def update_input(p, q):
    mass = 200 + 20 * p + 10 * q
    velocity_column = ((60 + p + q) * 1000 / 3600)
    velocity_aircraft = ((600 + 2 * p + 4 * q) * 1000 / 3600)
    coeff_k1 = 0.2 + 0.1 * p
    coeff_k2 = 0.04 + 0.01 * p
    time_step = 0.2
    gravity = 9.8
    height = 5 * ((20 + 2 * p + q) ** 2)
    return mass, velocity_column, velocity_aircraft, coeff_k1, coeff_k2, time_step, gravity, height

def calculate_time(time, time_step):
    return round(time * time_step, 2)

def calculate_speed(time, time_step, gravity, mass, coeff_k1, coeff_k2):
    return round(time + time_step * (gravity - 1 / mass * (coeff_k1 * time + coeff_k2 * (time ** 2))), 2)

def calculate_distance_x(distance, speed, time_step):
    return round(distance + time_step * speed, 2)

def calculate_distance_y(time, velocity_aircraft):
    return round(velocity_aircraft * time, 2)

def calculate_height(distance_x, height):
    return round(height - distance_x, 2)

def calculate_time_fall(table_data, time_step):
    last_two_rows = table_data[-2:]
    time_values = [row[0] for row in last_two_rows]
    height_values = [row[-1] for row in last_two_rows]
    return round(time_values[0] - (time_values[1] - time_values[0]) * height_values[0] / (height_values[1] - height_values[0]), 2)

def calculate_lead_distance(velocity_aircraft, velocity_column, time_fall):
    return round((velocity_aircraft - velocity_column) * time_fall, 2)

def fill_array(mass, velocity_column, velocity_aircraft, coeff_k1, coeff_k2, time_step, gravity, height):
    data = []
    count = 0

    while True:
        if count == 0:
            data.append([0, 0, 0, 0, height - 0])
            count += 1
            continue

        time = calculate_time(count, time_step)
        speed = calculate_speed(data[count - 1][1], time_step, gravity, mass, coeff_k1, coeff_k2)
        distance_x = calculate_distance_x(data[count - 1][2], data[count - 1][1], time_step)
        distance_y = calculate_distance_y(time, velocity_aircraft)
        height_projectile = calculate_height(distance_x, height)

        data.append([time, speed, distance_x, distance_y, height_projectile])
        count += 1

        if height_projectile <= 0:
            break

    return data

def render_table(p, q):
    mass, velocity_column, velocity_aircraft, coeff_k1, coeff_k2, time_step, gravity, height = update_input(p, q)
    data = fill_array(mass, velocity_column, velocity_aircraft, coeff_k1, coeff_k2, time_step, gravity, height)
    time_fall = calculate_time_fall(data, time_step)
    lead_distance = calculate_lead_distance(velocity_aircraft, velocity_column, time_fall)
    return data, time_fall, lead_distance


p = 0
q = 0

table_data, time_fall, lead_distance = render_table(p, q)

print("Табличные данные:")
print("Время\tСкорость\tРасстояние X\tРасстояние Y\tВысота снаряда")
for row in table_data:
    print(f"{row[0]:.2f}\t{row[1]:.2f}\t\t{row[2]:.2f}\t\t{row[3]:.2f}\t\t{row[4]:.2f}")

print(f"\nВремя падения снаряда: {time_fall:.2f}")
print(f"Расстояние упреждения цели: {lead_distance:.2f}")