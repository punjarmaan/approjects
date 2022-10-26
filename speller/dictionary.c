// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;


int sizeCounter = 0;

// TODO: Choose number of buckets in hash table
const unsigned int N = 78;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int key = hash(word);
    node *current = table[key];
    while (current != NULL)
    {
        if (strcasecmp(current->word, word) == 0)
        {
            return true;
        }
        else
        {
            current = current->next;
        }
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int value;
    // TODO: Improve this hash function
    if (strlen(word) >= 3)
    {
        value = toupper(word[0]) - 'A' + toupper(word[1]) - 'A' + toupper(word[2]) - 'A';
    }
    else if (strlen(word) == 2)
    {
        value = toupper(word[0]) - 'A' + toupper(word[1]) - 'A';
    }
    else
    {
        value = toupper(word[0]) - 'A';
    }

    return value;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE* ptr = fopen(dictionary, "r");
    if (ptr == NULL)
    {
        return false;
    }

    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    char buffer[LENGTH +1];
    while(fscanf(ptr, "%s\n", buffer) != EOF)
    {
        node *n = malloc(sizeof(node));
        int bucket = hash(buffer);
        strcpy(n->word, buffer);

        if (table[bucket] == NULL)
        {
            n->next = NULL;
            table[bucket] = n;
        }
        else
        {
            n->next = table[bucket];
            table[bucket] = n;
        }

        sizeCounter++;
    }

    fclose(ptr);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return sizeCounter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int j = 0; j < N; j++)
    {
        node *cursor = table[j];
        while(cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }

        table[j] = NULL;
    }
    return true;
}
