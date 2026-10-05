alunos = [
    {"codigo": "1", "nome": "Wess", "nota": 5.0},
    {"codigo": "2", "nome": "Ana", "nota": 7.0},
    {"codigo": "3", "nome": "Guilherme", "nota": 4.0}
]

print(alunos)

codigo = input("Informe o código do aluno que deseja alterar a nota: ")
nota_nova = float(input("Informe a nova nota do aluno: "))

for i in range(len(alunos)):
    if alunos[i]["codigo"] == codigo:
        alunos[i]["nota"] = nota_nova
        
print("\n", alunos)