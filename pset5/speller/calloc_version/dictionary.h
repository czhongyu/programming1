// Declares a dictionary's functionality

#ifndef DICTIONARY_H
#define DICTIONARY_H

#include <stdbool.h>

// Maximum length for a word
// (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
#define LENGTH 45

#define SIZE 27
#define APOS 26

// Prototypes
bool check(const char *word);
bool load(const char *dictionary);
unsigned int size(void);
bool unload(void);

typedef struct node
{
   bool is_word;
   struct node *children[SIZE];
}
node;

void offload(node *p);

#endif // DICTIONARY_H
