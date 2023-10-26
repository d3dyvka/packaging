#first
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)
print("\n")
#second
x, y, a = (1, 2, 5)
print(x)
print(y)
print(a)
print("\n")
#third
name, age, company = ("Илья", 18, "НГТУ")
print(name)
print(age)
print(company)
print("\n")
#fourth
people = ["Андрей", "Екатерина", "Сергей"]
first, second, third = people
print(first)
print(second)
print(third)
print("\n")
#fifth
dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
r, b, g = dictionary
print(r)
print(b)
print(g)
# получаем значение по ключу
print(dictionary[g])
print("\n")
#sixth
people = [
    ("Андрей", 17, "НГТУ"),
    ("Екатерина", 17, "НГУ"),
    ("Сергей", 19, "НГУЭУ")
]

for name, age, company in people:
    print(f"Name: {name}, Age: {age}, Company: {company}")
print("\n")
#seventh
people = ["Андрей", "Екатерина", "Сергей"]
for index, name in enumerate(people):
    print(f"{index}.{name}")
print("\n")
#eighth
person =("Илья", 18, "НГТУ")
name, _, company = person
print(name)
print(company)
print(_)
print("\n")
#ninght
num1=1
num2=2
num3=3
*numbers,=num1,num2,num3
print(numbers)
print("\n")
#ten
head, *tail = [1, 2, 3, 4, 5]

print(head)
print(tail)
print("\n")
#eleven
*head, tail = [1, 2, 3, 4, 5]

print(head)
print(tail)
print("\n")
#twelve
head, *middle, tail = [1, 2, 3, 4, 5]

print(head)
print(middle)
print(tail)
print("\n")
#13
first, second, *other = [1, 2, 3, 4, 5]

print(first)
print(second)
print(other)
print("\n")
#14
first, _, third, *_, last = [1, 2, 3, 4, 5, 6, 7, 8]

print(first)
print(third)
print(last)
print("\n")
#15
red, *other, green = {"red":"красный", "blue":"синий", "yellow":"желтый", "green":"зеленый"}

print(red)
print(green)
print(other)
print("\n")
#16
nums1 = [1, 2, 3]
nums2 = (4, 5, 6)

# распаковываем список nums1 и кортеж nums2
nums3 = [*nums1, *nums2]
print(nums3)
print("\n")
#17
dictionary1 = {"red":"красный", "blue":"синий"}
dictionary2 = {"green":"зеленый", "yellow":"желтый"}

# распаковываем словари
dictionary3 = {**dictionary1, **dictionary2}
print(dictionary3)