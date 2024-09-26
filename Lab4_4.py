def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))

    print(f"one = {one}\ntwo = {two}\nthree = {three}")

    return x + sum(args) / float(len(args))

if __name__ == '__main__':
    result = main(5, 1, -2, 3, 4)
    print(f"\nresult = {result}")

# 1. x = 5 (первый аргумент)
# 2. sum(args) = 1 + (-2) + 3 + 4 = 6 (сумма остальных аргументов)
# 3. len(args) = 4 (количество остальных аргументов)
# 4. 5 + 6 / 4 = 6.5 (результат вычисления)
