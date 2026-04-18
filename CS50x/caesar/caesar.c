#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    // Checa se tem apenas um argumento
    if (argc != 2)
    {
        printf("Erro: command-line argument errado, argumentos em excesso ou 0\n");
        return 1;
    }

    // Checa se valor do primeiro argumento é int
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int key = atoi(argv[1]);

    // checa wrap-around de 26
    if (key > 25)
    {
        int rounds = floor(key / 26);
        key = key - (26 * rounds);
    }
    // printf("%i\n", key);]

    string plainText = get_string("plaintext:  ");

    for (int i = 0; i < strlen(plainText); i++)
    {
        if (plainText[i] >= 'a' && plainText[i] <= 'z')
        {
            if (plainText[i] + key > 'z')
            {
                plainText[i] = plainText[i] + key - 26;
            }
            else
            {
                plainText[i] = plainText[i] + key;
            }
        }
        else if (plainText[i] >= 'A' && plainText[i] <= 'Z')
        {
            if (plainText[i] + key > 'Z')
            {
                plainText[i] = plainText[i] + key - 26;
            }
            else
            {
                plainText[i] = plainText[i] + key;
            }
        }
    }

    // logica aqui
    // string ciphertext = "";

    printf("ciphertext: %s\n", plainText);
}
