# Problem

Um Kit de Encolhimento de Polígonos é um material muito utilizado nas aulas de magia geométrica  na  Nlogônia.  O  kit  consiste  de  dois  pontos,  A  e  B  no  plano  cartesiano. Considere um polígono convexo dado pelos vértices 1, 2...N, nessa ordem. Para encolher esse  polígono  usando  o  kit,  algumas  regras  devem  ser  respeitadas.  Cada  vértice  x  do polígono  deve  ser  movido  uma  vez  só:  para  o  ponto  médio  do  segmento  Ax  ou  para  o ponto  médio  do  segmento  Bx.  A  operação  de  encolhimento  deve  produzir  um  novo polígono  convexo  que  preserve  a  ordem  relativa  dos  vértices  do  polígono  original.  Em outras palavras, considerando todas as possíveis maneiras de aplicar o kit, apenas aquelas cuja sequência final dos vértices 1, 2...N representa um polígono convexo são válidas. Veja que  o  polígono  convexo  original  pode  estar  em  sentido  horário  e  uma  operação  de encolhimento válida produzir um polígono convexo em sentido anti-horário, na mesma ordem dos vértices. Apenas a ordem relativa dos pontos é importante, não o sentido. E sabido que magia geométrica não é o forte da maioria dos alunos. A professora pediu que eles usassem o kit de encolhimento para encolher um polígono convexo fornecido por ela de forma a obter a menor área possível e um amigo seu implorou para que você resolva a questão por ele. Responda a menor área possível do polígono para ele.

Considerando  um  uso  válido  do  kit,  onde  o  polígono  sombreado  é  o  de  menor área possível que preserva a sequência dos vértices. Os pontos A e B correspondem aos pontos do kit. Note que, apesar do nome encolhimento, às vezes é possível utilizar o kit para  aumentar  a  área  dos  polígonos!  Como  geometria  é  difícil!  Observe  que  um  único ponto  ou  uma  reta  não  são  considerados  polígonos.  Sendo  assim,  se  um  uso  do  kit produzir  como  resultado  algo  diferente  de  um  polígono  convexo,  esse  não  é  um  uso válido.

## Inputs

A primeira linha da entrada contém um inteiro N (3  N  105), o número de vértices do polígono. Seguem N linhas, cada uma com dois inteiros x, y (-106  x, y  106), os vértices do polígono. A última linha da entrada contém quatro inteiros, Ax, Ay, Bx e By (-106  Ax, Ay, Bx, By  106), as coordenadas x e y de A e as coordenadas x e y de B, respectivamente. Os pontos da entrada serão dados na ordem correta em que aparecem no polígono, no sentido horário ou anti-horário. Não haverá pontos repetidos e o polígono será convexo.

## Outputs

Seu programa deve produzir uma linha, contendo um número real, com 3 casas decimais de precisão, representando a menor área possível para um polígono obtido com o uso do kit.

## Examples

| Exemplo de entrada 1  | Exemplo de saída 1    |
| --------------------- | --------------------- |
| 3                     | 3.500                 |
| 20 6                  |                       |
| 4 8                   |                       |
| 2 6                   |                       |
| 0 0 4 0               |                       |

| Exemplo de entrada 2  | Exemplo de saída 2    |
| --------------------- | --------------------- |
| 3                     | 1.000                 |
| 0 4                   |                       |
| 4 4                   |                       |
| 0 0                   |                       |
| 3  -2  -3  -2         |                       |

| Exemplo de entrada 3  | Exemplo de saída 3    |
| --------------------- | --------------------- |
| 3                     | 2.000                 |
| 0 4                   |                       |
| 4 4                   |                       |
| 0 0                   |                       |
| 2  -2  -2  -2         |                       |

## Code

[Go to code](../codes/W.py)
