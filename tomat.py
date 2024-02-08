class Tomato:
    states: dict[int, str] = {
        1: 'Отсутствует',
        2: 'Цветение',
        3: 'Зеленый',
        4: 'Красный'
    }

    def __init__(self, index: int) -> None:
        self.__current_state = 1
        self._index = index
        self._state = Tomato.states[self.__current_state]

    def grow(self):
        if self.is_ripe():
            raise ValueError(
                'Томат уже находится в финальном стадии созревания'
            )

        self.__current_state += 1
        self._state = Tomato.states[self.__current_state]  # Важно!

    def is_ripe(self):
        return self.__current_state == len(Tomato.states)

    def __str__(self):
        return f'\nTomato: {self._index}\nТекущая стадия: {self._state}'


class TomatoBush:
    def __init__(self, amount: int) -> None:
        self.quantity = amount  # для примера разные названия.
        # self.tomatoes = [Tomato(idx) for idx in range(1, self.quantity + 1)]
        self.tomatoes = []
        for idx in range(1, self.quantity + 1):
            self.tomatoes.append(Tomato(idx))

    def grow_all(self):
        for item in self.tomatoes:
            if not item.is_ripe():
                item.grow()

    def all_are_ripe(self):
        # TODO:
        pass

    def give_away_all(self):
        self.tomatoes.clear()


if __name__ == '__main__':
    obj = Tomato(10012)
    print(obj)
    obj.grow()
    obj.grow()
    obj.grow()
    print(obj)

    # obj: list[Tomato, ...] = []
    # for idx in range(1, self.quantity + 1):
    #     obj.append(Tomato(idx))
    #
    # print(obj)

    #
    # for item in obj:
    #     print(item)
