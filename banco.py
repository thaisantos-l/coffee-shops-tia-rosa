import json
import os
from modelos import Produto, Cliente, Pedido

PASTA_DADOS = "dados"


lista_produtos = []
lista_clientes = []
lista_pedidos = []


def caminho_do_arquivo(nome_arquivo):
    return os.path.join(PASTA_DADOS, nome_arquivo)


def criar_pasta_dados():
   
    if not os.path.exists(PASTA_DADOS):
        os.mkdir(PASTA_DADOS)


def salvar_lista(nome_arquivo, lista):
    
    dados = []
    for item in lista:
        dados.append(item.virar_dicionario())

    criar_pasta_dados()
    arquivo = open(caminho_do_arquivo(nome_arquivo), "w", encoding="utf-8")
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()


def ler_lista(nome_arquivo):
    caminho = caminho_do_arquivo(nome_arquivo)

   
    if not os.path.exists(caminho):
        return []

    arquivo = open(caminho, "r", encoding="utf-8")
    dados = json.load(arquivo)
    arquivo.close()
    return dados


def salvar_produtos():
    salvar_lista("produtos.json", lista_produtos)


def salvar_clientes():
    salvar_lista("clientes.json", lista_clientes)


def salvar_pedidos():
    salvar_lista("pedidos.json", lista_pedidos)


def carregar_produtos():
    dados_salvos = ler_lista("produtos.json")
    for dados in dados_salvos:
        produto = Produto(dados["codigo"], dados["nome"], dados["categoria"],
                          dados["preco"], dados["descricao"], dados["estoque"])
        lista_produtos.append(produto)


def carregar_clientes():
    dados_salvos = ler_lista("clientes.json")
    for dados in dados_salvos:
        cliente = Cliente(dados["codigo"], dados["nome"],
                          dados["telefone"], dados["pontos"])
        lista_clientes.append(cliente)


def carregar_pedidos():
    dados_salvos = ler_lista("pedidos.json")
    for dados in dados_salvos:
        pedido = Pedido(dados["codigo"], dados["nome_cliente"], dados["data_hora"])
        pedido.itens = dados["itens"]
        lista_pedidos.append(pedido)


def carregar_tudo():
   
    carregar_produtos()
    carregar_clientes()
    carregar_pedidos()


def gerar_codigo(lista):
  
    if len(lista) == 0:
        return 1

    maior_codigo = 0
    for item in lista:
        if item.codigo > maior_codigo:
            maior_codigo = item.codigo

    return maior_codigo + 1
