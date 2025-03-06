def bubble_sort_optimized(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        print(f"รอบที่ {i+1}:")
        
        for j in range(n - i - 1):
            print(f"  เปรียบเทียบ {arr[j]} กับ {arr[j+1]}", end=" -> ")
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # สลับค่า
                swapped = True
                print(f"สลับ: {arr}")
            else:
                print(f"ไม่สลับ: {arr}")
        
        if not swapped:
            print("  ไม่มีการสลับในรอบนี้ - ข้อมูลเรียงลำดับแล้ว")
            break
    
    return arr

test_data = [1, 2, 3, 4, 5,6,7,8,9,10]
print("ข้อมูลก่อนเรียงลำดับ:", test_data)
sorted_data = bubble_sort_optimized(test_data.copy())
print("ข้อมูลหลังเรียงลำดับ:", sorted_data)
