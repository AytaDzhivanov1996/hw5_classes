class MyList(list):
    def __init__(self, array):
        super().__init__(item for item in array)
        self.array = array
        print('Работает магический метод')

    def __setitem__(self, index, item):
        print('Работает магический метод')
        super().__setitem__(index, item)

    def __getitem__(self, item):
        print('Работает магический метод')
        super().__getitem__(item)

    def __str__(self):
        print('Работает магический метод')
        return f'{self.array}'

    def __len__(self):
        print('Работает магический метод')
        return len(self.array)


lst = MyList(['Jon', 'Snow', 'Java'])

if not lst[2] == 'Python':
    lst[2] = 'Python'

print(lst)
print(len(lst))
