# Problem

Hoje  o  seu  time  de  trabalho  na  SAP  decidiu  fazer  a  reunião  da  daily  de  uma  forma diferente!  Os  membros  do  time  estão  espalhados  pelo  labs,  cada  um  em  um  local diferente, e vocês decidiram que a daily vai ser feita a partir dos coffee-corners!

Para isso, cada membro do time irá se deslocar até o seu coffee-corner mais próximo e participar da reunião remotamente. Além disso, foi combinado que o primeiro membro a chegar  em  um  coffee-corner  será  o  que  vai  compartilhar  a  tela  do  seu  notebook  e conduzir a daily.

Dadas  as  coordenadas  (x, y) dos  membros  do time e dos  coffee-corners, a  sua tarefa é descobrir qual é este membro que chegará primeiro em um coffee-corner. Cada pessoa consegue mover-se somente nas quatro direções (para cima, para baixo, para a esquerda, para a direita), uma unidade de cada vez. Cada membro do time irá mover-se no menor caminho  possível  até  o  coffee-corner  mais  próximo  de  si,  sendo  que  todos  iniciam  a caminhada ao mesmo tempo, e caminham na mesma velocidade. É garantido que sempre há um único membro do time que chegará primeiro a um coffee-corner.

## Inputs

A primeira linha da entrada contém dois inteiros, N (1 ≤ N ≤ 103) e M (1 ≤ M ≤ 103), sendo a  quantidade  de  membros  do  time  e  de  coffee-corners,  respectivamente.  As  N  linhas seguintes contêm dois inteiros cada, Ax e Ay (0 ≤ Ax , Ay ≤ 105), as coordenadas do i-ésimo membro. As M linhas seguintes também contêm dois inteiros cada, Bx ≥ 0 e By ≥ 0 (0 ≤ Bx , By ≤ 105), as coordenadas do i-ésimo coffee-corner.

## Outputs

Seu programa deve imprimir uma única linha contendo um número inteiro, indicando o membro do time que chegará primeiro a um coffe-corner.

## Examples

| Exemplo de entrada 1  | Exemplo de saída 1    |
| --------------------- | --------------------- |
| 3 2                   | 1                     |
| 1 1                   |                       |
| 5 1                   |                       |
| 10 3                  |                       |
| 2 2                   |                       |
| 5 8                   |                       |

| Exemplo de entrada 2  | Exemplo de saída 2    |
| --------------------- | --------------------- |
| 1 1                   | 1                     |
| 0 3                   |                       |
| 0 0                   |                       |

## Code

[Go to code](../codes/F.py)
