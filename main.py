dict_ = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
a = sorted(students)
b = sum(grades[0])/ len(grades[0])
c = sum(grades[1])/ len(grades[1])
d = sum(grades[2])/ len(grades[2])
e = sum(grades[3])/ len(grades[3])
f = sum(grades[4])/ len(grades[4])
dict_.update({a[0]:b, a[1]:c, a[2]:d, a[3]:e, a[4]:f})
print(dict_)