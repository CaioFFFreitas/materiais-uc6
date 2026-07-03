

# ! CRIANDO UMA LISTA VAZIA
produtos = []

# ? Variável auxiliar para controlar o loop principal
sair = False

print("Bem vindo ao Sistema de Estoque!")
# ! Repita enquanto sair é igual a false
while sair == False:
    
    # ? Menu dentro do Loop Para Repetir
    print("-"*20)
    print("1- Listar Produtos")
    print("2- Cadastrar um Novo Produto")
    print("3- Deletar um Produto")
    print("0- Sair do Sistema")
    print("-"*20)
    # ! Pedir para a pessoa digitar a opção:
    opcao = input("Sua opção: ")
    # ! Escolha Caso / Match Case
    match opcao:
        case '0':
            # ? Colocamos sair como verdadeiro para que quando rodar o loop ele sair.
            sair = True
        case '1':
            print("Lista de Produtos:")
            for p in produtos:
                print("- ", p)
            print("#"*30)
            input("Pressione enter para continuar...")
        case '2':
            print("Cadastrar novo produto:")
            nome_produto = input("Nome do Produto: ")
            # ! A função append adiciona um novo item em uma lista
            produtos.append(nome_produto)
        case '3':
            print("Remover Produto:")
            nome_produto = input("Qual deletado: ")
            # ! Checar se o deletado existe na lista
            if nome_produto in produtos:
                produtos.remove(nome_produto)
                print("Removido com sucesso!")
            else:
                print(nome_produto, " não existe na lista!")
            
            input("Pressione enter para continuar...")

