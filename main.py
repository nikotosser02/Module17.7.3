
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input ("Введите желаемую сумму вклада: "))

list_per_cent = {}
for a in per_cent:
    list_per_cent[a]=round(money * (float(per_cent[a]/100)), 2) #перемножаем вклад на проценты
best_bank_max_pers = max(list_per_cent.values()) #для поиска максимального

print("Проценты доходности по банкам: ", per_cent)
print("Доход составит по вкладам в банках: ", list_per_cent)
print("Максимальный доход: ", round(best_bank_max_pers, 2))
