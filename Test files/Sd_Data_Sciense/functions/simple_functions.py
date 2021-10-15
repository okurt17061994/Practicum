## Functions

def add(x, y):
    return x + y

print(add (2, 3))

add (4, 7)

print("___________________________________________________")
print("___________________________________________________")

def square(x):
    print("Квадрат числа", x, ":", x ** 2 )

square(2)

print("___________________________________________________")
print("___________________________________________________")

def hello (name="World"):
	print("Hi", name)

hello ("Jone")
hello()

print("___________________________________________________")
print("___________________________________________________")

# Записываем курс в переменной rubles_for_dollar
# (англ. rubles for dollar, "рублей за доллар").
rubles_for_dollar = 73


def print_budget_in_rubles(dollars):
	rubles = dollars * rubles_for_dollar
	print('Бюджет: {:.2f} млн ₽'.format(rubles))

print('Титаник')
print_budget_in_rubles(200.0)
print()
print('Гладиатор')
print_budget_in_rubles(103.0)

