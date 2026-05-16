produtos = []
quantidade = []
preco = []


print ("Esse é um sistema de gerenciamento de estoque\n")

def opcao_invalida():
   print ("Opção invalida!\n")
   input ("Digite uma tecla para voltar para as opções: ")


def mercadoria():
    produtos_cadastrados = input ("Cadastrar produtos do estoque:")
    quantidade_de_produtos = int(input ("Quantidade de produtos no estoque:"))
    preco_dos_produtos = float(input("Digite o preço do produto que deseja cadastrar: "))

    if quantidade_de_produtos > 0:
      print ("temos", quantidade_de_produtos, "unidades de", produtos_cadastrados, "no estoque")
      produtos.append (produtos_cadastrados)
      quantidade.append (quantidade_de_produtos)
      preco.append(preco_dos_produtos)
      print ("Produtos: ", produtos)
      print ("Quantidade:", quantidade, "\n")

    else:
     opcao_invalida()
 
def cadastrar_novos_produtos():
    print("Novos produtos\n")
    while True:
     novo_produto = input ("Você deseja colocar mais produtos?\n 1.\nSim\n 2.\n Não\n Digite uma das opções:")
     if novo_produto == "1":
       novo_produto_cadastrado = input ("Digite o nome do novo produto cadastrado: ")
       quantidade_novo_produto = int(input("Digite a quantidade desse produto: "))
       preco_novo_produto = float (input("Digite o preço do produto que deseja cadastrar: "))
       
       if quantidade_novo_produto <=0:
           print ("Numero de produtos inválidos para vendas!")
       else:
           produtos.append(novo_produto_cadastrado)
           quantidade.append (quantidade_novo_produto)
           preco.append(preco_novo_produto)
           print ("Produto Cadastrado com Sucesso!")
           print ("Sua lista de produtos:\n", produtos, "\n")

       continuar  = input ("Deseja cadastrar mais novos produtos?\n 1.sim \n 2.não")  
       if continuar ==  "2":
        print ("sem produtos a cadastrar!")
        break
       elif continuar != "1":
        opcao_invalida()

     elif novo_produto =="2":
      break
     else:
       opcao_invalida()

     
     
     
    return produtos

def quero_ver_meus_produtos():
 querver = input ("deseja ver os produtos que você cadastrou?\n 1.sim \n 2.não")
 if querver == "sim" or "Sim":
   print ("Aqui estão seus produtos: ", produtos)
 

 

  





mercadoria()
cadastrar_novos_produtos()
quero_ver_meus_produtos()
