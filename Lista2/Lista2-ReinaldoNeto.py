## P.A.A
## Reinaldo Candido dos Santos Neto

## 1) Implemente um programa que, dado um conjunto C de n inteiros e outro inteiro I,
## determinar os pares de inteiros de C cuja subtração é exatamente igual a I. Em
## seguida, analise a complexidade do algoritmo proposto. O seu programa deve
## basear-se na estratégia de força bruta.


conjunto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
i = 3


def arraySubtract(conjunto, i):
    res = []
    for c in range(len(conjunto)):
        for t in range(len(conjunto)):
            if c != t and conjunto[c] - conjunto[t] == i:
                res.append([conjunto[c], conjunto[t]])
    print(res)


arraySubtract(conjunto, i)

## esta função tem complexidade O(nˆ2)


########################################################################################################################
## 2) Você recebe uma matriz booleana A [0..n - 1, 0..n - 1], onde n> 3, que deverá ser a
## matriz de adjacência de um grafo que representa uma rede com uma dessas
## topologias. Sua tarefa é determinar qual dessas três topologias, se houver, a matriz
## representa. O programa de retornar mensagem “Outra topologia” para matrizes que
## não apresentam nenhum dos três tipos. Implemente um programa baseado em força
## bruta para esta tarefa e indique sua classe de eficiência de tempo.


redeMalh = [
    [0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0]
]
redeEstr = [
    [1, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0]
]
redeAnel = [
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0]
]


## Ordenar dois números em ordem crescente
def sortTwoNumbers(n1, n2):  # 2
    if n1 < n2:  # 1
        return [n1, n2]  # 1
    else:
        return [n2, n1]  # 1


## Esta função tem complexidade 2nˆ2 + n^2 = 3n^2 -> O(n^2)
def isRedeAnel(rede):
    array_result = []
    for i in range(len(rede)):  # a complexidade desse for é `n` para o for * ( `n` do count + `n` do index) = 2(nˆ2)
        array = rede[i]
        if array.count(1) == 2:  # O(n) para o count
            index = array.index(1)  # O(n) para o index
            index_upper = index + 2
            index_lower = index - 2
            if index_lower < 0:
                last_index = len(array) + index_lower
            sortIndex = sortTwoNumbers(i, index)
            array_result.append(sortIndex)

            if index_upper < len(array) and array[index_upper] == 1:
                sortIntern = sortTwoNumbers(i, index_upper)
                array_result.append(sortIntern)

            elif index_upper < len(array) and array[index_lower] == 1:
                sortIntern = sortTwoNumbers(i, last_index)
                array_result.append(sortIntern)

            elif index_upper > len(array) and array[index_lower] == 1:
                sortIntern = sortTwoNumbers(i, last_index)
                array_result.append(sortIntern)
            else:
                return False
        else:
            return False

    for it in range(len(array_result)):  # a complexidade do for é n * n = nˆ2 = O(n^2)
        if array_result.count(array_result[it]) != 2:  # O(n) devido o count
            return False

    return True


def isRedeMalha(rede):  # O(nˆ2)
    array_result = []
    for i in range(len(rede)):  # a complexidade do for é n * n = n^2
        array = rede[i]
        if array.count(1) == len(array) - 1:  # O(n) devido o count
            array_result.append(array.index(0))
        else:
            return False

    for it in range(len(array_result)):
        if array_result.count(array_result[it]) != 1:
            return False
    return True


def isRedeEstrela(rede):  # O(nˆ2)
    index_mid = None
    array_satellite = []
    for i in range(len(rede)):  # O(n)
        array = rede[i]
        count = array.count(1)  # O(n)
        if count == 1:
            index = array.index(1)
            array_satellite.append(index)
        elif count == len(array) - 1 and index_mid is None:
            index_mid = array.index(0)
        else:
            return False

    if array_satellite.count(index_mid) == len(array_satellite):  # O(n)
        return True
    return False


def checkGrid(rede):
    if isRedeEstrela(rede):
        return 'Rede em Estrela'
    elif isRedeAnel(rede):
        return 'Rede em Anel'
    elif isRedeMalha(rede):
        return 'Rede em Malha'
    else:
        return 'Outra topologia'


print(checkGrid(redeEstr))
