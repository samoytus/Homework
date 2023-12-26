import abc


class AbstractUser(abc.ABC):

    @abc.abstractmethod
    def get_username(self):
        pass

    @abc.abstractmethod
    def get_full_name(self):
        pass


class BaseUser(AbstractUser):
    def __init__(self,
                 username: str,
                 email: str,
                 password: str,
                 first_name: str,
                 last_name: str,
                 is_admin: bool = False,
                 is_vip: bool = False) -> None:

        # атрибут       параметр
        self.username = username
        self.__email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.__is_admin = is_admin
        self.is_vip = is_vip
        print(f'Объект {self} создан!')

    def get_username(self) -> str:
        return self.username

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, other):
        if not isinstance(other, str):
            raise ValueError('Тип почты должен быть строкой')

        if '@' not in other:
            raise ValueError('Некорректный email')
        self.__email = other

    @property
    def is_admin(self) -> bool:  # Для получения
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value):  # Для установки нового значения
        if not isinstance(value, bool):
            raise TypeError('Тип значения должно быть булевое')
        self.__is_admin = value

    def __method_name(self):
        return f'{self} какой-то текст'


class Admin(BaseUser):
    """Класс администратора."""


class PremiumUser(BaseUser):
    """Класс премиум пользователя."""


admin_1: Admin = Admin('ivan',
                       'ivan@mail.com',
                       'qwerty123',
                       'Ivan',
                       'Ivanov',
                       is_admin=True)

print(admin_1.get_username())
print(admin_1.get_full_name())
admin_1.email = 'ivanov@mail.com'
admin_1.is_admin = None
print(admin_1.is_admin)
print(admin_1.email)

# print(admin_1.__method_name())

pr = PremiumUser('max',
                 'max@mil.ru',
                 'strong124',
                 'Максим',
                 'Смирнов',
                 is_vip=True)
