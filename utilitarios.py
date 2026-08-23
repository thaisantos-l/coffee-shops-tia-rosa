import os

def limpar_tela(): 
    if os.name == "nt":
            os.system("cls")
    else:
          os.system("clear")

def pausar():
      input("\nPressione Enter para continuar")

def mostrar_titulo(titulo):
    limpar_tela()
    print("=" * 45)
    print(titulo)
    print("=" * 45)
    print("")

def ler_texto(mensagem):    
    texto = input(mensagem).strip()
    while texto == "":
        print("Você precisa digitar alguma coisa.")
        texto = input(mensagem).strip()
    return texto

def ler_numero_int(mensagem):
      while True:
            digitando = input(mensagem)
            try:
                  numero = int(digitando)
                  return numero
            except ValueError:
                  print("Digite apenas numeros, sem vigurla ou ponto")

def ler_preco(mensagem):
      while True:
            digitado = input(mensagem).replace(",",".")
            try:
                  preco = float(digitado)
            except ValueError:
                print("Digite um valor válido. Ex 5.80")
                continue

            if preco <= 0:
                  print("O preço precisa ser maior que 0 (zero)")
            else:
                  return preco

def confirmar(mensagem):
      resposta = input(mensagem + "(S/N:) ").strip().upper()
      if resposta == "S":
            return True
      else:
            return False

def formatar_dinheiro(valor):
      valor_formatado = "%.2f" % valor
      return "R$ " + valor_formatado.replace(".", ",")