import pandas as pd

import pandas as pd

# Шаг 1: Загрузка данных из CSV-файла
df = pd.read_csv('dz.csv', encoding='UTF-8')

# Шаг 2: Вывод первых 5 строк данных
print("Первые 5 строк данных:")
print(df.head())

# Шаг 3: Вывод информации о данных
print("\nИнформация о данных:")
print(df.info())

# Рассчитаем среднюю зарплату по городу
average_salary_by_city = df.groupby('City')['Salary'].mean()

# Результат
print(average_salary_by_city)