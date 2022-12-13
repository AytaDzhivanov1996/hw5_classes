class TeamIterator:
    def __init__(self, team):
        self.__team = team
        self.__index = 0

    def __next__(self):
        if self.__index < (len(self.__team._junior_members) + len(self.__team._senior_members)):
            if self.__index < len(self.__team._junior_members):
                tup = (self.__team._junior_members[self.__index], 'junior')
            else:
                tup = (self.__team._senior_members[self.__index - len(self.__team._junior_members)], 'senior')
            self.__index += 1
            return tup
        raise StopIteration


class Team:
    """
    Хранит список джунов и синьоров, а также переопределяет метод __iter__().
    """

    def __init__(self):
        self._junior_members = list()
        self._senior_members = list()

    def add_junior_members(self, members):
        self._junior_members += members

    def add_senior_members(self, members):
        self._senior_members += members

    def __iter__(self):
        """ Возвращает объект-итератор """
        return TeamIterator(self)


def main():
    # создаем команду
    team = Team()
    # добавляем имена джунов
    team.add_junior_members(['Ivan', 'Mary', 'Nikita'])
    # добавляем имена синьоров
    team.add_senior_members(['Rita', 'Roma', 'Ramil'])

    print('*** Итерируемся по команде в цикле for ***')
    for member in team:
        print(member)

    print('*** Итерируемся по команде в цикле while ***')
    # Получаем итератор из итерируемого объекта - экземпляра класса Team
    iterator = iter(team)
    while True:
        try:
            elem = next(iterator)
            print(elem)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
