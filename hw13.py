# 13.8.19 (HW-03)

ticketQty = int(input('Input ticket quantity: '))
if ticketQty not in range(1, 1000):
    print('Неверно указано количество!')
    exit(0)

age = int(input('Input your age: '))

price = None
if age in range(0, 18):
    price = 0
elif age in range(18, 25):
    price = 990
elif age >= 25:
    price = 1390
else:
    print('Неверно указан возраст!')
    exit(1)

cost = ticketQty * price

discount = 0
if ticketQty > 3:
    discount = 0.1

cost -= cost * discount

print(f'С вас {cost} рублей за {ticketQty} шт. по цене {price}. Ваша скидка: {discount * 100} %')
