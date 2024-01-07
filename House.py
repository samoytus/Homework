class Human:
    default_name = 'No name'
    default_age = 0

    def __init__(self, name: str = default_name, age: int = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'\nName: {self.name}, '
              f'\nAge: {self.age}, '
              f'\nHouse: {self.__house}, '
              f'\nMoney: {self.__money}')

    @staticmethod
    def default_info():
        print(f'\nDefault Name: {Human.default_name}, '
              f'\nDefault Age: {Human.default_age}')

    def make_deal(self, house: 'House', price: int | float) -> None:
        # реализация покупки дома
        self.__money -= price
        self.__house = house

    def earn_money(self, amount: int | float) -> None:
        self.__money += amount

    def buy_house(self, house: 'House', discount: float) -> None:
        house_price: float = house.final_price(discount)

        if self.__money < house_price:
            raise ValueError('Недостаточно денег')
        self.__money -= house_price

class House:
    def __init__(self, area: str , price: int | float):
        self._area = area
        self._price = price

    def final_price(self, discount: float):
        final_price = self._price * (100 - discount) / 100
        print(f'Final price: {final_price}')
        return final_price


class SmallHouse(House):
    def __init__(self, small_area='40m2', small_price=500):
        self.area = small_area
        self.price = small_price
        super().__init__(area=small_area, price=small_price)


# Пример использования классов Human, House и SmallHouse
Human.default_info()
person = Human('John', 28)
person.info()

small_house = SmallHouse(600)
person.buy_house(small_house, 10)

person.earn_money(5000)
person.buy_house(small_house, 10)

person.earn_money(5000)
person.buy_house(small_house, 10)
person.info()
# person.earn_money(700)
# person.buy_house(small_house, 100)
# person.info()
