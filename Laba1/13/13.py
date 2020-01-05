def extra_enumerate(x):
    fraction = 0
    cum = 0
    for step in x:
        fraction += step
    for i in range(len(x)):
        elem = x[i]
        cum += x[i]
        frac = cum / fraction
        yield i, elem, cum, frac


x = [1, 3, 4, 2]
for i, elem, cum, frac in extra_enumerate(x):
    print(elem, cum, frac)
