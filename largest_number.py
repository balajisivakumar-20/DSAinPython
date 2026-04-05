def largest_number(arr):
    largest = float('-inf')
    for num in arr:
        if num > largest:
            largest = num
    return largest

arr = [12,234,45,56,76,987,543,5634,3435,453]
result = largest_number(arr)
print("Result : ", result)