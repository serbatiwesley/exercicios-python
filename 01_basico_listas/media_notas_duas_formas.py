notas = [8.5, 4.0, 6.0, 9.5, 3.5, 7.0]
acumulador = 0

for i in notas:
    acumulador = acumulador + i
media = acumulador / len(notas)
print(f"A média é {media: .2f}")

acumulador = 0

for i in range(len(notas)):
    acumulador = acumulador + notas[i]
media = acumulador / len(notas)
print(f"A média é {media: .2f}")

for i in range(len(notas)):
    if notas[i] >= 6:
        print(f"Aluno {i+1}: Aprovado")
    else:
        print(f"Aluno {i+1}: Reprovado")