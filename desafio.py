# Função para exibir o menu e obter a escolha do usuário
def exibir_menu():
    print("\nAgenda de Contatos")
    print("1. Adicionar um novo contato")
    print("2. Visualizar a lista de contatos cadastrados")
    print("3. Editar um contato existente")
    print("4. Marcar/desmarcar um contato como favorito")
    print("5. Ver lista de contatos favoritos")
    print("6. Apagar um contato")
    print("7. Sair da agenda")
    escolha = input("\nPor favor, digite o número correspondente à opção desejada: ")
    return escolha

# Função para adicionar um novo contato
def adicionar_contato(contatos):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    favorito = input("Marcar como favorito? (S/N): ").upper()
    if favorito == "S":
        favorito = True
    else:
        favorito = False
    novo_contato = {"Nome": nome, "Telefone": telefone, "Email": email, "Favorito": favorito}
    contatos.append(novo_contato)
    print("Contato adicionado com sucesso!")

# Função para visualizar a lista de contatos cadastrados
def visualizar_contatos(contatos):
    print("\nLista de Contatos:")
    for index, contato in enumerate(contatos, start=1):
        print(f"{index}. Nome: {contato['Nome']}, Telefone: {contato['Telefone']}, Email: {contato['Email']}, Favorito: {contato['Favorito']}")

# Função para editar um contato existente
def editar_contato(contatos):
    visualizar_contatos(contatos)
    indice = int(input("\nDigite o número do contato que deseja editar: ")) - 1
    contato = contatos[indice]
    print("Editar contato:")
    for chave, valor in contato.items():
        novo_valor = input(f"Novo {chave}: ")
        contato[chave] = novo_valor
    print("Contato editado com sucesso!")

# Função para marcar/desmarcar um contato como favorito
def marcar_favorito(contatos):
    visualizar_contatos(contatos)
    indice = int(input("\nDigite o número do contato que deseja marcar/desmarcar como favorito: ")) - 1
    contato = contatos[indice]
    if contato['Favorito']:
        contato['Favorito'] = False
        print("Contato removido dos favoritos.")
    else:
        contato['Favorito'] = True
        print("Contato marcado como favorito.")

# Função para ver uma lista de contatos favoritos
def listar_favoritos(contatos):
    favoritos = [contato for contato in contatos if contato['Favorito']]
    print("\nLista de Contatos Favoritos:")
    for index, contato in enumerate(favoritos, start=1):
        print(f"{index}. Nome: {contato['Nome']}, Telefone: {contato['Telefone']}, Email: {contato['Email']}")

# Função para apagar um contato
def apagar_contato(contatos):
    visualizar_contatos(contatos)
    indice = int(input("\nDigite o número do contato que deseja apagar: ")) - 1
    del contatos[indice]
    print("Contato apagado com sucesso!")

# Função principal
def main():
    contatos = []
    while True:
        escolha = exibir_menu()
        if escolha == "1":
            adicionar_contato(contatos)
        elif escolha == "2":
            visualizar_contatos(contatos)
        elif escolha == "3":
            editar_contato(contatos)
        elif escolha == "4":
            marcar_favorito(contatos)
        elif escolha == "5":
            listar_favoritos(contatos)
        elif escolha == "6":
            apagar_contato(contatos)
        elif escolha == "7":
            print("Saindo da agenda. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()