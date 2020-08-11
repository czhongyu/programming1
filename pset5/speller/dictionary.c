// Implements a dictionary's functionality

#include <stdbool.h>
#include <ctype.h>
#include <stdio.h>

#include "dictionary.h"

int trie[DICT][SIZE];
bool is_word[DICT];
int words;
char buffer[LENGTH];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // TODO
    // variables
    int i, index = 0, c;

    // read word
    for (i = 0; word[i] != '\0'; i++)
    {
        c = (word[i] == '\'') ? APOS : (tolower(word[i]) - 'a');
        if (!trie[index][c])
            return false;
        index = trie[index][c];
    }

    if (is_word[index])
        return true;
    else
        return false;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // TODO
    // variables
    int i, place, index = 0, n = 0;

    // open dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
        return false;

    // build trie
    while (fgets(buffer, LENGTH, file))
    {
        for (i = 0; buffer[i]; i++)
        {
            if (buffer[i] == '\n')
            {
                is_word[index] = 1;
                words++;
                index = 0;
            }
            else
            {
                place = (buffer[i] == '\'') ? APOS : (buffer[i]- 'a');
                if (!trie[index][place])
                    trie[index][place] = ++n;
                index = trie[index][place];
            }
        }
    }

    // close file!!!
    fclose(file);

    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return words;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO
    return true;
}