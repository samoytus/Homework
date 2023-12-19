class Animal:
    def __init__(self, name: str, sex: str, age: int):
        self.name = name
        self.sex = sex
        self.age = age

    def run(self):
        return "Я умею бегать"

    def voice(self):
        return "Я умею издавать звуки"

    def eat(self):
        return "Мне нравится есть"

    def info(self):
        print(f'Меня зовут {self.name}! '
              f'Мой пол: {self.sex}. '
              f'Мне {self.age} лет!')


class Cat(Animal):
    def run(self):
        print("Кошка бегает")

    def voice(self):
        print("Я умею мурлыкать")

    def eat(self):
        print("Я люблю молоко")

    def info(self):
        print(f"Привет, моя кличка {self.name}, я игривая!")


class Dog(Animal):
    def run(self):
        print("Я бегаю быстрее всех")

    def voice(self):
        print("Громко рычу")

    def eat(self):
        print("Люблю кушать")

    def info(self):
        print(f"Привет, моя кличка {self.name}, я люблю своего хозяина!")


my_cat = Cat("Мурка", "Женский", 4)
my_cat.info()
my_cat.voice()

my_dog = Dog("Боб", "Мужской", 10)
my_dog.info()
my_dog.run()
