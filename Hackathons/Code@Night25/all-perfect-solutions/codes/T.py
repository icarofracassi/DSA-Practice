values = input().split()
values.pop()
n = len(values)

result = True
start_info = int(values[0]) > 0
last = int(values[0])

for i in range(int(n/2)):
    j = n-i-1
    vi = int(values[i])
    vj = int(values[j])
    breakCase1 = abs(vi) != abs(vj)
    breakCase2 = (vi > 0) ^ start_info
    breakCase3 = last > vi
    if breakCase1 or breakCase2 or breakCase3:
        result = False
        break
    last = vi

if result:
    print("SEQUENCIA VALIDA")
else:
    print("SEQUENCIA INVALIDA")