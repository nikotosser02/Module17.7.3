
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input ("Введите желаемую сумму вклада: "))

list_per_cent = {}
for a in per_cent:
    # max_pers1 = \
    list_per_cent[a]=money * float(per_cent[a]) #перемножаем вклад на проценты
    # if max_pers<max_pers1:
    #     max_pers = max_pers1
    #     best_bank = max_pers1
    #     print("<fyr>: ", best_bank)
best_bank_max_pers = max(list_per_cent.values()) #для поиска максимального

print("Проценты доходности по банкам: ", per_cent)
print("Доход составит по вкладам в банках: ", list_per_cent)
print("Максимальный доход: ", best_bank_max_pers)
