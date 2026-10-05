#Função Somar
def somar(a, b):
    return a + b
    
#Função Média
def media(x, y):
    return (x + y) / 2

#Função Saudação
def saudacao(nome, saudacao_tipo = "Olá"):
    print(f"{saudacao_tipo}, {nome}!")
    
#Função Cadastrar Endereço
def cadastrar_endereco(rua = "Rua Projetada", numero = "Sem Número"):
    print(f"Endereço: {rua}, {numero}")



#Printando o resultado Soma de duas formas
resultado = somar(3, 5)
print(resultado)
print(f"{somar(3, 5)}\n")

#Printando o resultado Média de duas formas
resultadoMedia = media(7, 9)
print(f"{resultadoMedia}")
print(f"{media(7, 9)}\n")

#Printando a função Saudação
saudacao("Wesley")
saudacao("Wesley", "Bom dia")

#Cadastrando um Endereço
cadastrar_endereco("Rua das Flores", "123")
cadastrar_endereco("Rua das Flores")
cadastrar_endereco()



