class Taggable(object):
    def tag(self):
        res = self.name.split()
        for word in res:
            if not word.istitle():
                res.remove(word)
                return res


class Book(Taggable):
    key = 0

    def __init__(self, name, author):
        assert (len(name) != 0), "Название книги обязательно"
        assert (len(author) != 0), "Автор книги обязателен"
        self.name = name
        self.author = author
        self.key = self.index()

    def __str__(self):
        info = self.author.split(' ')
        first_name = info[1]
        last_name = info[0]
        return f'[{self.key}] {last_name[0]}.{first_name} "{self.name}"'

    @classmethod
    def index(cls):
        cls.key += 1
        return cls.key


class Library(Book):
    def __init__(self, number, address):
        assert (number is not None and number >= 1), "Номер библиотеки обязательно"
        assert (len(address) != 0), "Адрес библиотеки обязателен"
        self.number = number
        self.address = address
        self.book = []
        self.itr = -1

    def __iadd__(self, other):
        self.book.append(other)
        return self

    def __iter__(self):
        return self

    def __next__(self):
        self.itr = self.itr + 1
        if self.itr < len(self.book):
            return self.book[self.itr]
        else:
            raise StopIteration


lib = Library(1, 'Artyoma st. 55, Dumbass')
lib += Book('War and Peace', 'Lev Tolstoi')
lib += Book('Blood of Elves', 'Andrzej Sapkowski')

for book in lib:
    print(book)
    print(book.tag())
