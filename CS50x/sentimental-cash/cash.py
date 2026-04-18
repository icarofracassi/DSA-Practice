from cs50 import get_float
import math

cashinput = 0
coins = [25, 10, 5, 1]
while True:
    cashinput = get_float("Change: ")*100
    try:
        cashinput = int(cashinput)
    except ValueError:
        continue
    else:
        if cashinput > 0:
            break

finalcount = 0
for coinvalue in coins:
    coinscount = cashinput / coinvalue
    coinscount = math.floor(coinscount)
    cashinput = cashinput - coinscount*coinvalue
    finalcount = finalcount + coinscount

print(finalcount)
