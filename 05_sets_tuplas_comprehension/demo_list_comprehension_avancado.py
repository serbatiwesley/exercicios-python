funcionarios = [
    {"nome": "Carlos", "cargo": "Analista", "salario": 4500.00, "anos_empresa": 3},
    {"nome": "Fernanda", "cargo": "Gerente", "salario": 9000.00, "anos_empresa": 8},
    {"nome": "Bruno", "cargo": "Estagiário", "salario": 1800.00, "anos_empresa": 1},
    {"nome": "Juliana", "cargo": "Analista", "salario": 4800.00, "anos_empresa": 5},
    {"nome": "Rafael", "cargo": "Diretor", "salario": 15000.00, "anos_empresa": 12},
    {"nome": "Patrícia", "cargo": "Estagiário", "salario": 1800.00, "anos_empresa": 1},
]

nomes_gerencia = [funcionario['nome'] for funcionario in funcionarios if funcionario['cargo'] == 'Gerente' or funcionario['cargo'] == 'Diretor']

print(nomes_gerencia)

salarios_com_reajuste = [funcionario['salario'] * 1.1 for funcionario in funcionarios]

print(salarios_com_reajuste)

nomes_veteranos = [funcionario['nome'].upper() for funcionario in funcionarios if funcionario['anos_empresa'] > 4]

print(nomes_veteranos)

resumo = [f"{funcionario['nome']} - {funcionario['cargo']}" for funcionario in funcionarios if funcionario['salario'] > 4000]

print(resumo)