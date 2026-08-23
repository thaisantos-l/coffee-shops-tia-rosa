import banco
from modelos import Cliente
from utilitarios import mostrar_titulo, pausar, ler_texto, ler_numero_int
from utilitarios import confirmar

PONTOS_PARA_BRINDE = 100

def buscar_cliente(codigo):
    for cliente in banco.lista_clientes:
        if cliente.codigo == codigo:
            return cliente

    return None

def mostrar_tabela_clientes():
    if len(banco.lista_clientes) == 0:
        print("Nenhum cliente cadastrado ainda.")
        return

    print("CÓD".ljust(6) + "CLIENTE".ljust(26) + "TELEFONE".ljust(18) + "PONTOS")
    print("-" * 58)

    for cliente in banco.lista_clientes:
        codigo = str(cliente.codigo).ljust(6)
        nome = cliente.nome[:24].ljust(26)
        telefone = cliente.telefone.ljust(18)
        print(codigo + nome + telefone + str(cliente.pontos))

def cadastrar_cliente():
    mostrar_titulo("CADASTRAR NOVO CLIENTE")

    nome = ler_texto("Nome do cliente: ")
    telefone = ler_texto("Telefone: ")

    codigo = banco.gerar_codigo(banco.lista_clientes)
   
    cliente = Cliente(codigo, nome, telefone, 0)

    banco.lista_clientes.append(cliente)
    banco.salvar_clientes()

    print("")
    print("Cliente cadastrado com sucesso! Código " + str(codigo))
    pausar()

def listar_clientes():
    mostrar_titulo("CLIENTES CADASTRADOS")
    mostrar_tabela_clientes()
    pausar()

def consultar_pontos():
    mostrar_titulo("CONSULTAR PONTOS")
    mostrar_tabela_clientes()

    if len(banco.lista_clientes) == 0:
        pausar()
        return

    print("")
    codigo = ler_numero_int("Código do cliente: ")
    cliente = buscar_cliente(codigo)

    if cliente == None:
        print("Cliente não encontrado.")
        pausar()
        return

    print("")
    print("Cliente ..: " + cliente.nome)
    print("Telefone .: " + cliente.telefone)
    print("Pontos ...: " + str(cliente.pontos))

    if cliente.pontos >= PONTOS_PARA_BRINDE:
        print("")
        print("Este cliente já pode trocar os pontos por um brinde!")
    else:
        faltam = PONTOS_PARA_BRINDE - cliente.pontos
        print("Faltam " + str(faltam) + " pontos para ganhar um brinde.")

    pausar()

def trocar_pontos():
    mostrar_titulo("TROCAR PONTOS POR BRINDE")
    mostrar_tabela_clientes()

    if len(banco.lista_clientes) == 0:
        pausar()
        return

    print("")
    codigo = ler_numero_int("Código do cliente: ")
    cliente = buscar_cliente(codigo)

    if cliente == None:
        print("Cliente não encontrado.")
        pausar()
        return

    if cliente.pontos < PONTOS_PARA_BRINDE:
        print("")
        print(cliente.nome + " tem apenas " + str(cliente.pontos) + " pontos.")
        print("São necessários " + str(PONTOS_PARA_BRINDE) + " pontos.")
        pausar()
        return

    if confirmar("Trocar " + str(PONTOS_PARA_BRINDE) + " pontos por um café grátis?"):
        cliente.pontos = cliente.pontos - PONTOS_PARA_BRINDE
        banco.salvar_clientes()
        print("")
        print("Brinde liberado! Saldo agora: " + str(cliente.pontos) + " pontos.")
    else:
        print("Troca cancelada.")

    pausar()

def editar_cliente():
    mostrar_titulo("EDITAR CLIENTE")
    mostrar_tabela_clientes()

    if len(banco.lista_clientes) == 0:
        pausar()
        return

    print("")
    codigo = ler_numero_int("Código do cliente: ")
    cliente = buscar_cliente(codigo)

    if cliente == None:
        print("Cliente não encontrado.")
        pausar()
        return

    print("")
    print("Editando: " + cliente.nome)
    print("1 - Alterar o nome")
    print("2 - Alterar o telefone")
    print("")

    opcao = ler_numero_int("O que deseja alterar? ")

    if opcao == 1:
        cliente.nome = ler_texto("Novo nome: ")
    elif opcao == 2:
        cliente.telefone = ler_texto("Novo telefone: ")
    else:
        print("Opção inválida. Nada foi alterado.")
        pausar()
        return

    banco.salvar_clientes()
    print("Cliente atualizado!")
    pausar()

def excluir_cliente():
    mostrar_titulo("EXCLUIR CLIENTE")
    mostrar_tabela_clientes()

    if len(banco.lista_clientes) == 0:
        pausar()
        return

    print("")
    codigo = ler_numero_int("Código do cliente: ")
    cliente = buscar_cliente(codigo)

    if cliente == None:
        print("Cliente não encontrado.")
        pausar()
        return

    if confirmar("Tem certeza que quer excluir " + cliente.nome + "?"):
        banco.lista_clientes.remove(cliente)
        banco.salvar_clientes()
        print("Cliente excluído.")
    else:
        print("Nada foi excluído.")

    pausar()

def menu_clientes():
    opcao = -1

    while opcao != 0:
        mostrar_titulo("MENU DE CLIENTES")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Consultar pontos")
        print("4 - Trocar pontos por brinde")
        print("5 - Editar cliente")
        print("6 - Excluir cliente")
        print("0 - Voltar")
        print("")

        opcao = ler_numero_int("Escolha uma opção: ")

        if opcao == 1:
            cadastrar_cliente()
        elif opcao == 2:
            listar_clientes()
        elif opcao == 3:
            consultar_pontos()
        elif opcao == 4:
            trocar_pontos()
        elif opcao == 5:
            editar_cliente()
        elif opcao == 6:
            excluir_cliente()
        elif opcao != 0:
            print("Opção inválida.")
            pausar()
