def insertion_sort_descending(arr):
    print(f"เริ่มต้น: {arr}")
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"\nรอบที่ {i}: พิจารณา key = {key}")
        
        while j >= 0 and arr[j] < key:  # เปลี่ยนจาก '>' เป็น '<' เพื่อเรียงจากมากไปน้อย
            arr[j+1] = arr[j]
            j -= 1
            print(f"  ย้าย {arr[j+2]} ไปทางขวา: {arr}")
        
        arr[j+1] = key
        print(f"  แทรก {key} ลงในตำแหน่ง {j+1}: {arr}")
    
    return arr

# ทดสอบแสดงขั้นตอน
test_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 9]
insertion_sort_descending(test_data.copy())
