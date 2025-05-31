# Estrutura de dados utilizada: lista de tuplas para armazenar intervalos de datas (interval scheduling)
# Algoritmo: verificação de sobreposição de intervalos

def to_day_of_year(date):
    # Dias acumulados até o início de cada mês (não bissexto)
    days_in_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    day, month = map(int, date.split('-'))
    return days_in_month[month - 1] + day

N = int(input())
intervals = []
for _ in range(N):
    start, end = input().split()
    intervals.append((to_day_of_year(start), to_day_of_year(end)))

joao_start, joao_end = input().split()
joao_start = to_day_of_year(joao_start)
joao_end = to_day_of_year(joao_end)

possible = True
for start, end in intervals:
    # Verifica se há sobreposição de intervalos
    if not (joao_end < start or joao_start > end):
        possible = False
        break

print("Sim" if possible else "Nao")