## P.A.A
## Reinaldo Candido dos Santos Neto

## 1) Implemente um programa que, dado um conjunto C de n inteiros e outro inteiro I,
## determinar os pares de inteiros de C cuja subtração é exatamente igual a I. Em
## seguida, analise a complexidade do algoritmo proposto. O seu programa deve
## basear-se na estratégia de força bruta.


conjunto = [1, 2, 3, 4, 5, 6]
i = 2
res = []

for c in range(len(conjunto)):
    for t in range(len(conjunto)):
        if c != t and conjunto[c] - conjunto[t] == i:
            res.append([conjunto[c], conjunto[t]])
print(res)

## esta função tem complexidade O(nˆ2)