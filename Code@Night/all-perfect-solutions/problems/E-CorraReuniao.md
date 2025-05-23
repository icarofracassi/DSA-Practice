# Problem

João  mora  em  Viamão  e  todo  dia  útil  precisa  acordar  bem  cedo  para  pegar  o SAP  Bus. Geralmente, ele chega no horário previsto, bem a tempo de participar da primeira reunião do  dia.  Como  alguns  trechos  da  BR  estão  em  obra,  em  alguns  dias  ele  se  atrasa.  Para chegar até o seu local de trabalho, João precisa fazer uma boa caminhada pelo Labs, além de pegar um elevador, visto que seu time trabalha no último andar do prédio.

Não  bastasse  estar  atrasado,  em  um  dia  desses,  o  elevador  estava  com  defeito  e  João precisou  subir  as  escadas.  Do  térreo  até  o  último  andar,  é  necessário  subir  N  degraus. Além disso, cada degrau infringe um cansaço Ci, sendo i o i-ésimo degrau da escadaria. João  pode  subir  1  ou  2  degraus  de  uma  só  vez,  podendo  começar  tanto  no  degrau  0 quanto no degrau 1. Sua tarefa é minimizar o cansaço de João para que ele não chegue suado na reunião.

## Inputs

A primeira linha de entrada consiste em um inteiro N (2 <= N <= 1000), representando o número de degraus. Na linha seguinte, seguem N inteiros Ci (0 <= Ci <= 999 e 1 <= i <= N), separados por espaço, representando o cansaço atribuído ao degrau Ci.

## Outputs

A saída consiste em uma única linha contendo um único inteiro, representando o mínimo de cansaço necessário para subir todos os degraus.

## Examples

| Exemplo de entrada 1  | Exemplo de saída 1    |
| --------------------- | --------------------- |
| 3                     | 15                    |
| 10 15 20              |                       |

| Exemplo de entrada 2      | Exemplo de saída 2    |
| ------------------------- | --------------------- |
| 10                        | 6                     |
| 1 100 1 1 1 100 1 1 100 1 |                       |

## Code

[Go to code](../codes/E.py)
