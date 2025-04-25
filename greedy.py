cost = 132
money = 200

banknot_type = [200, 100, 50, 20, 10, 5, 1]

amount = money - cost
print("Geri verilmesi gereken tutar : ", amount)
cashback_list = []

for banknot in banknot_type:
    while banknot<=amount:
        cashback_list.append(banknot)
        amount -= banknot # amount = amount - banknot

print("Geri verilen tutar :")
print(cashback_list)

