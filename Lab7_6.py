with open('text.txt', 'a+') as f:
    f.write('\nIm small and stupid')

with open('text.txt', 'r') as f:
    result = f.readlines()
    print(result)
