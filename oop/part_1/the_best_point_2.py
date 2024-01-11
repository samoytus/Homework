class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __calc_distance(self, x1, y1, x2, y2):
        expr = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
        return round(expr ** 0.5, 2)

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def length(self, obj: 'Point'):
        # x1 = self.x
        # y1 = self.y
        #
        # x2 = obj.x
        # y2 = obj.y

        return self.__calc_distance(self.x, self.y, obj.x, obj.y)


if __name__ == '__main__':
    first_point = Point(2, -7)
    second_point = Point(7, 9)
    print(first_point.length(second_point))
    print(second_point.length(first_point))

"""    point = Point(3, 5)
    print(point.x, point.y)
    point.move(2, -3)
    print(point.x, point.y)
"""
#   # Дом x - 5, 1
#
#     # ТЦ y - 10, 7
#
#     x1 = 5
#     x2 = 1
#
#     y1 = 10
#     y2 = 7
#
#     res_x = (x2 - x1) ** 2
#     res_y = (y2 - y1) ** 2
#
#     total = (res_x + res_y) ** 0.5
#     print(total)
#     # -------------------------
#
#     # ТЦ 10, 2
#
#     # Дом 5, 9
#
#     # from math import sqrt
#     # 9 ** 0.5
