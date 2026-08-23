import banco
import produtos
import clientes
import pedidos
import relatorios
from utilitarios import mostrar_titulo, pausar, ler_numero_int, limpar_tela

def mostrar_boas_vindas():
    limpar_tela()
    print("=" * 45)
    print("         COFFEE SHOPS TIA ROSA")
    print("      Sistema de Gerenciamento 1.0")
    print("=" * 45)
    print("")
    print("Dados carregados:")
    print("Produtos no cardápio : " + str(len(banco.lista_produtos)))
    print("Clientes cadastrados : " + str(len(banco.lista_clientes)))
    print("Pedidos registrados  : " + str(len(banco.lista_pedidos)))
    pausar()

def encerrar_sistema():
  
    banco.salvar_produtos()
    banco.salvar_clientes()
    banco.salvar_pedidos()

    limpar_tela()
    print("=" * 45)
    print("   Dados salvos com sucesso.")
    print("   Obrigado por usar o sistema!")
    print("         COFFEE SHOPS TIA ROSA")
    print("=" * 45)
    print("")

def menu_principal():
    opcao = -1

    while opcao != 0:
        mostrar_titulo("MENU PRINCIPAL - COFFEE SHOPS TIA ROSA")
        print("1 - Produtos e estoque")
        print("2 - Clientes e fidelidade")
        print("3 - Pedidos")
        print("4 - Relatórios")
        print("0 - Sair do sistema")
        print("")

        opcao = ler_numero_int("Escolha uma opção: ")

        if opcao == 1:
            produtos.menu_produtos()
        elif opcao == 2:
            clientes.menu_clientes()
        elif opcao == 3:
            pedidos.menu_pedidos()
        elif opcao == 4:
            relatorios.menu_relatorios()
        elif opcao == 0:
            encerrar_sistema()
        else:
            print("Opção inválida. Digite um número de 0 a 4.")
            pausar()


if __name__ == "__main__":
    banco.carregar_tudo()
    mostrar_boas_vindas()
    menu_principal()
