n = int(input())
values = input().split('0')
aux1 = 0
aux2 = 0
for i in range(len(values)):
    if (len(values[i]) > aux1):
        aux1 = len(values[i])
        aux2 = len(values[i].split())

print(aux2)