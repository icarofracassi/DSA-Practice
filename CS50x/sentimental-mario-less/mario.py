height = 0

while True:
    height = input("Height: ")
    if height.isdigit():
        height = int(height)
        if height > 0 and height < 9:
            break

#    except ValueError:
#    else:

for linha in range(1, height+1):
    for j in range(height-linha):
        print (' ',end="")
    for j in range(linha):
        print ("#",end="")
    print ("")
