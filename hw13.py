# 13.8.19 (HW-03)

ticketQty = int(input('Input ticket quantity: '))
if ticketQty not in range(1, 1000):
    print('Invalid quantity value!')
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
    print('Invalid age value!')
    exit(1)

cost = ticketQty * price

discount = 0
if ticketQty > 3:
    discount = 0.1

cost -= cost * discount

print(f'Total cost: {cost} RUR for {ticketQty} pcs. Price of each {price} RUR. Your discount: {discount * 100} %')
