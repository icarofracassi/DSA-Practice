#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;

    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int linha = 1; linha < height + 1; linha++)
    {
        for (int j = 0; j < height - linha; j++)
        {
            printf(" ");
        }

        for (int j = 0; j < linha; j++)
        {
            printf("#");
        }

        printf("  ");

        for (int j = 0; j < linha; j++)
        {
            printf("#");
        }

        printf("\n");
    }
}
