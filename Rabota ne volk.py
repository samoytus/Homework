class Programmer:

    __RANK = {
        'Junior': 10,
        'Middle': 15,
        'Senior': 20,
    }

    def __init__(self, name: str, position: str) -> None:
        self.name = name
        self.position = position
        self.salary = 0
        self.work_time = 0
        self.bonus = 0

    def work(self, time: int) -> None:
        self.work_time += time
        self.salary += (self.__RANK[self.position] + self.bonus) * time

    def rise(self):
        if self.__RANK[self.position] < 20:
            self.__RANK[self.position] += 5
        else:
            self.bonus += 1

    def info(self):
        return f'{self.name} {self.work_time}ч. {self.salary}тгр.'


