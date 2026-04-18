// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include "dictionary.h"
#include <string.h>
#include <strings.h>
#include <stdlib.h>

#define HASH_LENGTH 100

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Hash table
node *table[HASH_LENGTH];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    unsigned int hashvalue = hash(word);


    node *indexcursor;

    indexcursor = table[hashvalue];

    while (indexcursor != NULL){
        if (strcasecmp(indexcursor->word, word) == 0){
            return true;
        }

        indexcursor = indexcursor->next;
    }
    return false;
}

unsigned int countofwords = 0;

// Hashes word to a number
unsigned int hash(const char *word)
{
    int sum = 0;
    int len = strlen(word);
    char copy[len+1];

    for (int i = 0; word[i] != '\0'; i++)
    {
         copy[i] = toupper(word[i]);
    }
    copy[len] = '\0';

    for (int i = 0; copy[i] != '\0'; i++)
    {
        sum += copy[i];
    }
    // printf("Word: %s, Hash: %i", word, sum);
    return sum % HASH_LENGTH;
    //output is always between 1 and HASH_LENGTH digit integer

    // TODO: Improve this hash function
    // return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open the dictionary file
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        printf("Could not open %s.\n", dictionary);
        return false;
    }
    countofwords = 0;
    char wordbuffer[LENGTH + 1];
    while (fscanf(source, "%s", wordbuffer) != EOF)
    {
        node *nodetemp = malloc(sizeof(node));
        if (nodetemp == NULL)
        {
            return false;
        }

        strcpy(nodetemp->word, wordbuffer);

        unsigned int hashindex = hash(wordbuffer);

        nodetemp->next = table[hashindex]; //move current pointer to node at table index

        table[hashindex] = nodetemp; //add current node to table index

        countofwords++;
    }

    // Close the dictionary file
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return countofwords;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{

    int nodes_free = 0;

    for (int i = 0; i < HASH_LENGTH; i++){
     node *cursor = table[i];

     while (cursor != NULL)
     {
        node *temp = cursor;
        cursor = cursor->next;
        free(temp);
        nodes_free++;
     }
    }
    if(nodes_free == countofwords){
        return true;
    }

    return false;
}
