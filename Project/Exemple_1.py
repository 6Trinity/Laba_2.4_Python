import sys
A = list(map(int, input().split()))
if len(A) != 10: print("Неверный размер списка", file=sys.stderr), exit(1)
s = sum([a for a in A if abs(a) < 5])
print("Сумма чисел больших по модулую 5: {0}".format(s))