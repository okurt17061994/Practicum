print("Поиск среднего числа в списке")
#a = (-4, 3, 10, 15)
a = (1, 2, 3, 4, 5)

def find_average(a):
    return sum(a) / len(a) if a else 0

print(find_average(a))