# Sistema de Vendas e Relatórios

Este é um sistema de linha de comando (CLI) simples, desenvolvido em Python, para gerenciar vendas, cadastrar produtos e vendedores, e gerar relatórios consolidados sobre o desempenho das vendas.

## Descrição

O projeto foi criado para simular o ambiente de vendas de uma pequena loja. Ele permite o cadastro dinâmico de produtos com códigos únicos, o registro de múltiplas vendas por diferentes vendedores e, ao final, a geração de um "dashboard" completo em um arquivo de texto (`.txt`) com as métricas essenciais de cada vendedor.

## Funcionalidades

- **Cadastro de Produtos:** Permite cadastrar múltiplos produtos no início da execução, gerando um código único para cada um.
- **Cadastro de Vendedores:** Cada venda é associada a um vendedor, que informa seu nome e percentual de comissão.
- **Múltiplas Vendas:** O sistema opera em um loop, permitindo que várias vendas sejam registradas em uma única sessão.
- **Carrinho de Compras:** Para cada venda, é possível adicionar múltiplos produtos, especificando valor e quantidade. O sistema calcula o subtotal e o total da compra.
- **Acumulação de Dados:** Todas as informações de vendas (valor total, unidades vendidas) são acumuladas para cada vendedor individualmente.
- **Geração de Relatório Final:** Ao final do dia de vendas, o sistema gera um relatório consolidado (`relatorio_vendas.txt`) com as seguintes métricas para cada vendedor:
    - Valor Total Vendido
    - Quantidade Total de Unidades Vendidas
    - Número de Vendas Realizadas
    - Ticket Médio por Venda
    - Percentual de Comissão
    - Valor Final da Comissão a Receber

## Fluxo de Execução

1.  **Cadastro de Produtos:** Ao iniciar, o sistema solicita o cadastro de todos os produtos que estarão disponíveis para venda durante a sessão.
2.  **Menu Principal:** Após o cadastro, um menu permite ao usuário escolher entre realizar uma `Venda` ou gerar o `Relatório`.
3.  **Realizar uma Venda:**
    * O nome e a comissão do vendedor são solicitados.
    * O catálogo de produtos é exibido.
    * O usuário adiciona produtos ao carrinho informando o código, o valor e a quantidade de cada um.
    * Ao final, um resumo da compra é exibido e o usuário confirma a finalização.
    * Os dados da venda são salvos e acumulados para aquele vendedor.
4.  **Gerar Relatório:**
    * Quando o usuário decide encerrar, ele escolhe a opção `Relatório`.
    * O sistema calcula as métricas finais para todos os vendedores que realizaram vendas.
    * Um relatório detalhado é exibido no terminal e também salvo no arquivo `relatorio_vendas.txt` na mesma pasta do script.
