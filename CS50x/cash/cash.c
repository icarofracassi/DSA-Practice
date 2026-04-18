#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int troco;
    do
    {
        troco = get_int("Change owed: ");
    }
    while (troco < 0);

    // moedas = [25, 10, 5, 1]
    int qtdmoedas = 0;
    while (troco >= 25)
    {
        troco -= 25;
        qtdmoedas += 1;
    }
    while (troco >= 10)
    {
        troco -= 10;
        qtdmoedas += 1;
    }
    while (troco >= 5)
    {
        troco -= 5;
        qtdmoedas += 1;
    }
    while (troco >= 1)
    {
        troco -= 1;
        qtdmoedas += 1;
    }

    printf("%i\n", qtdmoedas);
}
