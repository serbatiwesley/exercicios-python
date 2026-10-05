# TUPLA: cada sessão é um dado fixo, que não deveria mudar (nome, horário)
sessoes = [
    ("Introdução a ML", "09:00"),
    ("Estruturas de Dados na Prática", "10:30"),
    ("Python para Ciência de Dados", "14:00"),
]

# LISTA de DICIONÁRIOS: cada participante é um registro, e a lista pode crescer
participantes = []

def inscrever(participante, sessao):
    participante['sessoes_inscritas'].add(sessao)

while True:
    quantidade = input("Informe quantos participantes serão cadastrados: ")
    try:
        quantidade = int(quantidade)
        if quantidade < 0:
            print("ERRO: Informe um número positivo!")
        else:
            break
    except ValueError:
            print("ERRO: Isso não é um número!")
   
for i in range(quantidade):
    nome = input("Informe o nome: ")
    email = input("Informe o email: ")
    
    participante_atual = {
        "nome": nome,
        "email": email,
        "sessoes_inscritas": set()
    }

    participantes.append(participante_atual)

for participante in participantes:
    print(f"\n--- Seleção de Sessão para: {participante['nome']} ---")
        
    continuar = True
    while continuar:
        for indice, (sessao, horario) in enumerate(sessoes):
            print(f"[{indice + 1}] {sessao}: {horario}")
        opcao = input("Digite o número da sessão desejada: ")
        try:
            opcao_ind = int(opcao) - 1
            if 0 <= opcao_ind < len(sessoes):
                inscrever(participante, sessoes[opcao_ind][0])
            else:
                print("ERRO: Número inválido! Escolha uma opção da lista.")
        except ValueError:
            print("ERRO: Digite apenas o número da opção.")
        resposta = input("Deseja se inscrever em outra sessão? (s/n): ")
        if resposta != "s":
            continuar = False

nomes_inscritos_ml = [participante['nome'] for participante in participantes if "Introdução a ML" in participante['sessoes_inscritas']]
    
for participante in participantes:
    print(f"Nome: {participante['nome']} | Total de Sessões: {len(participante['sessoes_inscritas'])}")
  
  
  