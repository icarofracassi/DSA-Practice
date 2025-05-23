# Problem

Juliano é fã do programa de auditório Apagando e Ganhando, um programa no qual os participantes são selecionados através de um sorteio e recebem prêmios em dinheiro por participarem.  No  programa,  o  apresentador  escreve  um  número  de  N dígitos  em  uma lousa.  O  participante  então  deve  apagar  exatamente  D dígitos  do  número  que  está  na lousa; o número formado pelos dígitos que restaram é então o prêmio do participante. Juliano  finalmente  foi  selecionado  para  participar  do  programa,  e  pediu  que  você escrevesse um programa que, dados o número que o apresentador escreveu na lousa, e quantos dígitos Juliano tem que apagar, determina o valor do maior prêmio que Juliano pode ganhar.

## Inputs

A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém dois inteiros N e D (1 ≤ D < N ≤ 105), indicando a quantidade de dígitos do número que o apresentador escreveu na lousa e quantos dígitos devem ser apagados. A linha seguinte contém o número escrito pelo apresentador, que não contém zeros à esquerda. O final da entrada é  indicado por uma linha que contém apenas  dois  zeros, separados  por um espaço em branco.

## Outputs

Para cada caso de teste da entrada seu programa deve imprimir uma única linha na saída, contendo o maior prêmio que Juliano pode ganhar.

## Examples

| Exemplo de entrada 1  | Exemplo de saída 1    |
| --------------------- | --------------------- |
| 4 2                   | 79                    |
| 759                   | 323                   |
| 6 3                   | 100                   |
| 123123                |                       |
| 7 4                   |                       |
| 1000000               |                       |
| 0 0                   |                       |

| Exemplo de entrada 2  | Exemplo de saída 2    |
| --------------------- | --------------------- |

## Code

[Go to code](../codes/H.py)
