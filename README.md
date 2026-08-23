# Coffee Shops Tia Rosa - Sistema de Gerenciamento

Sistema de gerenciamento desenvolvido em Python para a cafeteria Coffee Shops Tia Rosa,
com interface de linha de comando (terminal).

Trabalho academico da disciplina de  Lógica- Algoritmos e Programação de Computadores.
Curso: Análise e Desenvolvimento de Sistemas
Aluna: Thaís de Lima Santos

## Sobre o projeto

A cafeteria Coffee Shops Tia Rosa fazia todo o controle no papel, o que gerava confusao
nos horarios de pico, dificuldade para saber o que tinha em estoque e nenhum controle
das vendas do dia. Alem disso, os clientes tinham duvidas sobre os ingredientes e a
cafeteria nao tinha nenhuma forma de fidelizar quem voltava sempre.

Este sistema resolve esses pontos com quatro modulos: produtos, clientes, pedidos e
relatorios. Como a equipe da cafeteria tem pouca familiaridade com tecnologia, todas as
telas funcionam por menus numerados e o sistema avisa quando algo esta errado em vez de
simplesmente fechar.

## Funcionalidades

### Produtos e estoque
- Cadastrar produto com nome, categoria, preco, descricao dos ingredientes e estoque
- Ver o cardapio completo em formato de tabela
- Consultar os detalhes e ingredientes de um produto
- Editar nome, preco ou descricao
- Repor estoque quando chega mercadoria
- Excluir produto

### Clientes e fidelidade
- Cadastrar cliente com nome e telefone
- Listar os clientes com o saldo de pontos
- Consultar quantos pontos faltam para o brinde
- Trocar pontos por brinde
- Editar e excluir cliente

### Pedidos
- Montar pedido item por item, para cliente cadastrado ou venda de balcao
- Calculo automatico do subtotal de cada item e do total do pedido
- Baixa automatica no estoque
- Bloqueio da venda quando nao ha estoque suficiente
- Devolucao do estoque caso o pedido seja cancelado no fechamento
- Credito automatico dos pontos de fidelidade
- Consulta dos pedidos ja registrados

### Relatorios
- Vendas do dia com faturamento e ticket medio
- Resumo geral da cafeteria
- Ranking dos produtos mais vendidos
- Alerta dos produtos com estoque baixo

## Tecnologias utilizadas

- Python 3
- Bibliotecas da propria linguagem: json, os e datetime
- Nao e necessario instalar nenhuma biblioteca externa

## Estrutura dos arquivos

```
coffee-shops-tia-rosa/
├── main.py            menu principal, e o arquivo que deve ser executado
├── produtos.py        telas do cardapio e do estoque
├── clientes.py        cadastro de clientes e programa de pontos
├── pedidos.py         registro dos pedidos
├── relatorios.py      relatorios gerenciais
├── modelos.py         classes Produto, Cliente e Pedido
├── banco.py           listas de dados e leitura/gravacao dos arquivos JSON
├── utilitarios.py     funcoes usadas por todos os modulos
├── dados/             arquivos JSON com os dados salvos
│   ├── produtos.json
│   ├── clientes.json
│   └── pedidos.json
├── imagens/           prints do sistema em funcionamento
└── README.md
```

Cada arquivo cuida de um assunto so. Assim, para mexer no calculo do pedido basta abrir
o pedidos.py, sem precisar procurar em um arquivo unico e gigante.

## Como executar

1. Instale o Python 3 (https://www.python.org/downloads/)
2. Baixe ou clone este repositorio:

3. Abra o terminal dentro da pasta do projeto
4. Execute:

```
python main.py
```

Importante: o comando precisa ser executado de dentro da pasta do projeto, porque o
caminho da pasta dados e relativo.

## Como usar

Ao abrir, o sistema mostra quantos produtos, clientes e pedidos foram carregados e
apresenta o menu principal:

```
1 - Produtos e estoque
2 - Clientes e fidelidade
3 - Pedidos
4 - Relatorios
0 - Sair do sistema
```

Basta digitar o numero da opcao e pressionar Enter. Dentro de cada modulo, a opcao 0
volta para o menu anterior.

Para registrar uma venda: opcao 3, depois opcao 1, informe se o cliente e cadastrado,
digite o codigo do produto e a quantidade quantas vezes for preciso e digite 0 para
fechar. O sistema mostra o resumo e pede confirmacao antes de gravar.

## Regras de negocio

- Cada R$ 1,00 gasto vale 1 ponto de fidelidade (apenas para clientes cadastrados)
- 100 pontos podem ser trocados por um brinde
- Produtos com 15 unidades ou menos aparecem no alerta de reposicao
- Nao e possivel vender uma quantidade maior do que a disponivel em estoque
- O codigo de cada produto, cliente e pedido e gerado automaticamente

## Onde os dados ficam salvos

Os dados sao gravados em arquivos JSON dentro da pasta dados. Isso faz com que as
informacoes continuem salvas depois de fechar o programa. Os arquivos sao regravados a
cada cadastro, edicao ou venda, entao nada se perde se o computador desligar.

Exemplo de um produto gravado:

```json
{
    "codigo": 3,
    "nome": "Cappuccino",
    "categoria": "Bebida",
    "preco": 9.5,
    "descricao": "Espresso, leite vaporizado, canela e chocolate em po",
    "estoque": 28
}
```

## Telas do sistema

Os prints do sistema em funcionamento estao na pasta imagens.

| Arquivo | Tela |
|---|---|
| 01-tela-inicial.png | Abertura do sistema |
| 03-cardapio.png | Cardapio completo |
| 08-resumo-pedido.png | Fechamento do pedido |
| 09-comprovante-pedido.png | Pedido registrado e pontos creditados |
| 10-vendas-do-dia.png | Relatorio de vendas do dia |
| 13-validacao-estoque.png | Validacao de estoque insuficiente |

