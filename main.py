money = float(input("Введите сумму вклада: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = [ per_cent['ТКБ']*money/100,
            per_cent['СКБ']*money/100,
            per_cent['ВТБ']*money/100,
            per_cent['СБЕР']*money/100 ]
deposit.sort()
print("Максимальная сумма, которую вы можете заработать — ", deposit[-1])
