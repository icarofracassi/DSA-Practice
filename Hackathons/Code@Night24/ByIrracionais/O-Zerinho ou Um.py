valores = input().split(" ")
a = valores[0]
b = valores[1]
c = valores[2]
if a == b == c:
  print("*")
elif a == b:
  print("C")
elif b == c:
  print("A")
elif a == c:
  print("B")
