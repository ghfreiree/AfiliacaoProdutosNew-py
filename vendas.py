from random import randint
import os

def cadastro_vendedor():
    """Cadastra um novo vendedor e sua comissão."""
    print('\n--- CADASTRO / LOGIN DO VENDEDOR ---')
    nome = input('Digite o nome do vendedor: ').upper()
    comissao = (float(input(f'Digite a comissão de {nome} (em %): ')))/100
    print(f'Vendedor {nome} pronto para a venda!\n')
    return nome, comissao


def gera_codigo():
    """
    - Cadastra os produtos que estarão disponíveis para venda.
    - Retorna uma lista no formato [produto1, codigo1, produto2, codigo2, ...].
    """
    produtos_codigos = []
    produtos = []
    print('--- CADASTRO INICIAL DE PRODUTOS ---\n')
    while True:
        produto = (input('Digite o nome do produto que deseja cadastrar: ')).upper()
        # Garante que o código gerado seja único
        while True:
            codigo_gerado = produto[:3] + str(randint(0, 999))
            if codigo_gerado not in produtos_codigos:
                produtos.append(produto)
                produtos_codigos.append(produto)
                produtos_codigos.append(codigo_gerado)
                break
        
        while True:
            continuar = (input('Deseja cadastrar outro produto? (s/n): ')).lower()
            if continuar in ['s', 'n']:
                break
            else:
                print('Opção inválida. Tente novamente.')
        if continuar == 'n':
            break
    return produtos_codigos


def mostrar_produtos(lista_codigos):
    """Exibe os produtos e seus códigos de forma organizada."""
    j = 1
    print('\n--- CATÁLOGO DE PRODUTOS ---')
    for i in range(0, len(lista_codigos), 2):
        print(f'{j}. Produto: {lista_codigos[i]} - Código: {lista_codigos[i + 1]}')
        j += 1
    print('----------------------------\n')


def identifica_produto(lista_codigos):
    """
    - Identifica o produto pelo código.
    - Retorna o nome do produto.
    """
    produto_encontrado = ''
    while True:
        cod = input('Digite o código do produto que será comprado: ')
        # Itera pela lista de códigos (que estão nos índices ímpares)
        for i in range(1, len(lista_codigos), 2):
            if cod == lista_codigos[i]:
                produto_encontrado = lista_codigos[i - 1]
                print(f'--> Produto encontrado: {produto_encontrado}')
                break
        if produto_encontrado != '':
            break
        else:
            print('Código inválido. Tente novamente.')
    return produto_encontrado


def infos_produto(produto):
    """
    - Pede o valor e a quantidade do produto.
    - Retorna uma lista com [nome, valor, quantidade].
    """
    produto_vl_qtd = []
    produto_vl_qtd.append(produto)
    while True:
        try:
            valor = float(input(f'Digite o valor do(a) {produto}: R$'))
            quantidade = int(input(f'Digite quantas unidades de {produto} serão compradas: '))
            produto_vl_qtd.append(valor)
            produto_vl_qtd.append(quantidade)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para valor e quantidade.")
    return produto_vl_qtd


def carrinho_compras(info_produtos):
    """
    - Mostra os itens do carrinho e calcula o total da compra e a quantidade de produtos.
    - Retorna uma tupla (total_da_compra, total_de_unidades).
    """
    print('\n===========================================================\n')
    print('          CARRINHO DE COMPRAS (Resumo da Venda)          \n')
    lista_valores = []
    lista_unidades = []
    i = 1
    # CORREÇÃO: A variável 'nome' foi trocada para 'nome_produto' para não sobrescrever
    # a variável com o nome do vendedor que pode ser usada fora da função.
    for nome_produto, valor, quantidade in info_produtos:
        subtotal = valor * quantidade
        print(f'{i}. Produto: {nome_produto} - Valor: R${valor:.2f} - Qtd: {quantidade} - Subtotal: R${subtotal:.2f}')
        lista_valores.append(subtotal)
        lista_unidades.append(quantidade)
        i += 1
    total_valores = sum(lista_valores)
    total_unidades = sum(lista_unidades)
    print(f'\nTotal da compra: R${total_valores:.2f}')
    print(f'Total de unidades: {total_unidades}')
    print('\n===========================================================')
    return total_valores, total_unidades


