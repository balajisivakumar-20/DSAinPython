

value_1 = int(input("Enter the 1st value: "))
value_2 = int(input("Enter the 2nd value: "))
value_3 = int(input("Enter the 3rd value: "))
value_4 = int(input("Enter the 4th value: "))

def calculate(value_1, value_2, value_3, value_4):
    final_value = value_1 - (value_2 + value_3 + value_4)
    return final_value

if __name__ == "__main__":
    result = calculate(value_1, value_2, value_3, value_4)
    print(result)