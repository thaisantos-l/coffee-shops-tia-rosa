import banco
from modelos import Produto
from utilitarios import mostrar_titulo, pausar, ler_texto, ler_numero_int
from utilitarios import ler_preco, confirmar, formatar_dinheiro

def buscar_produto(codigo):
   
    for produto in banco.lista_produtos:
        if produto.codigo == codigo:
            return produto

   
    return None

def mostrar_tabela_produtos():
    if len(banco.lista_produtos) == 0:
        print("Nenhum produto cadastrado ainda.")
        return

    print("CÓD".ljust(6) + "PRODUTO".ljust(24) + "CATEGORIA".ljust(17)
          + "PREÇO".ljust(13) + "ESTOQUE")
    print("-" * 68)

    for produto in banco.lista_produtos:
        codigo = str(produto.codigo).ljust(6)
        
        nome = produto.nome[:22].ljust(24)
        categoria = produto.categoria[:15].ljust(17)
        preco = formatar_dinheiro(produto.preco).ljust(13)
        print(codigo + nome + categoria + preco + str(produto.estoque))

def cadastrar_produto():
    mostrar_titulo("CADASTRAR NOVO PRODUTO")

    nome = ler_texto("Nome do produto: ")
    categoria = ler_texto("Categoria (Bebida, Doce, Salgado): ")
    preco = ler_preco("Preço em reais: ")
    descricao = ler_texto("Descrição / ingredientes: ")
    estoque = ler_numero_int("Quantidade em estoque: ")

    codigo = banco.gerar_codigo(banco.lista_produtos)
    produto = Produto(codigo, nome, categoria, preco, descricao, estoque)

    banco.lista_produtos.append(produto)
    banco.salvar_produtos()

    print("")
    print("Produto cadastrado com sucesso! Código " + str(codigo))
    pausar()

def listar_produtos():
    mostrar_titulo("CARDÁPIO - PRODUTOS CADASTRADOS")
    mostrar_tabela_produtos()
    pausar()

def ver_detalhes():
    mostrar_titulo("DETALHES DO PRODUTO")
    mostrar_tabela_produtos()

    if len(banco.lista_produtos) == 0:
        pausar()
        return

    print("")
    codigo = ler_numero_int("Código do produto: ")
    produto = buscar_produto(codigo)

    if produto == None:
        print("Produto não encontrado.")
        pausar()
        return

    print("")
    print("Nome ......: " + produto.nome)
    print("Categoria .: " + produto.categoria)
    print("Preço .....: " + formatar_dinheiro(produto.preco))
    print("Ingredientes: " + produto.descricao)
    print("Estoque ...: " + str(produto.estoque) + " unidades")
    pausar()

def editar_produto():
    mostrar_titulo("EDITAR PRODUTO")
    mostrar_tabela_produtos()

    if len(banco.lista_produtos) == 0:
        pausar()
        return

    print("")
    codigo = ler_numero_int("Código do produto que quer editar: ")
    produto = buscar_produto(codigo)

    if produto == None:
        print("Produto não encontrado.")
        pausar()
        return

    print("")
    print("Editando: " + produto.nome)
    print("1 - Alterar o nome")
    print("2 - Alterar o preço")
    print("3 - Alterar a descrição")
    print("")

    opcao = ler_numero_int("O que deseja alterar? ")

    if opcao == 1:
        produto.nome = ler_texto("Novo nome: ")
    elif opcao == 2:
        produto.preco = ler_preco("Novo preço: ")
    elif opcao == 3:
        produto.descricao = ler_texto("Nova descrição: ")
    else:
        print("Opção inválida. Nada foi alterado.")
        pausar()
        return

    banco.salvar_produtos()
    print("Produto atualizado!")
    pausar()

def repor_estoque():
    mostrar_titulo("REPOR ESTOQUE")
    mostrar_tabela_produtos()

    if len(banco.lista_produtos) == 0:
        pausar()
        return

    print("")
    codigo = ler_numero_int("Código do produto: ")
    produto = buscar_produto(codigo)

    if produto == None:
        print("Produto não encontrado.")
        pausar()
        return

    quantidade = ler_numero_int("Quantas unidades chegaram? ")

    if quantidade <= 0:
        print("A quantidade precisa ser maior que zero.")
        pausar()
        return

    produto.estoque = produto.estoque + quantidade
    banco.salvar_produtos()

    print("")
    print("Estoque de " + produto.nome + " agora é " + str(produto.estoque))
    pausar()

def excluir_produto():
    mostrar_titulo("EXCLUIR PRODUTO")
    mostrar_tabela_produtos()

    if len(banco.lista_produtos) == 0:
        pausar()
        return

    print("")
    codigo = ler_numero_int("Código do produto: ")
    produto = buscar_produto(codigo)

    if produto == None:
        print("Produto não encontrado.")
        pausar()
        return

    if confirmar("Tem certeza que quer excluir " + produto.nome + "?"):
        banco.lista_produtos.remove(produto)
        banco.salvar_produtos()
        print("Produto excluído.")
    else:
        print("Nada foi excluído.")

    pausar()

def menu_produtos():
    opcao = -1

    while opcao != 0:
        mostrar_titulo("MENU DE PRODUTOS")
        print("1 - Cadastrar produto")
        print("2 - Ver cardápio")
        print("3 - Ver detalhes de um produto")
        print("4 - Editar produto")
        print("5 - Repor estoque")
        print("6 - Excluir produto")
        print("0 - Voltar")
        print("")

        opcao = ler_numero_int("Escolha uma opção: ")

        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            ver_detalhes()
        elif opcao == 4:
            editar_produto()
        elif opcao == 5:
            repor_estoque()
        elif opcao == 6:
            excluir_produto()
        elif opcao != 0:
            print("Opção inválida.")
            pausar()
