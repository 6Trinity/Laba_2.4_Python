import sys
a = list(map(int, input("Введите спосок цифр").split()))
if not a: print("Заданный список пуст", file=sys.stderr), exit(1)
start = a.index(0)
end = ~a[::-1].index(0)
a_sum_0 = sum(a[start:end])
a_len = len(a)
a_sum = 0
minus = []
plus = []
for i in range(a_len):
    if (i + 1) % 2 == 0: a_sum += a[i]
print("Сумма элементов между первым и последнем нулевым элемент: {0}\nСумма четных элементов {1}".format(a_sum_0, a_sum))
for i in a:
    if (i < 0):
        minus.append(i)
    else:
        plus.append(i)
for i in minus: plus.append(i)
print(plus)


