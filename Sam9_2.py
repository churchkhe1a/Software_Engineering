def remove_first_occurrence(tpl, value):
    lst = list(tpl)

    try:
        lst.remove(value)
    except ValueError:
        pass

    return tuple(lst)


print(remove_first_occurrence((1, 2, 3), 1))
print(remove_first_occurrence((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove_first_occurrence((2, 4, 6, 6, 4, 2), 9))
