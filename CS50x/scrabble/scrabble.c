#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int alfValues[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int computePoints(string word);

int main(void)
{
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Compute the score of each word
    int points1 = computePoints(word1);
    int points2 = computePoints(word2);

    if (points1 > points2)
    {
        printf("Player 1 wins!\n");
    }
    else if (points1 < points2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int computePoints(string word)
{
    int points = 0;
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        if (word[i] >= 'a' && word[i] <= 'z')
        {
            points += alfValues[word[i] - 'a'];
        }
        else if (word[i] >= 'A' && word[i] <= 'Z')
        {
            points += alfValues[word[i] - 'A'];
        }
    }
    return (points);
}
