# Problem

Um investidor principiante deseja aprender a investir na bolsa de valores. Como ele não tem  experiência,  selecionou  uma  única  empresa,  e  acompanhou  os  valores  diários  das ações  dessa  empresa,  durante  N  dias.  Ficou  curioso  quanto  teria  ganhado  se  tivesse investido  nesse  período  em  que  acompanhou  os  valores.  Na  verdade,  o  investidor  é milionário e tem muito dinheiro, suficiente para comprar qualquer quantidade de ações da empresa. Entretanto, como é um investidor cuidadoso, decidiu que nunca teria mais do  que  uma  ação  da  empresa.  Como  sempre  há  intermediários,  a  corretora  de  valores cobra uma taxa fixa de C reais a cada compra de uma ação da empresa. Você deve calcular qual o lucro máximo que o investidor poderia ter auferido, investindo durante alguns dos N dias, podendo inclusive decidir não investir.

## Inputs

A primeira linha contém dois inteiros, N e C (1 ≤ N ≤ 2 × 105 e 0 ≤ C ≤ 30). A segunda linha contém as N cotações P1, P2, . . . ,PN, dos dias 1, 2, . . . , N, respectivamente. Cada cotação Pi satisfaz as desigualdades 1 ≤ Pi ≤ 1000.

## Outputs

Seu  programa  deve  produzir  uma  única  linha  com  um  inteiro  representando  o  lucro máximo do investidor, em reais.

## Examples

| Exemplo de entrada 1                      | Exemplo de saída 1    |
| ----------------------------------------- | --------------------- |
| 6 10                                      | 20                    |
| 100 120 130 80 50 40                      |                       |

| Exemplo de entrada 2                      | Exemplo de saída 2    |
| ----------------------------------------- | --------------------- |
| 5 10                                      | 0                     |
| 70 80 50 40 50                            |                       |

| Exemplo de entrada 2                      | Exemplo de saída 2    |
| ----------------------------------------- | --------------------- |
| 13 30                                     | 220                   |
| 10 80 20 40 30 50 40 60 50 70 60 10 200   |                       |

## Code

[Go to code](../codes/V.py)
