// Implements a dictionary's functionality

#include <stdbool.h>
#include <malloc.h>
#include <ctype.h>

#include "dictionary.h"

// root pointer
node *root;
// count of words
int words;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // TODO
    // variables
    int c, i;

    // read word
    node *p = root;
    for (i = 0; word[i] != '\0'; i++)
    {
        if (word[i] == '\'')
        {
            if (p->children[APOS] == NULL)
                return false;
            else
                p = p->children[APOS];
        }
        else
        {
            c = tolower(word[i]) - 'a';
            if (p->children[c] == NULL)
                return false;
            else
                p = p->children[c];
        }
    }

    // check if is_word
    if (p->is_word)
        return true;
    else
        return false;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // TODO

    // variables
    int c;
    node *p = NULL;

    // open dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("Could not open %s.\n", dictionary);
        return false;
    }

    // head pointer
    root = (struct node *)calloc(1, sizeof(node));
    if (root == NULL)
        return false;

    // build trie
    p = root;
    for (c = fgetc(file); c != EOF; c = fgetc(file))
    {
        if (c == '\n')
        {
            p->is_word = 1;
            words++;
            p = root;
        }
        else if (c == '\'')
        {
            if (p->children[APOS] == NULL)
            {
                p->children[APOS] = (struct node *)calloc(1, sizeof(node));
                if (p->children[APOS] == NULL)
                    return false;
            }
            p = p->children[APOS];
        }
        else
        {
            c = c - 'a';
            if (p->children[c] == NULL)
            {
                p->children[c] = (struct node *)calloc(1, sizeof(node));
                if (p->children[c] == NULL)
                    return false;
            }
            p = p->children[c];
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
    offload(root);

    return true;
}

void offload(node *p)
{
    if (p)
    {
        // recursion
        for (int i = 0; i < SIZE; i++)
            offload(p->children[i]);
        // free memory
        free(p);
    }

    return;
}