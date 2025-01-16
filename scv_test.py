import sys
sys.stdin = open('books.csv', 'r')


c = 0
for i in range(9410):
    a = input()
    k = a.count(';')
    if k != 12:
        print(i + 1, k, a)
        c += 1
print(c)