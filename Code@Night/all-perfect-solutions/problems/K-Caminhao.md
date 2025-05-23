# Problem

A  Sociedade  de  Balões  Coloridos  (SBC)  é  a  principal  fornecedora  de  balões  para competições de programação; ela dispõe de grandes fábricas e depósitos, além de uma extensa  frota  de  caminhões  para  garantir  a  alegria  dos  competidores.  Há  várias  sedes regionais na Nlogônia, todas as quais contrataram a SBC para o fornecimento de balões para  a  prova.  A  Nlogônia  é  um  arquipélago  ligado  por  várias  pontes.  Cada  ilha  do arquipélago pode conter várias sedes regionais e vários depósitos da SBC. Ao planejar as rotas,  a  SBC  se  deparou  com  um  problema:  por  razões  de  segurança,  cada  ponte  da Nlogônia tem um limite máximo de peso permitido para os veículos que trafegam sobre ela. Devido ao grande número de pontes na Nlogônia, e ao elevado peso da mercadoria transportada, o diretor de operações da SBC pediu que você escrevesse um programa que determina o maior peso bruto que pode ser transportado entre os depósitos e os locais de prova.

## Inputs

A primeira linha contém três inteiros N, M e S, indicando, respectivamente, o número de ilhas da Nlogônia, o número de pontes que ligam as ilhas e o número de sedes. As ilhas nlogonianas  são  numeradas  de  1  a  N.  Cada  uma  das  M  linhas  seguintes  descreve  uma ponte. A descrição de cada ponte consiste de uma linha contendo três inteiros A, B e P, indicando  as  duas  ilhas  ligadas  por  aquela  ponte  e  o  peso  máximo  permitido  naquela ponte, em toneladas. Todas as pontes são de mão dupla; cada par de ilhas é ligado por no máximo  uma  ponte;  é  possível  ir  de  qualquer  ilha  para  qualquer  outra  ilha  utilizando apenas as pontes do arquipélago (mas pode ser preciso passar por outras ilhas primeiro). Cada uma das S linhas seguintes descreve uma sede. A descrição de cada sede consiste de uma linha contendo dois inteiros A e B, indicando, respectivamente, a ilha onde está a sede e a ilha onde está o depósito que irá fornecer os balões àquela sede.

RESTRIÇÕES

- 2 ≤ N ≤ 2 × 104
- 1 ≤ M ≤ 105
- 1 ≤ S ≤ 5 × 104
- 1 ≤ A, B ≤ N, A != B
- 0 ≤ P ≤ 105

## Outputs

Para cada sede, na ordem em que elas foram descritas  na entrada, seu programa deve imprimir  uma  linha  contendo  um  único  inteiro,  indicando  o  maior  peso  bruto,  em toneladas,  que  pode  ser  transportado  por  caminhão  do  depósito  que  irá  fornecer  os balões até ela.

## Examples

| Exemplo de entrada 1  | Exemplo de saída 1    |
| --------------------- | --------------------- |
| 4 5 4                 | 7                     |
| 1 2 9                 | 9                     |
| 1 3 0                 | 8                     |
| 2 3 8                 | 7                     |
| 2 4 7                 |                       |
| 3 4 4                 |                       |
| 1 4                   |                       |
| 2 1                   |                       |
| 3 1                   |                       |
| 4 3                   |                       |

| Exemplo de entrada 2  | Exemplo de saída 2    |
| --------------------- | --------------------- |
| 4 5 2                 | 20                    |
| 1 2 30                | 40                    |
| 2 3 20                |                       |
| 3 4 10                |                       |
| 4 1 40                |                       |
| 2 4 50                |                       |
| 1 3                   |                       |
| 1 2                   |                       |

## Code

[Go to code](../codes/K.py)
