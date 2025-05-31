# Estrutura de dados utilizada: dicionário para mapear o código do andar para o nome do andar
# Tipo de algoritmo: extração e formatação de string

floor_map = {
    'B': 'basement',
    'G': 'ground',
    '1': 'first',
    '2': 'second'
}

code = input().strip()
floor_code = code[0]
sector = code[1]
room_number = code[2:]

floor = floor_map.get(floor_code, floor_code)
print(f"Room {room_number} on the {floor} floor of sector {sector}")