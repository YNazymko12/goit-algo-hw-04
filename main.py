import timeit
import random

# Функція для вимірювання часу сортування
def measure_time(sort_func, data):
    start_time = timeit.default_timer()
    sorted_data = sort_func(data[:])  # Робимо копію даних перед сортуванням
    execution_time = timeit.default_timer() - start_time
    return sorted_data, execution_time

# Реалізація алгоритму сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Реалізація алгоритму сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

# Функція для злиття двох відсортованих списків
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Використання вбудованого сортування Python
def built_in_sort(arr):
    arr.sort()
    return arr

# Генеруємо випадкові дані для тестування
data_smallest = [random.randint(0, 1_000) for _ in range(10)]
data_small = [random.randint(0, 1_000) for _ in range(100)]
data_big = [random.randint(0, 1_000) for _ in range(1_000)]
data_largest = [random.randint(0, 10_000) for _ in range(10_000)]

test_data = [
    ("Smallest (10)", data_smallest),
    ("Small (100)", data_small),
    ("Big (1,000)", data_big),
    ("Largest (10,000)", data_largest)
]

sorting_functions = [
    ("Insertion Sort", insertion_sort),
    ("Merge Sort", merge_sort),
    ("Timsort (Python's sorted)", sorted),
    ("Timsort (Python's sort)", built_in_sort)
]

def main():
    results = []
    headers = ["Array Size"] + [name for name, _ in sorting_functions]

    for size_name, data in test_data:
        row = [size_name]
        for name, func in sorting_functions:
            _, exec_time = measure_time(func, data)
            row.append(f"{exec_time:.6f} s")
        results.append(row)

    col_widths = [max(len(str(cell)) for cell in column) for column in zip(*([headers] + results))]

    header_row = " | ".join(f"{headers[i]:<{col_widths[i]}}" for i in range(len(headers)))
    separator_row = " | ".join('-' * col_widths[i] for i in range(len(headers)))
    print(header_row)
    print(separator_row)

    for row in results:
        print(" | ".join(f"{row[i]:<{col_widths[i]}}" for i in range(len(row))))

if __name__ == "__main__":
    main()
