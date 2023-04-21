import sys
a = list(map(int, input("Введите спосок цифр").split()))
if not a: print("Заданный список пуст", file=sys.stderr), exit(1)
a_min = a[0]
a_len = len(a)
for i in a:
    if i < a_min: a_min=i
    a[a_len - 1] = a_min
for i in range(a_len): print("{0} ".format(a[i]))

