def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    if total == 0:
        return 0  # Handle case with only zeros
    return total / len(numbers)

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

my_list = [0,0,0]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_list = [1,2,3]
average = calculate_average(my_list)
print(f"The average is: {average}") 