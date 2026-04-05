#second largest number in an array

"""
Edge cases that we need to cover are
1. Duplicate numbers inside an array
2. negative numbers need to be handled
3. empty array need to be handled
"""

def second_largest(arr):
    first_largest = float('-inf')
    second_largest = float('-inf')

    if len(arr) < 2:
        return "Invalid Array"
    
    for num in arr:
        if num > second_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num != first_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else "No second largest number"

arr = [12,23,34,45,45,45]
result = second_largest(arr)
print("Second largest : ", result)