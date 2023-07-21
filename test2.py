# Функция, определяющая минимальный квадрат элемента, больший суммы всех элементов
def minsqrt(num_set):
  # Сортируем элементы множества num_set функциями map и lambda
  num_sq = sorted(map(lambda x: x**2, num_set))
  # Задаем i = 0
  i = 0
  # Обходим элеиенты, пока квадрат элемента не станет больше или равен сумме всех элементов множества
  while num_sq[i]**2 < sum(num_set):
    # Увеличиваем индекс на единицу, если квадрат меньше суммы
    i += 1
  # Возвращаем первый элемент, квадрат которошо больше или равен сумме всех элементов множества
  return num_sq[i]

# Множество. Для простоты взял из целых чисел. Номожно расширить и добавить блок фильтра по типу
a = {5, 2, 6, -3, 3, 8, 9, 12, -4, 22}

# Выводим результат функции
print(minsqrt(a))

# Сложность O(n*log(n)), т.к. это сложность сортировка sorted.
# Максимальная сложность перебора элементов и сравнения составлеет O(n) и поглощается O(n*log(n))