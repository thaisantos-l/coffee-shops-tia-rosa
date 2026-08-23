class Produto: 
    def __init__(self, codigo, nome, categoria, preco, descricao, estoque):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.descricao = descricao
        self.estoque = estoque

    def tem_estoque(self, quantidade):
        if self.estoque >= quantidade:
            return True
        else:
            return False

    def baixar_estoque(self, quantidade):
        self.estoque = self.estoque - quantidade

    def virar_dicionario(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "categoria": self.categoria,
            "preco": self.preco,
            "descricao": self.descricao,
            "estoque": self.estoque
        }


class Cliente:

    def __init__(self, codigo, nome, telefone, pontos):
        self.codigo = codigo
        self.nome = nome
        self.telefone = telefone
        self.pontos = pontos

    def ganhar_pontos(self, valor_do_pedido):

        pontos_ganho = int(valor_do_pedido)
        self.pontos = self.pontos + pontos_ganho
        return pontos_ganho


    def virar_dicionario(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "telefone": self.telefone,
            "pontos": self.pontos
        }



class Pedido:

    def __init__(self, codigo, nome_cliente, data_hora):
        self.codigo = codigo
        self.nome_cliente = nome_cliente
        self.data_hora = data_hora
        # lista com um dicionário para cada produto que entrou no pedido
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        item = {
            "nome": produto.nome,
            "quantidade": quantidade,
            "preco": produto.preco,
            "subtotal": produto.preco * quantidade
        }
        self.itens.append(item)

    def calcular_total(self):
        total = 0
        for item in self.itens:
            total = total + item["subtotal"]
        return total

    def virar_dicionario(self):
        return {
            "codigo": self.codigo,
            "nome_cliente": self.nome_cliente,
            "data_hora": self.data_hora,
            "itens": self.itens,
            "total": self.calcular_total()
        }