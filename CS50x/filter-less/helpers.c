#include "helpers.h"
#include <math.h>

int min(int a, int b);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Take average of red, green, and blue
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;

            float average = (red + green + blue) / 3.0;
            average = round(average);
            // Update pixel values
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}
// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Take original values of red, green, and blue
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;

            float sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue;
            float sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue;
            float sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue;

            sepiaRed = round(sepiaRed);
            sepiaGreen = round(sepiaGreen);
            sepiaBlue = round(sepiaBlue);

            sepiaRed = min(sepiaRed, 255);
            sepiaGreen = min(sepiaGreen, 255);
            sepiaBlue = min(sepiaBlue, 255);

            // Update pixel values
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over half horizontal pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // Swap pixels
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a copy of image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float redTotalBlur = 0;
            float greenTotalBlur = 0;
            float blueTotalBlur = 0;
            int countNeighboor = 0;

            int k = 0;
            int l = 0;

            for (k = -1; k < 2; k++)
            {

                for (l = -1; l < 2; l++)
                {

                    if (i + k < 0 || i + k > height - 1)
                    {
                        continue;
                    }

                    if (j + l < 0 || j + l > width - 1)
                    {
                        continue;
                    }

                    redTotalBlur += copy[i + k][j + l].rgbtRed;
                    greenTotalBlur += copy[i + k][j + l].rgbtGreen;
                    blueTotalBlur += copy[i + k][j + l].rgbtBlue;
                    countNeighboor++;
                }
            }

            image[i][j].rgbtRed = round(redTotalBlur / countNeighboor);
            image[i][j].rgbtGreen = round(greenTotalBlur / countNeighboor);
            image[i][j].rgbtBlue = round(blueTotalBlur / countNeighboor);
        }
    }

    return;
}

int min(int a, int b)
{
    if (a > b)
    {
        return b;
    }
    return a;
}


