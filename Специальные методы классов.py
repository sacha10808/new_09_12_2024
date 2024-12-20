class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self,new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i + 1)
    def __str__(self):
        return self.name
    def __len__(self):
        return self.number_of_floors


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
print(f'Название: {str(h1)}, количество этажей: {len(h1)}')
print(f'Название: {str(h2)}, количество этажей: {len(h2)}')
print(len(h1))
print(len(h2))