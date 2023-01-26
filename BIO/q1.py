fib = []
fib.append(1)
fib.append(2)
i = 2

while i < 100:
    fib.append(fib[i-1] + fib[i-2])
    i+=1

print(fib)