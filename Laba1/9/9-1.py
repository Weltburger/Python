def Foo():
    values = {1000:2, 500:2, 200:10, 100:0, 50:5, 10:20}
    res = {1000:0, 500:0, 200:0, 100:0, 50:0, 10:0}
    money = 5370
    for key in values.keys():
        current = money//key
        if (current > values[key]):
            money = money - (values[key] * key)
            res[key] = values[key]
        else:
            money = money % key
            res[key] = current
    print(money)
    print(sum([k * v for k, v in zip(res.keys(), res.values())]))
    print(res)


if __name__ == "__main__":
    Foo()