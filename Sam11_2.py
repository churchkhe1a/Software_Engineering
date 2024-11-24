def fib(n):
  a, b = 1, 1
  for _ in range(n):
    yield a
    a, b = b, a + b

fib_sequence = fib(200)

with open("fib.txt", "w") as f:
  for i in range(200):
    num = next(fib_sequence)
    f.write(str(num) + "\n")

print(f"200-е число Фибоначчи: {num}")
