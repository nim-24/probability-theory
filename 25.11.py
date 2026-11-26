import math
import random

# задача 1
def integral(f, a, b, n):
    h = (b - a) / n
    total = 0.0

    for i in range(n):
        x_mid = a + (i + 0.5) * h
        total += f(x_mid)

    return total * h


print("Задача 1")
print("∫₀^π sin(x) dx ≈", integral(math.sin, 0, math.pi, 10000))
print("∫₀¹ x² dx ≈", integral(lambda x: x**2, 0, 1, 10000))


# задача 2
def left_rectangles(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + i * h) for i in range(n))


def midpoint_rectangles(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + (i + 0.5) * h) for i in range(n))


def trapezoids(f, a, b, n):
    h = (b - a) / n
    total = (f(a) + f(b)) / 2
    total += sum(f(a + i * h) for i in range(1, n))
    return h * total


print("\nЗадача 2: интеграл sin(x) от 0 до π, точное значение 2")
print(f"{'n':>6} {'левые':>14} {'ошибка':>14} "
      f"{'средние':>14} {'ошибка':>14} {'трапеции':>14} {'ошибка':>14}")

for n in (10, 100, 1000):
    left = left_rectangles(math.sin, 0, math.pi, n)
    middle = midpoint_rectangles(math.sin, 0, math.pi, n)
    trap = trapezoids(math.sin, 0, math.pi, n)

    print(f"{n:6d} {left:14.10f} {abs(left - 2):14.3e} "
          f"{middle:14.10f} {abs(middle - 2):14.3e} "
          f"{trap:14.10f} {abs(trap - 2):14.3e}")

print("При увеличении n в 10 раз ошибка метода средних прямоугольников "
      "и трапеций обычно уменьшается примерно в 100 раз.")
print("У левых прямоугольников для этой задачи ошибка уменьшается "
      "примерно в 10 раз.")


# задача 3
def estimate_pi(n):
    inside = 0

    for _ in range(n):
        x = random.random()
        y = random.random()

        if x * x + y * y <= 1:
            inside += 1

    return 4 * inside / n


print("\nЗадача 3: Монте-Карло")
random.seed(1)  

for n in (10**3, 10**4, 10**5, 10**6):
    estimate = estimate_pi(n)
    print(f"n={n:>7}: π ≈ {estimate:.8f}, ошибка = {abs(estimate - math.pi):.8f}")

print("Типичный размер ошибки уменьшается примерно как 1/√n.")


# задача 4
def simulate_fall(dt):
    y = 100.0
    v = 0.0
    g = 9.8
    t = 0.0
    target_time = 2.0

    while t < target_time:
        step = min(dt, target_time - t)
        y -= v * step
        v += g * step
        t += step

    return y


exact_y = 100 - 0.5 * 9.8 * 2**2

print("\nЗадача 4: высота через 2 секунды")
print(f"Точная формула: {exact_y:.6f} м")

for dt in (0.1, 0.001):
    y = simulate_fall(dt)
    print(f"dt={dt}: y ≈ {y:.6f} м, ошибка = {abs(y - exact_y):.6f} м")

print("При обновлении y сначала используется старая скорость — "
      "это даёт небольшую погрешность вниз.")
print("Если сначала обновлять v, а затем y, координата каждого шага "
      "сдвигается чуть дальше вниз.")


# задача 5

n = math.floor(math.sqrt(1 / (12 * 1e-8))) + 1
estimated_error = 1 / (12 * n**2)
numerical_value = midpoint_rectangles(lambda x: x**2, 0, 1, n)
exact_value = 1 / 3

print("\nЗадача 5")
print("Минимальное n:", n)
print("Оценка ошибки h²/12:", estimated_error)
print("Ошибка по сравнению с точным значением:",
      abs(numerical_value - exact_value))
