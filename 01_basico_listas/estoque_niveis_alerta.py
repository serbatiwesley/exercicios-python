produtos = ["Caneta", "Caderno", "Mouse", "Teclado", "Monitor"]
quantidades = [45, 0, 8, 15, 3]
total = 0

print("--STATUS DE ESTOQUE--")
for i in range(len(produtos)):
    if (quantidades[i] <= 10):
        if (quantidades[i] == 0):
            print(f"({i + 1}º) {produtos[i]}: ESGOTADO")
        else:
            print(f"({i + 1}º) {produtos[i]}: BAIXO")
    else:
        print(f"({i + 1}º) {produtos[i]}: OK")
    total = total + quantidades[i]
print("O total do estoque é: ", total)