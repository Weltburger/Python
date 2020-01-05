def non_empty(foo):
    def wrapper():
        res = foo()
        iter = 0
        for i in res:
            if i == '' or i is None:
                res.pop(iter)
            iter += 1
        return res
    return wrapper


@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1']


print(get_pages())
