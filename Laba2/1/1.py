try:
    with open('1.txt', 'r') as f:
        lines = f.read().lower()
    #       lines.strip()
    # print(lines)

    arr = []
    for i in range(len(lines)):
        if lines[i].isalpha():  # only letters
            arr.append(lines[i])

    symbols = {}
    for i in range(len(arr)):
        count = 0
        for j in arr:
            if arr[i] == j:
                count = count + 1
                symbols[arr[i]] = count

    key_value = lambda x: x[1]
    Sorted = sorted(symbols.items(), key=key_value, reverse=True)
    print('Unsorted: \n', symbols, "\n\n", 'Sorted: \n', Sorted)
    f.close()

except IOError as ioe:
    print(ioe)
except NameError as ne:
    print(ne)
