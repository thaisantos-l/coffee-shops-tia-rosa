import banco
from datetime import datetime
from utilitarios import mostrar_titulo, pausar, ler_numero_int, formatar_dinheiro

LIMITE_ESTOQUE_BAIXO = 15

def data_de_hoje():
    return datetime.now().strftime("%d/%m/%Y")

def vendas_do_dia():
    hoje = data_de_hoje()
    mostrar_titulo("VENDAS DO DIA - " + hoje)

    pedidos_de_hoje = []
    total_do_dia = 0

    for pedido in banco.lista_pedidos:
       
        if pedido.data_hora[:10] == hoje:
            pedidos_de_hoje.append(pedido)
            total_do_dia = total_do_dia + pedido.calcular_total()

    if len(pedidos_de_hoje) == 0:
        print("Nenhum pedido foi registrado hoje.")
        pausar()
        return

    print("CÓD".ljust(6) + "HORA".ljust(10) + "CLIENTE".ljust(26) + "TOTAL")
    print("-" * 58)

    for pedido in pedidos_de_hoje:
        codigo = str(pedido.codigo).ljust(6)
        # do caractere 11 em diante fica só a hora
        hora = pedido.data_hora[11:].ljust(10)
        nome = pedido.nome_cliente[:24].ljust(26)
        print(codigo + hora + nome + formatar_dinheiro(pedido.calcular_total()))

    ticket_medio = total_do_dia / len(pedidos_de_hoje)

    print("-" * 58)
    print("Pedidos no dia ..: " + str(len(pedidos_de_hoje)))
    print("Faturamento .....: " + formatar_dinheiro(total_do_dia))
    print("Ticket médio ....: " + formatar_dinheiro(ticket_medio))
    pausar()

def resumo_geral():
    mostrar_titulo("RESUMO GERAL DA CAFETERIA")

    if len(banco.lista_pedidos) == 0:
        print("Nenhum pedido registrado ainda.")
        pausar()
        return

    faturamento = 0
    itens_vendidos = 0

    for pedido in banco.lista_pedidos:
        faturamento = faturamento + pedido.calcular_total()
        for item in pedido.itens:
            itens_vendidos = itens_vendidos + item["quantidade"]

    ticket_medio = faturamento / len(banco.lista_pedidos)

    print("Pedidos registrados .: " + str(len(banco.lista_pedidos)))
    print("Itens vendidos ......: " + str(itens_vendidos))
    print("Faturamento total ...: " + formatar_dinheiro(faturamento))
    print("Ticket médio ........: " + formatar_dinheiro(ticket_medio))
    print("")
    print("Clientes cadastrados : " + str(len(banco.lista_clientes)))
    print("Produtos no cardápio : " + str(len(banco.lista_produtos)))
    pausar()

def produtos_mais_vendidos():
    mostrar_titulo("PRODUTOS MAIS VENDIDOS")

    if len(banco.lista_pedidos) == 0:
        print("Nenhum pedido registrado ainda.")
        pausar()
        return

   
    contagem = {}

    for pedido in banco.lista_pedidos:
        for item in pedido.itens:
            nome = item["nome"]
            if nome in contagem:
                contagem[nome]["quantidade"] = contagem[nome]["quantidade"] + item["quantidade"]
                contagem[nome]["valor"] = contagem[nome]["valor"] + item["subtotal"]
            else:
                contagem[nome] = {"quantidade": item["quantidade"], "valor": item["subtotal"]}

    print("PRODUTO".ljust(26) + "QUANTIDADE".ljust(14) + "VALOR VENDIDO")
    print("-" * 55)

   
    while len(contagem) > 0:
        nome_do_maior = ""
        maior_quantidade = -1

        for nome in contagem:
            if contagem[nome]["quantidade"] > maior_quantidade:
                maior_quantidade = contagem[nome]["quantidade"]
                nome_do_maior = nome

        valor_vendido = contagem[nome_do_maior]["valor"]
        print(nome_do_maior[:24].ljust(26) + str(maior_quantidade).ljust(14)
              + formatar_dinheiro(valor_vendido))

    
        del contagem[nome_do_maior]

    pausar()

def estoque_baixo():
    mostrar_titulo("PRODUTOS COM ESTOQUE BAIXO")

    if len(banco.lista_produtos) == 0:
        print("Nenhum produto cadastrado ainda.")
        pausar()
        return

    encontrou = False

    print("PRODUTO".ljust(26) + "CATEGORIA".ljust(17) + "ESTOQUE")
    print("-" * 52)

    for produto in banco.lista_produtos:
        if produto.estoque <= LIMITE_ESTOQUE_BAIXO:
            nome = produto.nome[:24].ljust(26)
            categoria = produto.categoria[:15].ljust(17)
            print(nome + categoria + str(produto.estoque))
            encontrou = True

    if encontrou == False:
        print("Nenhum produto abaixo do limite.")

    print("")
    print("Produtos com " + str(LIMITE_ESTOQUE_BAIXO) + " unidades ou menos precisam de reposição.")
    pausar()

def menu_relatorios():
    opcao = -1

    while opcao != 0:
        mostrar_titulo("MENU DE RELATÓRIOS")
        print("1 - Vendas do dia")
        print("2 - Resumo geral da cafeteria")
        print("3 - Produtos mais vendidos")
        print("4 - Produtos com estoque baixo")
        print("0 - Voltar")
        print("")

        opcao = ler_numero_int("Escolha uma opção: ")

        if opcao == 1:
            vendas_do_dia()
        elif opcao == 2:
            resumo_geral()
        elif opcao == 3:
            produtos_mais_vendidos()
        elif opcao == 4:
            estoque_baixo()
        elif opcao != 0:
            print("Opção inválida.")
            pausar()
