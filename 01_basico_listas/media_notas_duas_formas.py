notas = [8.5, 4.0, 9.0, 6.5, 3.0, 7.0, 10.0]

quantidade = 0
total = 0

for nota in notas:
    total += nota
    quantidade += 1

media = total / quantidade
print(f"A média da turma é: {media:.2f}")
""
total = 0

for i in range(len(notas)):
    total += notas[i]

media = total / len(notas)
print(f"A média da turma é: {media:.2f}")