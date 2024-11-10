user_input = input("Введите последовательность чисел, разделенных пробелом: ")

numbers_list = [int(x) for x in user_input.split()]

numbers_tuple = tuple(numbers_list)

print("Список: ", numbers_list)
print("Кортеж: ", numbers_tuple)
