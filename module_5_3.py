class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.number_of_floors_max = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors_max or new_floor < 1:
            print('Такого этажа не существует')
        else:
            self.number_of_floors = new_floor
            print(f'Вы в доме {self.name}, на {self.number_of_floors} этаже')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name},  кол-во этажей:  {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if not isinstance(other, House):
            print(f'Надо объект  House')
        else:
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        else:
            print(f"Необходимо прибавить целое число")
        return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        else:
            print(f"Необходимо прибавить целое число")
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        else:
            print(f"Необходимо прибавить целое число")
        return self


h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Альбатрос', 10)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h2 = h2 + 20     # __add__

print(h2)
print(h1)
print(h1 == h2)

h1 += 10          # __iadd__
print(h1)

h2 = 10 + h2      # __radd__
print(h2)

print(h1 > h2)     # __gt__
print(h1 >= h2)    # __ge__
print(h1 < h2)     # __lt__
print(h1 <= h2)    # __le__
print(h1 != h2)    # __ne__
