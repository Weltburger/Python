from re import finditer


def script(filename):
    try:
        file = open(filename, "rt")
        for i, line in enumerate(file.buffer, 1):
            line = line.decode('utf-8')
            for match in finditer(r'[a-z]{1,}: (?:int|short|byte) \[[0-9]{1,}\]', line):
                yield ("Строка {}, позиция {} : найдено '{}'"
                       .format(i, match.span()[0] + 1, match.group()))
    finally:
        file.close()
