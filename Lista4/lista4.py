from prettytable import PrettyTable

# 1)
# Implemente um algoritmo utilizando programação dinâmica para o seguinte problema.
# Considere que tubulações são vendidas em pedaços de tamanho inteiro. Os
# fabricantes produzem tubulações longas e os comércios cortam em pedaços para
# vender. Problema: dada uma tubulação de tamanho n e a tabela de preços pi, qual a
# melhor forma de cortar para maximizar o preço de venda total? Quais são as
# eficiências de tempo e espaço do seu algoritmo?

# Eficiências de tempo do algoritmo: O(nˆ2)
# Complexidade de espaço do algoritmo: O(nˆ2) + O(n)

# Menor valor inteiro
INT_MIN = -32767


# Retorna o melhor preço e a melhor combinação de cortes para cada tamanho da tubulação
def cortar_tubulacao(price, n):
    val = [0 for x in range(n + 1)]
    val_combination = [[0] for x in range(n + 1)]
    val[0] = 0

    for i in range(1, n + 1):
        max_val = INT_MIN
        for j in range(i):
            val_max = max(max_val, price[j] + val[i - j - 1])
            if val_max > max_val:
                max_val = val_max
                val_combination[i] = [*val_combination[i - j - 1], j + 1]
        val[i] = max_val

    return [val, val_combination]


# Criar a tabela para plotar os valores encontrados
def make_table(tamanho, valor_por_tamanho, valor_max, combinacao):
    table = PrettyTable()
    table.add_column("Tamanho", tamanho)
    table.add_column("Valor por tamanho", valor_por_tamanho)
    table.add_column("Valor Máximo", valor_max)
    table.add_column("Combinacao", combinacao)
    return table


array = [1, 5, 8, 9, 10, 17, 19, 21, 26]
# array = [1, 3, 4, 7, 9, 10, 10, 11, 11, 11, 35]
size = len(array)
array_preco_maximo, array_combinacao_valor = cortar_tubulacao(array, size)
array_de_tamanho = [i for i in range(size + 1)]
print(make_table(array_de_tamanho, [0, *array], array_preco_maximo, array_combinacao_valor))
