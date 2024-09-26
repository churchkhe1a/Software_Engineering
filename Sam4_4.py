def main(*args):

    if not args:
        return 0

    total = sum(args)
    average = total / len(args)
    return average


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    average = main(*numbers)
    print(f"Среднее арифметическое: {average}")
