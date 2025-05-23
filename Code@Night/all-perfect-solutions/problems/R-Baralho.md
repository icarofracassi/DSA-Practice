# Problem

Um baralho contém um número par 2n de cartas a1, a2, . . . , a2n, todas distintas (a1 < a2 < · · · < a2n). O baralho encontra-se perfeitamente ordenado, ou seja, a primeira carta é a1, a segunda carta é a2, e assim por diante, até a última carta, que é a2n. Um croupier então executa repetidamente um procedimento de embaralhar, que consiste em dois passos: 1. o baralho  é  dividido ao meio; 2. as cartas  das duas  metades são então intercaladas, de maneira que se a sequência de cartas do baralho no início do passo 1 é x1, x2, . . . , x2n, então ao final do passo 2 a sequência de cartas se torna xn+1, x1, xn+2, x2, . . . , x2n, xn. Dado o  número  de  cartas  do  baralho,  escreva  um  programa  que  determine  quantas  vezes  o procedimento de embaralhar descrito acima deve ser repetido de forma que o baralho volte a ficar ordenado.

## Inputs

A única linha da entrada contém um inteiro par P (2 ≤ P ≤ 2 × 105), indicando o número de cartas do baralho (note que o valor P corresponde ao valor 2n na descrição acima).

## Outputs

Seu  programa  deve  produzir  uma  única  linha  contendo  um  único  inteiro,  o  número mínimo  de  vezes  que  o  processo  de  embaralhamento  deve  ser  repetido  para  que  o baralho fique novamente ordenado.

## Examples

| Exemplo de entrada 1  | Exemplo de saída 1    |
| --------------------- | --------------------- |
| 4                     | 4                     |

| Exemplo de entrada 2  | Exemplo de saída 2    |
| --------------------- | --------------------- |
| 6                     | 3                     |

| Exemplo de entrada 3  | Exemplo de saída 3    |
| --------------------- | --------------------- |
| 2                     | 2                     |

| Exemplo de entrada 4  | Exemplo de saída 4    |
| --------------------- | --------------------- |
| 100002                | 100002                |

## Code

[Go to code](../codes/R.py)
