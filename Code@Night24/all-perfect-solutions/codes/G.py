# Estrutura de dados utilizada: listas para armazenar eventos e horários de massagem
# Tipo de algoritmo: verificação de sobreposição de intervalos (interval overlap checking)

def time_to_minutes(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m

dias_semana = {2: 'segunda', 3: 'terça', 4: 'quarta', 5: 'quinta', 6: 'sexta'}

e1, e2 = map(int, input().split())
eventos = []
for _ in range(e1):
    d, h, m = input().split()
    d = int(d)
    ini = time_to_minutes(h)
    fim = ini + int(m)
    eventos.append((d, ini, fim))

massagens = []
for _ in range(e2):
    d, h = input().split()
    d = int(d)
    ini = time_to_minutes(h)
    fim = ini + 10
    massagens.append((d, ini, fim, h))

# Ordena por dia e horário
massagens.sort()

def livre(massagem):
    d, ini, fim, _ = massagem
    for ed, eini, efim in eventos:
        if d == ed and not (fim <= eini or ini >= efim):
            return False
    return True

for massagem in massagens:
    if livre(massagem):
        print(f"{massagem[3]} na {dias_semana[massagem[0]]}")
        break
else:
    print("Sem massagem essa semana :(")