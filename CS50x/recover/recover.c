#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");

    // Create a buffer for a block of data
    uint8_t buffer[512];
    char *jpegFileName = malloc(sizeof(char)*8);

    int imgCounter = 0;

    FILE *outputFile = NULL;

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        //look for beginning of a JPEG, start is "0xff 0xd8 0xff 0xe"
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] >= 0xe0 && buffer[3] <= 0xef))
        {
            if (outputFile != NULL)
            {
                fclose(outputFile);
            }

            // name the file
            sprintf(jpegFileName, "%03i.jpg", imgCounter);

            outputFile = fopen(jpegFileName, "w");


            if (outputFile == NULL)
            {
                printf("Cannot open file: %s\n", jpegFileName);
                return 2;
            }

            fwrite(buffer, 1, 512, outputFile);

            imgCounter++;

        }
        else
        {
            if(imgCounter > 0)
            {
                fwrite(buffer, 1, 512, outputFile);
            }
        }

    }

    fclose(card);
    fclose(outputFile);

    free(jpegFileName);

}
