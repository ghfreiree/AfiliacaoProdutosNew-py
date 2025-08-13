'''
- Criar códigos para produtos
- Identificá-los pelos códigos
- Efetuar uma compra pelo código
- Dar um valor total dos itens
- Relatório com vendedor, total vendido, ticket médio por vendedor, produtos por venda
- Criar um arquivo .txt para colocar o relatório
'''

from random import randint


def cadastro_vendedor():
    print('BEM-VINDO AO SISTEMA DE VENDEDOR DA LOJA\n')
    print('Cadastro:')
    nome = input('Digite o nome do vendedor: ').upper()
    comissao = (float(input('Digite a comissão do vendedor (em %): ')))/100
    print(f'Vendedor {nome} cadastrado com sucesso, bem-vindo(a) à nossa loja!\n')
    return nome, comissao


def gera_codigo():
    '''
    - Retorna uma lista o nome do produto seguido do seu código gerado.
    '''
    produtos_codigos = []
    produtos = []
    while True:
        produto = (input('Digite o nome do produto que deseja cadastrar: ')).upper()
        produtos.append(produto)
        while True:
            continuar = (input('Deseja cadastrar outro produto? (s/n): ')).lower()
            if continuar == 'n':
                break
            elif continuar == 's':
                break
            else:
                print('Opção inválida. Tente novamente.')
        if continuar == 'n':
            break
    
    for i in range(len(produtos)):
        produtos_codigos.append(produtos[i])
        produtos_codigos.append(produtos[i][0] + str(randint(0, 999)))
    return produtos_codigos

def mostrar_produtos(lista_codigos):
    '''
    - Exibe os produtos e seus códigos.
    '''
    j = 1
    print('\nCATÁLOGO DE PRODUTOS CADASTRADOS\n')
    for i in range(0, len(lista_codigos), 2):
        print(f'Produto {j}: {lista_codigos[i]} - Código: {lista_codigos[i + 1]}')
        j += 1

def identifica_produto(lista_codigos):
    '''
    - Identifica o produto pelo código.
    - Retorna o nome do produto.
    '''
    produto = ''
    while True:
        cod = input('\nDigite o código do produto que será comprado: ')
        for i in range(len(lista_codigos)):
            if cod == lista_codigos[i]:
                produto = lista_codigos[i - 1]
                print(f'Produto encontrado: {produto}')
                break
        if produto != '':
            break
        else:
            print('Código inválido. Tente novamente.')
    return produto

def infos_produto(produto):
    '''
    - Pede o valor e a quantidade do produto.
    - Retorna uma lista com o nome do produto, valor e quantidade, respectivamente.
    '''
    produto_vl_qtd = []
    produto_vl_qtd.append(produto)
    valor = int(input(f'\nDigite o valor do(a) {produto}: '))
    produto_vl_qtd.append(valor)
    quantidade = int(input('Digite quantas unidades serão compradas: '))
    produto_vl_qtd.append(quantidade)
    return produto_vl_qtd

def carrinho_compras(nome, info):
    '''
    - Retorna o total da compra e a quantidade de produtos.'''
    print('\n===========================================================\n')
    print('CARRINHO DE COMPRAS\n')
    lista_valores = []
    lista_unidades = []
    i = 1
    for nome, valor, quantidade in info:
        print(f'Produto {i}: {nome} - Valor: R${valor} - Quantidade: {quantidade} - Subtotal: R${valor*quantidade}')
        lista_valores.append(valor*quantidade)
        lista_unidades.append(quantidade)
        i+=1
    total_valores = sum(lista_valores)
    total_unidades = sum(lista_unidades)
    print(f'\nTotal da compra: R${total_valores}')
    print('\n===========================================================')
    return nome, total_valores, total_unidades




def montar_carrinho():
    while True:
        nome_comissao = cadastro_vendedor() # Tupla (nome do vendedor, comissão do vendedor)
        produtos_codigos = gera_codigo() # Lista [nome do produto, código do produto, nome do produto 2, código do produto 2, ...]
        mostrar_produtos(produtos_codigos) # Exibe os produtos cadastrados
        infos_produtos = [] # Lista de listas [[nome do produto, valor, quantidade], ...]

        while True:
            produto = identifica_produto(produtos_codigos) # Nome do produto
            infos = infos_produto(produto) # Lista [nome do produto, valor, quantidade]
            infos_produtos.append(infos)
            while True:
                continuar = (input('\nDeseja adicionar mais produtos ao carrinho? (s/n): ')).lower()
                if continuar == 'n':
                    break
                elif continuar == 's':
                    break
                else:
                    print('Opção inválida. Tente novamente.')
            if continuar == 'n':
                break
        infos_venda = carrinho_compras(nome_comissao[0], infos_produtos) # Tupla (nome do vendedor, valor total da venda, unidades vendidas)
        while True:
            confirmacao = (input('\nDeseja finalizar a compra? (s/n): ')).lower()
            if confirmacao == 's':
                print('\nCompra finalizada com sucesso!')
                break
            elif confirmacao == 'n':
                print('\nCompra cancelada.')
                break
            else:
                print('\nOpção inválida. Tente novamente.')
        if confirmacao == 's':
            break
    return infos_venda, nome_comissao[0]
