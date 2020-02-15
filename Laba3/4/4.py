class StringFormatter:
    def del_n(self, string, n, splitter=' '):
        words_list = string.split(splitter)
        arr = list(filter(lambda x: len(x) >= n, words_list))
        new_str = ''
        for i in arr:
            new_str += i + ' '
        return new_str

    def replace_numbers(self, string):
        new_str = string.translate(str.maketrans('0123456789', '**********'))
        return new_str

    def add_spaces(self, string):
        return ' '.join(list(string))

    def sort_len(self, string, splitter=' '):
        arr = sorted(string.split(splitter), key=len)
        new_str = ''
        for word in arr:
            new_str += word + ' '
        return new_str

    def lex_order(self, string, splitter=' '):
        arr = sorted(string.split(splitter))
        new_str = ''
        for word in arr:
            new_str += word + ' '
        return new_str


SFor = StringFormatter()

print(SFor.del_n('Первое второе третье четвертое пятое шестое седьмое', 7))
print(SFor.replace_numbers('Замена цифр 5 89 6 54 654 68 654'))
print(SFor.add_spaces('Добавление пробелов в строке'))
print(SFor.sort_len('А почему бы не отсортировать эту строку по длине слов?', 'о'))
print(SFor.sort_len('А почему бы не отсортировать эту строку по длине слов?'))
print(SFor.lex_order('А почему бы не отсортировать эту строку в лексикографическом порядке?'), ' ')
