import banco
from datetime import datetime
from modelos import Pedido
from produtos import buscar_produto, mostrar_tabela_produtos
from clientes import buscar_cliente, mostrar_tabela_clientes
from utilitarios import mostrar_titulo, pausar, ler_texto, ler_numero_int
from utilitarios import confirmar, formatar_dinheiro

def buscar_pedido(codigo):
    for pedido in banco.lista_pedidos:
        if pedido.codigo == codigo:
            return pedido

    return None

def escolher_cliente():
   
    if len(banco.lista_clientes) == 0:
        return None

    if confirmar("O cliente é cadastrado?") == False:
        return None

    print("")
    mostrar_tabela_clientes()
    print("")
    codigo = ler_numero_int("Código do cliente: ")
    cliente = buscar_cliente(codigo)

    if cliente == None:
        print("Cliente não encontrado. O pedido vai seguir sem cadastro.")
        pausar()

    return cliente

def mostrar_resumo(pedido):
    print("Pedido nº " + str(pedido.codigo))
    print("Cliente: " + pedido.nome_cliente)
    print("Data: " + pedido.data_hora)
    print("")
    print("QTD".ljust(6) + "PRODUTO".ljust(26) + "UNITÁRIO".ljust(14) + "SUBTOTAL")
    print("-" * 60)

    for item in pedido.itens:
        quantidade = str(item["quantidade"]).ljust(6)
        nome = item["nome"][:24].ljust(26)
        preco = formatar_dinheiro(item["preco"]).ljust(14)
        print(quantidade + nome + preco + formatar_dinheiro(item["subtotal"]))

    print("-" * 60)
    print("TOTAL: " + formatar_dinheiro(pedido.calcular_total()))

def novo_pedido():
    mostrar_titulo("NOVO PEDIDO")

    if len(banco.lista_produtos) == 0:
        print("Cadastre algum produto antes de registrar um pedido.")
        pausar()
        return

    cliente = escolher_cliente()

    if cliente == None:
        nome_cliente = ler_texto("Nome do cliente (ou Balcao): ")
    else:
        nome_cliente = cliente.nome

    codigo = banco.gerar_codigo(banco.lista_pedidos)
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
    pedido = Pedido(codigo, nome_cliente, data_hora)


    itens_lancados = []

    while True:
        mostrar_titulo("PEDIDO " + str(codigo) + " - " + nome_cliente)
        mostrar_tabela_produtos()
        print("")
        print("Digite 0 quando terminar o pedido.")
        codigo_produto = ler_numero_int("Código do produto: ")

        if codigo_produto == 0:
            break

        produto = buscar_produto(codigo_produto)

        if produto == None:
            print("Produto não encontrado.")
            pausar()
            continue

        quantidade = ler_numero_int("Quantidade: ")

        if quantidade <= 0:
            print("A quantidade precisa ser maior que zero.")
            pausar()
            continue

        if produto.tem_estoque(quantidade) == False:
            print("Estoque insuficiente. Temos apenas " + str(produto.estoque) + " unidades.")
            pausar()
            continue

        
        produto.baixar_estoque(quantidade)
        pedido.adicionar_item(produto, quantidade)
        itens_lancados.append({"produto": produto, "quantidade": quantidade})

        print("")
        print(str(quantidade) + "x " + produto.nome + " adicionado.")
        print("Total parcial: " + formatar_dinheiro(pedido.calcular_total()))
        pausar()

    if len(pedido.itens) == 0:
        print("")
        print("Nenhum item foi adicionado. Pedido cancelado.")
        pausar()
        return

    mostrar_titulo("FECHAMENTO DO PEDIDO")
    mostrar_resumo(pedido)
    print("")

    if confirmar("Confirma o pedido?") == False:
        
        for item in itens_lancados:
            produto_devolvido = item["produto"]
            produto_devolvido.estoque = produto_devolvido.estoque + item["quantidade"]

        print("Pedido cancelado. O estoque foi devolvido.")
        pausar()
        return

    banco.lista_pedidos.append(pedido)
    banco.salvar_pedidos()
    banco.salvar_produtos()

    total = pedido.calcular_total()

    print("")
    print("Pedido " + str(pedido.codigo) + " registrado com sucesso!")
    print("Valor a receber: " + formatar_dinheiro(total))

    
    if cliente != None:
        pontos_ganhos = cliente.ganhar_pontos(total)
        banco.salvar_clientes()
        print("")
        print(cliente.nome + " ganhou " + str(pontos_ganhos) + " pontos.")
        print("Saldo atual: " + str(cliente.pontos) + " pontos.")

    pausar()

def listar_pedidos():
    mostrar_titulo("PEDIDOS REGISTRADOS")

    if len(banco.lista_pedidos) == 0:
        print("Nenhum pedido registrado ainda.")
        pausar()
        return

    print("CÓD".ljust(6) + "DATA E HORA".ljust(20) + "CLIENTE".ljust(24) + "TOTAL")
    print("-" * 62)

    for pedido in banco.lista_pedidos:
        codigo = str(pedido.codigo).ljust(6)
        data = pedido.data_hora.ljust(20)
        nome = pedido.nome_cliente[:22].ljust(24)
        print(codigo + data + nome + formatar_dinheiro(pedido.calcular_total()))

    pausar()

def ver_detalhes_pedido():
    mostrar_titulo("DETALHES DO PEDIDO")

    if len(banco.lista_pedidos) == 0:
        print("Nenhum pedido registrado ainda.")
        pausar()
        return

    codigo = ler_numero_int("Código do pedido: ")
    pedido = buscar_pedido(codigo)

    if pedido == None:
        print("Pedido não encontrado.")
        pausar()
        return

    print("")
    mostrar_resumo(pedido)
    pausar()

def menu_pedidos():
    opcao = -1

    while opcao != 0:
        mostrar_titulo("MENU DE PEDIDOS")
        print("1 - Novo pedido")
        print("2 - Listar pedidos do dia")
        print("3 - Ver detalhes de um pedido")
        print("0 - Voltar")
        print("")

        opcao = ler_numero_int("Escolha uma opção: ")

        if opcao == 1:
            novo_pedido()
        elif opcao == 2:
            listar_pedidos()
        elif opcao == 3:
            ver_detalhes_pedido()
        elif opcao != 0:
            print("Opção inválida.")
            pausar()
