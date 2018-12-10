#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <cs50.h>

int main()
{
    int length, i;

    //get name
    string name = get_string();
    length = strlen(name);

    //print initials
    for (i = 0; i < length; i++)
    {
        if (isalpha(name[i]))
        {
            printf("%c", toupper(name[i]));
            while (isalpha(name[i]))//ignore the rest
            {
                i++;
            }
        }
        else
        {
            continue;//ignore spaces
        }
    }
    printf("\n");

    return 0;
}