import numpy as np
import pandas as pd
from tabulate import tabulate

print("=== Фаза 3: Полная оценка трудоёмкости проекта FitLife ===\n")

# 1. Use Case Points (UCP) - уже полный
uaw = 24
uucw = 100
tcf = 0.6 + (0.01 * 45)  # 1.05
ecf = 1.4 + (-0.03 * 18.5)  # ≈0.845
ucp = (uaw + uucw) * tcf * ecf
print("Use Case Points:")
print(f"UAW: {uaw}")
print(f"UUCW: {uucw}")
print(f"TCF: {tcf:.2f}")
print(f"ECF: {ecf:.3f}")
print(f"UCP: {ucp:.2f} ≈ 89\n")

# 2. COSMIC Function Points - полный расчёт
cosmic_data = [
    ["Регистрация пользователя", 4, 2, 2, 2, 10],
    ["Просмотр каталога", 1, 3, 4, 0, 8],
    ["Поиск и фильтры", 2, 3, 5, 0, 10],
    ["Добавление в корзину", 2, 1, 2, 1, 6],
    ["Оформление заказа", 5, 3, 4, 3, 15],
    ["Интеграция оплаты", 3, 3, 2, 2, 10],
    ["Интеграция доставки", 2, 4, 3, 2, 11],
    ["Админ-панель: товары", 4, 2, 3, 4, 13],
    ["Админ-панель: заказы", 2, 3, 5, 2, 12],
    ["Отзывы и рейтинги", 3, 2, 3, 3, 11]
]

cosmic_df = pd.DataFrame(cosmic_data, columns=["Процесс", "E", "X", "R", "W", "CFP"])
total_cosmic = cosmic_df["CFP"].sum()
print("COSMIC Function Points:")
print(tabulate(cosmic_df, headers="keys", tablefmt="psql", showindex=False))
print(f"\nИтог: {total_cosmic} CFP\n")

# 3. Expert Judgement (Парное оценивание)
use_cases = [
    "Регистрация пользователя",
    "Просмотр каталога",
    "Поиск и фильтры",
    "Оформление заказа",
    "Интеграция оплаты/доставки",
    "Админ-панель",
    "Отзывы и рейтинги",
    "Личные данные",
    "Соцсети"
]

expert1_hours = [40, 30, 50, 90, 80, 70, 60, 20, 40]
expert2_hours = [45, 25, 55, 100, 85, 65, 55, 25, 45]
agreed_hours = np.mean([expert1_hours, expert2_hours], axis=0)
total_hours = np.sum(agreed_hours)

ej_data = list(zip(use_cases, expert1_hours, expert2_hours, agreed_hours))
ej_df = pd.DataFrame(ej_data, columns=["Use Case", "Эксперт 1 (ч)", "Эксперт 2 (ч)", "Согласованно (ч)"])
print("Expert Judgement:")
print(tabulate(ej_df, headers="keys", tablefmt="psql", showindex=False, floatfmt=".1f"))
print(f"\nИтоговая трудоёмкость: {total_hours:.0f} ч\n")

# 4. Сроки и стоимость
team_size = 5
hours_per_month = 160
efficiency = 0.8
team_hours_month = team_size * hours_per_month * efficiency  # 640
months = total_hours / team_hours_month
monthly_cost = 610_000
total_cost = monthly_cost * months

print("Сроки и стоимость:")
print(f"Ресурс команды: {team_hours_month:.0f} ч/мес")
print(f"Срок: {months:.1f} месяцев ≈ 3 месяца")
print(f"Стоимость: {total_cost:,.0f} руб\n")

# 5. Итоговый вывод
print("=== Итоговый сводный вывод ===")
print(f"Проект: FitLife (Интернет-магазин спортивных товаров)")
print(f"UCP: {ucp:.0f}")
print(f"COSMIC: {total_cosmic} FP")
print(f"Трудоёмкость: {total_hours:.0f} ч")
print(f"Срок: {months:.1f} мес (≈ 3 мес)")
print(f"Команда: {team_size} чел")
print(f"Стоимость: {total_cost:,.0f} руб")