class Human:
    default_name = 'No name'
    default_age = 0

    def __init__(self, name: str = default_name, age: int = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'\nName: {self.name} '
              f'\nAge: {self.age} '
              f'\nHouse: {self.__house} '
              f'\nMoney: {self.__money}')

    @staticmethod
    def default_info():
        print(f'\nDefault Name: {Human.default_name} '
              f'\nDefault Age: {Human.default_age}')

    def __make_deal(self, house: 'House', price: int | float) -> None:
        # реализация покупки дома
        self.__money -= price
        self.__house = house

    def earn_money(self, amount: int | float) -> None:
        self.__money += amount
        print(f'Earned {amount} money! Current value: {self.__money}')

    def buy_house(self, house: 'House', discount: float) -> None:
        price: float = house.final_price(discount)

        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('Не достаточно денег')

class House:
    def __init__(self, area: str , price: int | float):
        self._area = area
        self._price = price

    def final_price(self, discount: float):
        final_price = self._price * (100 - discount) / 100
        print(f'Final price: {final_price}')
        return final_price


class SmallHouse(House):

    default_area = 40
    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)

    def __str__(self):
        return f"House: area={self._area}, price={self._price}"



# Пример использования классов Human, House и SmallHouse
Human.default_info()
h_1 = Human('Andrey', 28)
h_1.info()
small_house = SmallHouse(8500)
h_1.buy_house(small_house, 10)
h_1.earn_money(5000)
h_1.buy_house(small_house, 10)
h_1.earn_money(10000)
h_1.buy_house(small_house, 10)
h_1.info()