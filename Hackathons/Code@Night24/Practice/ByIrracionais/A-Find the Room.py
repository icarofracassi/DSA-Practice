code = input()

floors = {
  "B": "basement",
  "G": "ground",
  "1": "first",
  "2": "second"
}

floorCode = code[0]
floor = floors.get(floorCode)
sector = code[1]
room = code[2] + code[3]
print(f'Room {room} on the {floor} foor of sector {sector}')
