# Problem

Frustrado  e  desanimado  com  os  resultados  de  sua  equipe  de  futebol,  o  Super Brasileiro  Clube (SBC)  resolveu  investir  na  equipe  de  handebol.  Para  melhor  avaliar  os  atletas,  os  técnicos identificaram  que  seria  útil  analisar  a  regularidade  dos  jogadores.  Especificamente,  eles  estão interessados em saber quantos jogadores fizeram gols em todas as partidas. Como o volume de dados  é  muito  grande,  eles  gostariam  de  ter  um  programa  de  computador  para  realizar  essa contagem.

## Inputs

A primeira linha da entrada contém dois inteiros N e M (1 ≤ N ≤ 100 e 1 ≤ M ≤ 100), indicando respectivamente o número de jogadores e o número de partidas. Cada uma das N linhas seguintes descreve o desempenho de um jogador: a i-ésima linha contém M inteiros Xj (0 ≤ Xj ≤ 100, para 1 ≤ j ≤ M), informando o número de gols do i-ésimo jogador em cada partida.

## Outputs

Seu programa deve produzir uma única linha, contendo um único inteiro, o número de jogadores que fizeram gols em todas as partidas.

## Examples

| Exemplo de entrada 1  | Exemplo de saída 1    |
| --------------------- | --------------------- |
| 5 3                   | 0                     |
| 0 0 0                 |                       |
| 1 0 5                 |                       |
| 0 0 0                 |                       |
| 0 1 2                 |                       |
| 1 1 0                 |                       |

| Exemplo de entrada 2  | Exemplo de saída 2    |
| --------------------- | --------------------- |
| 12 5                  | 2                     |
| 4 4 2 3 7             |                       |
| 0 0 0 1 0             |                       |
| 7 4 7 0 6             |                       |
| 1 2 3 3 2             |                       |
| 0 0 0 0 0             |                       |
| 4 0 9 10 10           |                       |
| 0 1 0 0 0             |                       |
| 1 2 0 2 3             |                       |
| 10 10 10 1 0          |                       |
| 0 3 3 3 4             |                       |
| 10 10 0 10 10         |                       |
| 1 1 2 0 9             |                       |

## Code

[Go to code](../codes/Q.py)
