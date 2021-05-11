"""
    В диапазоне натуральных чисел от 2 до 99 определить,
    сколько из них кратны каждому из чисел в диапазоне от 2 до 9
"""
sequence_ = range(2, 100)
divisors = range(2, 10)

dividends = {}

for d in divisors:
    dividends[d] = 0

for s in sequence_:
    for d in divisors:
        if s % d == 0:
            dividends[d] += 1

for d in divisors:
    print(f'последовательность содержит {dividends[d]} чисел кратных {d}')
