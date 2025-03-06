def selection_sort_descending(arr):
    n = len(arr)
    
    for i in range(n):
        max_idx = i
        print(f"\nรอบที่ {i+1}:")
        print(f"  ข้อมูลปัจจุบัน: {arr}")
        print(f"  ค้นหาค่ามากที่สุดในตำแหน่ง {i} ถึง {n-1}")
        
        for j in range(i+1, n):
            print(f"    เปรียบเทียบ {arr[max_idx]} กับ {arr[j]}", end=" -> ")
            if arr[j] > arr[max_idx]:  # เปลี่ยนเงื่อนไขจาก '<' เป็น '>' เพื่อเรียงจากมากไปน้อย
                max_idx = j
                print(f"พบค่าที่มากกว่า: {arr[j]}")
            else:
                print("ไม่มีการเปลี่ยนแปลง")
        
        print(f"  ค่ามากที่สุดคือ {arr[max_idx]} ที่ตำแหน่ง {max_idx}")
        if i != max_idx:
            print(f"  สลับ {arr[i]} กับ {arr[max_idx]}")
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else:
            print(f"  ไม่ต้องสลับเนื่องจากอยู่ในตำแหน่งที่ถูกต้องแล้ว")
        
        print(f"  ข้อมูลหลังรอบที่ {i+1}: {arr}")
    
    return arr

# ทดสอบแสดงขั้นตอน
test_data = [10, 9, 8, 7, 5, 6, 4, 3, 2, 1]
selection_sort_descending(test_data.copy())
