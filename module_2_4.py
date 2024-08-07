numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]    # Исходный список
primes = []
not_primes = []
ind = 0
is_prime = True                                                 # Переменная - флаг
for i in numbers:
    if i == 1:                                                  # Пропускаем 1
        continue
    for j in range(1, i+1):                                     # Перебор с первого до текущего элемента списка
        if i % j == 0:
            ind = ind + 1
    if ind == 2 and is_prime == True:                           # Если флаг - Истина
        primes.append(i)
    else:
        not_primes.append(i)
    ind = 0
print('-----------------------------')
print(primes, '<- Простые числа')                                 # Список простых чисел
print('-----------------------------')
print(not_primes,'<- Числа, не являющиеся простыми')              # Список  чисел не явл. простыми