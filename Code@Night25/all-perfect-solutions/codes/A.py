entrada1 = input().split()
entrada2 = input().split()
status = True

for i in range(5):
    if entrada1[i] == entrada2[i]:
        status = False
        break

if status:
    print("Y")
else:
    print("N")