first_ = int(input('Введите first'))
second_ = int(input('Введите second'))
third_ = int(input('Введите third'))
if first_ == second_ == third_:
    print(3)
elif first_ == second_ or first_ == third_ or second_ == third_:
    print(2)
else:
    print(0)
