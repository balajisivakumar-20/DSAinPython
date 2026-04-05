#smalles number

def smallest(arr):
    smallest_number = float('inf')
    for num in arr:
        if num < smallest_number:
            smallest_number = num
    return smallest_number

arr = [12,23,34,4,5,65,76]
result = smallest(arr)
print("Result : ",result)