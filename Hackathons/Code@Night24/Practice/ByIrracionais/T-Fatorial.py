num = int(input())
valor = 0
while True:
    if num >= 40320:
        num -= 40320
        valor += 1
    elif num >= 5040:
        num -= 5040
        valor += 1
    elif num >= 720:
        num -= 720
        valor += 1
    elif num >= 120:
        num -= 120
        valor += 1
    elif num >= 24:
        num -= 24
        valor += 1
    elif num >= 6:
        num -= 6
        valor += 1
    elif num >= 2:
        num -= 2
        valor += 1
    elif num >= 1:
        num -= 1
        valor += 1
    else:
        print(valor)
        break
    
    