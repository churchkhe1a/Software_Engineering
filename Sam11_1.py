def fib(n):
  a, b = 1, 1
  for _ in range(n):
    yield a
    a, b = b, a + b

fib_sequence = fib(200)

for i in range(199):
  next(fib_sequence)
print(f"200-е число Фибоначчи: {next(fib_sequence)}")
