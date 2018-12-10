#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    int i, k, length;
    string p;
    char c;

    //check command-line arguments
    if (argc != 2)
    {
        printf("Usage: ./caesar k\n");
        return 1;
    }

    //get non-negative integer k
    k = atoi(argv[1]);

    //get plaintext
    p = get_string("plaintext:  ");

    //get ciphertext
    printf("ciphertext: ");
    for (i = 0, length = strlen(p); i < length; i++)
    {
        if (!isalpha(p[i]))
        {
            c = p[i];//not a letter
        }
        else if (isupper(p[i]))
        {
            c = (p[i] - 'A' + k) % 26 + 'A';//upper letter
        }
        else
        {
            c = (p[i] - 'a' + k) % 26 + 'a';//lower letter
        }

        printf("%c", c);
    }
    printf("\n");

    return 0;
}