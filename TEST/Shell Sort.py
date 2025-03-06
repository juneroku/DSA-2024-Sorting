import time
import random

def quick_sort_with_steps(arr, depth=0):
    if len(arr) <= 1:
        return arr
    
    first = arr[0]
    middle = arr[len(arr) // 2]
    last = arr[-1]
    pivot = sorted([first, middle, last])[1]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort_with_steps(left, depth + 1) + middle + quick_sort_with_steps(right, depth + 1)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    
    return arr

# สร้างชุดข้อมูลที่เกือบเรียงลำดับแล้ว
nearly_sorted_data = list(range(1, 10001))
for i in range(0, len(nearly_sorted_data), 100):
    if i + 1 < len(nearly_sorted_data):
        nearly_sorted_data[i], nearly_sorted_data[i + 1] = nearly_sorted_data[i + 1], nearly_sorted_data[i]

# วัดเวลาการทำงานของ Quick Sort
quick_data = nearly_sorted_data.copy()
start_time = time.time()
quick_sort_with_steps(quick_data)
quick_sort_time = time.time() - start_time

# วัดเวลาการทำงานของ Insertion Sort
insertion_data = nearly_sorted_data.copy()
start_time = time.time()
insertion_sort(insertion_data)
insertion_sort_time = time.time() - start_time

# วัดเวลาการทำงานของ Shell Sort
shell_data = nearly_sorted_data.copy()
start_time = time.time()
shell_sort(shell_data)
shell_sort_time = time.time() - start_time

# แสดงผลลัพธ์
print(f"Quick Sort ใช้เวลา: {quick_sort_time:.6f} วินาที")
print(f"Insertion Sort ใช้เวลา: {insertion_sort_time:.6f} วินาที")
print(f"Shell Sort ใช้เวลา: {shell_sort_time:.6f} วินาที")
