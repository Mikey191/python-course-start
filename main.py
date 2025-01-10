print(hash("hello"))  # Хэш строки
print(hash(42))  # Хэш числа
print(hash((1, 2, 3)))  # Хэш кортежа
print(hash((1, 2, 3)).__xor__(12))  # Хэш кортежа
