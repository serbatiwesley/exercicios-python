
def aplicar_desconto(produto, percentual):
    novo_preco = produto["preco"] - (produto["preco"] * percentual / 100)
    produto["preco"] = novo_preco
    
def calcular_valor_total(produto):
    return produto["quantidade"] * produto["preco"]

produtos = []

cont = int(input("Quantos produtos deseja cadastrar? "))
while (cont <= 0):
    cont = int(input("Quantidade incorreta, digite um número superior a zero: "))
    
for i in range(cont):
    print(f"---Cadastro do {i + 1}º produto---")
    codigo = i + 1
    nome = input("Informe o nome do produto: ")
    quantidade = int(input("Informe a quantidade do produto: "))
    preco = float(input("Informe o preco do produto: R$ "))
    
    produto_atual = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    
    produtos.append(produto_atual)
    
print(produtos)

codigo_atual = int(input("Informe o código do produto a sofrer desconto: "))
if (codigo_atual == 0):
    print("Nenhum produto sofrerá alteração no valor")
else: 
    desconto = float(input("Informe o desconto: "))
    for i in range(len(produtos)):
          if (produtos[i]["codigo"] == codigo_atual):
              aplicar_desconto(produtos[i], desconto)

print("\n", produtos, "\n")

for i in range(len(produtos)):
    print(f"O valor total do estoque do {i + 1}º produto é: {calcular_valor_total(produtos[i])}")