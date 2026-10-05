def buscar_livro(livros, titulo):
    for i in range(len(livros)):
        if livros[i]["Título"] == titulo:
            print(f"O índice do livro é {i}")
            return i
    print("-1")
    return -1
    
def emprestar_livro(livros, titulo):
    for i in range(len(livros)):
        if (livros[i]["Título"] == titulo):
            if livros[i]["Cópias disponíveis"] > 0:
                livros[i]["Cópias disponíveis"] -= 1
                print(f"Um livro de título {livros[i]['Título']} foi emprestado!")
                return
            else:
                print("Não há cópias disponíveis.")
                return

livros = []

while True:
    try:
        quantidade = int(input("Informe a quantidade de livros para cadastro: "))
        if quantidade <= 0:
            print("ERRO: Informe um número maior que zero.\n")
        else: 
            break
    except ValueError:
        print("ERRO: Isso não é um número.\n")

for i in range(quantidade):
    titulo = input("Informe o título do livro: ")
    autor = input("Informe o autor do livro: ")
    while (True):
        try:
            copias = int(input("informe quantas cópias estão disponíveis: "))
            if (copias < 0):
                print("ERRO: Informe um número positivo ou zero no caso de não haver cópias.\n")
                pass
            else: 
                print(copias)
                break
        except (ValueError):
            print("ERRO: Isso não é um número.\n")
        
    livro_atual = {
        "Título" : titulo,
        "Autor" : autor,
        "Cópias disponíveis" : copias,
    }
    
    livros.append(livro_atual)

titulo_busca = input("Informe um título para ser buscado e emprestado: ")
indice = buscar_livro(livros, titulo_busca)
if indice == -1:
    print("Não foi encontrado nenhum livro com esse título.")
else:
    emprestar_livro(livros, titulo_busca)
    
for i in range(len(livros)):
    print (f"---{i+1}º livro---")
    print(f"Título: {livros[i]['Título']}")
    print(f"Autor: {livros[i]['Autor']}")
    print(f"Cópias disponíveis: {livros[i]['Cópias disponíveis']}\n")
