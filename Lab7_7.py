lines = ['one', 'two', 'three']
with open ('text.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
