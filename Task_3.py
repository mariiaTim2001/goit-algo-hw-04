"""
==========================================================================================================================|
Таблиця теоретичних оцінок складності алгоритмів                                                                          |
==========================================================================================================================|
| Алгоритм       | Середня/гірша складність | Найкращий випадок | Коментар                                                |
|-----------------|--------------------------|-------------------|--------------------------------------------------------|
| Insertion sort  | O(n²)                   | O(n)             | Дуже простий, але повільний на великих даних             |
| Merge sort      | O(n log n)              | O(n log n)       | Стабільний, добре працює на будь-яких даних              |
| Timsort         | O(n log n)              | O(n)             | Гібрид merge + insertion, ефективний на реальних наборах |
==========================================================================================================================|
"""

import random
import timeit

#  Алгоритми 

def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Функція вимірювання

def measure_time(func, data):
    stmt = f"{func.__name__}(data)"
    return timeit.timeit(stmt, globals={'data': data, func.__name__: func}, number=1)

# Запуск експериментів

sizes = [1000, 5000, 10000, 20000]
results = []

for n in sizes:
    arr = [random.randint(0, n) for _ in range(n)]
    results.append({
        "n": n,
        "Insertion": measure_time(insertion_sort, arr),
        "Merge":     measure_time(merge_sort, arr),
        "Timsort":   measure_time(sorted, arr)
    })

for r in results:
    print(f"n={r['n']}: Insertion={r['Insertion']:.4f}s | Merge={r['Merge']:.4f}s | Timsort={r['Timsort']:.4f}s")

# Аналіз результатів
"""
1. Insertion sort показує найгірші результати на великих масивах через квадратичну складність.
2. Merge sort стабільно працює за O(n log n) і є значно швидшим за Insertion sort на великих даних.
3. Вбудований Timsort є найефективнішим для реальних наборів даних, особливо на частково відсортованих масивах.
4. Результати підтверджують теоретичні оцінки складності алгоритмів.
"""