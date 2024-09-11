import pandas as pd

# Шаг 1: Загрузка данных из CSV-файла
df = pd.read_csv('wfp_market_food_prices.csv', encoding='ISO-8859-1')

# Шаг 2: Вывод первых 5 строк данных
print("Первые 5 строк данных:")
print(df.head())

# Шаг 3: Вывод информации о данных
print("\nИнформация о данных:")
print(df.info())

# Шаг 4: Статистическое описание данных
print("\nСтатистическое описание данных:")
print(df.describe())