def realizar_venda(produtos_cadastrados):
    """
    - Orquestra uma única transação de venda completa.
    - Retorna uma tupla com (nome_vendedor, comissao, total_vendido, unidades_vendidas).
    """
    nome_vendedor, comissao_vendedor = cadastro_vendedor()
    mostrar_produtos(produtos_cadastrados)
    
    infos_produtos_carrinho = [] # Lista de listas [[produto, valor, qtd], ...]
    while True:
        produto = identifica_produto(produtos_cadastrados)
        infos = infos_produto(produto)
        infos_produtos_carrinho.append(infos)
        
        while True:
            continuar = (input('\nDeseja adicionar mais produtos ao carrinho? (s/n): ')).lower()
            if continuar in ['s', 'n']:
                break
            else:
                print('Opção inválida. Tente novamente.')
        if continuar == 'n':
            break

    total_venda, unidades_venda = carrinho_compras(infos_produtos_carrinho)
    
    while True:
        confirmacao = (input('\nDeseja finalizar a compra? (s/n): ')).lower()
        if confirmacao == 's':
            print('\nCompra finalizada com sucesso!')
            return nome_vendedor, comissao_vendedor, total_venda, unidades_venda
        elif confirmacao == 'n':
            print('\nCompra cancelada. Nenhum dado será salvo.')
            return None # Retorna None para indicar que a venda foi cancelada
        else:
            print('\nOpção inválida. Tente novamente.')


def gerar_relatorio_final(dados_vendedores):
    """
    - Calcula as métricas finais para cada vendedor.
    - Imprime o dashboard no console.
    - Salva o dashboard em um arquivo 'relatorio_vendas.txt'.
    """
    print("\n\n||" + "="*50 + "||")
    print("||" + "RELATÓRIO FINAL DE VENDAS".center(50) + "||")
    print("||" + "="*50 + "||\n")

    relatorio_texto = "RELATÓRIO FINAL DE VENDAS\n" + "="*30 + "\n\n"

    for vendedor, dados in dados_vendedores.items():
        total_vendido = dados['total_vendido']
        total_unidades = dados['total_unidades']
        numero_vendas = dados['numero_vendas']
        comissao_percentual = dados['comissao_percentual']

        # Evita divisão por zero caso um vendedor não tenha vendas
        ticket_medio = total_vendido / numero_vendas if numero_vendas > 0 else 0
        valor_comissao = total_vendido * comissao_percentual

        # Monta a string para o console e para o arquivo
        bloco_vendedor = (
            f"VENDEDOR(A): {vendedor}\n"
            f"-----------------------------------------\n"
            f"  - Valor Total Vendido: R$ {total_vendido:.2f}\n"
            f"  - Unidades Vendidas: {total_unidades} unid.\n"
            f"  - Número de Vendas Realizadas: {numero_vendas}\n"
            f"  - Ticket Médio por Venda: R$ {ticket_medio:.2f}\n"
            f"  - Comissão: {comissao_percentual:.2%}\n"
            f"  - Valor a Receber de Comissão: R$ {valor_comissao:.2f}\n"
            f"-----------------------------------------\n\n"
        )
        print(bloco_vendedor)
        relatorio_texto += bloco_vendedor

    # Salva o relatório em um arquivo .txt
    try:
        with open('relatorio_vendas.txt', 'w', encoding='utf-8') as f:
            f.write(relatorio_texto)
        print(f"\nRelatório também foi salvo em: {os.path.abspath('relatorio_vendas.txt')}")
    except IOError as e:
        print(f"\nErro ao salvar o arquivo de relatório: {e}")


def main():
    """Função principal que gerencia o sistema de vendas."""
    
    # Estrutura para acumular os dados:
    # { 'NOME_VENDEDOR': {'total_vendido': X, 'total_unidades': Y, ...}, ...}
    dados_vendedores = {}

    print('BEM-VINDO AO SISTEMA DE VENDAS DA LOJA')
    
    # Passo 1: Cadastrar todos os produtos.
    produtos_cadastrados = gera_codigo()
    if not produtos_cadastrados:
        print("Nenhum produto cadastrado. Encerrando o sistema.")
        return

    # Passo 2: Loop principal para realizar múltiplas vendas ou gerar um relatório delas.
    while True:
        print("\n--- MENU PRINCIPAL ---")
        acao = input("Digite 'V' para iniciar uma nova VENDA ou 'R' para gerar o RELATÓRIO final: ").upper()

        if acao == 'V':
            resultado_venda = realizar_venda(produtos_cadastrados)
            
            # Se a venda não foi cancelada, processa os dados
            if resultado_venda:
                vendedor, comissao, total, unidades = resultado_venda
                
                # Se é a primeira venda do vendedor, inicializa seus dados
                if vendedor not in dados_vendedores:
                    dados_vendedores[vendedor] = {
                        'total_vendido': 0,
                        'total_unidades': 0,
                        'numero_vendas': 0,
                        'comissao_percentual': comissao
                    }
                
                # Acumula os dados da venda recém-realizada
                dados_vendedores[vendedor]['total_vendido'] += total
                dados_vendedores[vendedor]['total_unidades'] += unidades
                dados_vendedores[vendedor]['numero_vendas'] += 1

        elif acao == 'R':
            if not dados_vendedores:
                print("\nNenhuma venda foi realizada. Não há relatório para gerar.")
            else:
                gerar_relatorio_final(dados_vendedores)
            print("\nEncerrando o sistema. Obrigado!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

main()
