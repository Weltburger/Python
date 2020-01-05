def frange(start, end, step):
    for i in range(start, end):
        while i < end:
            i += step
            yield i


for j in frange(1, 5, 0.1):
    print(j)
