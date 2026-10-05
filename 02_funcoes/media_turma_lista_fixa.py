def calcular_media(notas):
    acumulador = 0
    for i in range(len(notas)):
        acumulador = acumulador + notas[i]
    return acumulador / len(notas)

turma = [7.0, 8.5, 6.0, 9.0, 5.5]
media = calcular_media(turma)

print(f"Média da turma: {media:.2f}")
if (media >= 7):
    print("Turma com bom desempenho!")
else: 
    print("Turma precisa de reforço.")