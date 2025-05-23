# Problem

João  está  prestes  a  completar  dois  anos  de  contrato  na  SAP  e  está  bem  feliz com  seu trabalho. Ele gosta tanto de trabalhar que acabou esquecendo de  marcar suas férias e, por isso, recebeu uma notificação da sua gestora que ele precisa fazer isso o quanto antes! Contudo,  João  só  pode  tirar  férias  se  a  data  de  início  e  fim  não  sobrepor  as  datas  de nenhum outro colega de trabalho.

Será que João vai conseguir tirar suas férias?

## Inputs

A  primeira  linha  de  entrada  consiste  em  um  inteiro  N  (0  <=  N  <= 104)  representando  a quantidade de colegas que já marcaram suas férias. Em seguida, seguem N linhas, cada uma contendo a data de início e de fim das férias do i-ésimo colega. A data é representada por uma string no formato dd-mm, onde dd é o dia e mm o mês. Considere que todas as datas fornecidas são válidas. A última linha consiste na data de início e de fim que João gostaria de tirar suas férias.

## Outputs

Seu programa deve imprimir uma única linha com a palavra “Sim”, caso João possa tirar férias ou “Nao”, caso contrário.

## Examples

| Exemplo de entrada 1  | Exemplo de saída 1    |
| --------------------- | --------------------- |
| 0                     | Sim                   |
| 10-10 17-10           |                       |

| Exemplo de entrada 2  | Exemplo de saída 2    |
| --------------------- | --------------------- |
| 1                     | Nao                   |
| 10-10 17-10           |                       |
| 17-10 28-10           |                       |

## Code

[Go to code](../codes/C.py)
