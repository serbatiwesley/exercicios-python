def calcular_media(lista):
    resultado = 0
    for i in range(len(lista)):
        resultado = resultado + lista[i]
    return resultado / len(lista)

nomes = []
notas = []
alunos = 0

while (alunos <= 0):
    entrada = input("Quantos alunos? ")
    alunos = int(entrada)
    if (alunos <= 0): 
        print(f"Quantidade invalida, tente novamente.\n")
    
for i in range(alunos):
    nomes.append(input("\nInforme o nome do aluno: "))
    while (True):
        nota = input(f"Informe a nota do(a) {nomes[i]}: ")
        try:
            notas.append(float(nota))
            break
        except ValueError:
            print("Isso não é um número válido!")
    print(f"Nome do aluno: {nomes[i]} / Nota: {notas[i]}")

media = calcular_media(notas)

print(f"\n-----------------------\nMédia da turma: {media:.2f}\n-----------------------\n")
for i in range(len(nomes)):
    print(f"Aluno {i+1} = Nome: {nomes[i]} / Nota: {notas[i]}")
    if (notas[i] >= 6):
        print("| APROVADO! |\n")
    else:
        print("| REPROVADO! |\n")