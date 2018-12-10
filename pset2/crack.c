#define _XOPEN_SOURCE
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <cs50.h>

#define CHECK if (!strcmp(crypt(key, "50"), argv[1])) { printf("%s\n", key); return 0; }

int main(int argc, string argv[])
{
    char key[6];
    int i, j, k, m, n;

    //check command-line arguments
    if (argc != 2)
    {
        printf("Usage: ./crack hash\n");
        return 1;
    }

    //crack
    //1
    key[1] = '\0';
    for (i = 0; i < 26; i++)
    {
        key[0] = 'A' + i;
        CHECK
        key[0] = 'a' + i;
        CHECK
    }

    //2
    key[2] = '\0';
    for (i = 0; i < 26; i++)
    {
        key[0] = 'A' + i;
        for (j = 0; j < 26; j++)
        {
            key[1] = 'A' + j;
            CHECK
            key[1] = 'a' + j;
            CHECK
        }
        key[0] = 'a' + i;
        for (j = 0; j < 26; j++)
        {
            key[1] = 'A' + j;
            CHECK
            key[1] = 'a' + j;
            CHECK
        }
    }

    //3
    key[3] = '\0';
    for (i = 0; i < 26; i++)
    {
        key[0] = 'A' + i;
        for (j = 0; j < 26; j++)
        {
            key[1] = 'A' + j;
            for (k = 0; k < 26; k++)
            {
                key[2] = 'A' + k;
                CHECK
                key[2] = 'a' + k;
                CHECK
            }

            key[1] = 'a' + j;
            for (k = 0; k < 26; k++)
            {
                key[2] = 'A' + k;
                CHECK
                key[2] = 'a' + k;
                CHECK
            }
        }
        key[0] = 'a' + i;
        for (j = 0; j < 26; j++)
        {
            key[1] = 'A' + j;
            for (k = 0; k < 26; k++)
            {
                key[2] = 'A' + k;
                CHECK
                key[2] = 'a' + k;
                CHECK
            }

            key[1] = 'a' + j;
            for (k = 0; k < 26; k++)
            {
                key[2] = 'A' + k;
                CHECK
                key[2] = 'a' + k;
                CHECK
            }
        }
    }

    //4
    key[4] = '\0';
    for (i = 0; i < 26; i++)
    {
        key[0] = 'A' + i;
        for (j = 0; j < 26; j++)
        {
            key[1] = 'A' + j;
            for (k = 0; k < 26; k++)
            {
                key[2] = 'A' + k;
                for (m = 0; m < 26; m++)
                {
                    key[3] = 'A' + m;
                    CHECK
                    key[3] = 'a' + m;
                    CHECK
                }
                key[2] = 'a' + k;
                for (m = 0; m < 26; m++)
                {
                    key[3] = 'A' + m;
                    CHECK
                    key[3] = 'a' + m;
                    CHECK
                }
            }

            key[1] = 'a' + j;
            for (k = 0; k < 26; k++)
            {
                key[2] = 'A' + k;
                for (m = 0; m < 26; m++)
                {
                    key[3] = 'A' + m;
                    CHECK
                    key[3] = 'a' + m;
                    CHECK
                }
                key[2] = 'a' + k;
                for (m = 0; m < 26; m++)
                {
                    key[3] = 'A' + m;
                    CHECK
                    key[3] = 'a' + m;
                    CHECK
                }
            }
        }
        key[0] = 'a' + i;
        for (j = 0; j < 26; j++)
        {
            key[1] = 'A' + j;
            for (k = 0; k < 26; k++)
            {
                key[2] = 'A' + k;
                for (m = 0; m < 26; m++)
                {
                    key[3] = 'A' + m;
                    CHECK
                    key[3] = 'a' + m;
                    CHECK
                }
                key[2] = 'a' + k;
                for (m = 0; m < 26; m++)
                {
                    key[3] = 'A' + m;
                    CHECK
                    key[3] = 'a' + m;
                    CHECK
                }
            }

            key[1] = 'a' + j;
            for (k = 0; k < 26; k++)
            {
                key[2] = 'A' + k;
                for (m = 0; m < 26; m++)
                {
                    key[3] = 'A' + m;
                    CHECK
                    key[3] = 'a' + m;
                    CHECK
                }
                key[2] = 'a' + k;
                for (m = 0; m < 26; m++)
                {
                    key[3] = 'A' + m;
                    CHECK
                    key[3] = 'a' + m;
                    CHECK
                }
            }
        }
    }


    //5
    key[5] = '\0';
    for (i = 0; i < 26; i++)
    {
        key[0] = 'A' + i;
        for (j = 0; j < 26; j++)
        {
            key[1] = 'A' + j;
            for (k = 0; k < 26; k++)
            {
                key[2] = 'A' + k;
                for (m = 0; m < 26; m++)
                {
                    key[3] = 'A' + m;
                    for (n = 0; n < 26; n++)
                    {
                        key[4] = 'A' + n;
                        CHECK
                        key[4] = 'a' + n;
                        CHECK
                    }

                    key[3] = 'a' + m;
                    for (n = 0; n < 26; n++)
                    {
                        key[4] = 'A' + n;
                        CHECK
                        key[4] = 'a' + n;
                        CHECK
                    }
                }
                key[2] = 'a' + k;
                for (m = 0; m < 26; m++)
                {
                    key[3] = 'A' + m;
                    for (n = 0; n < 26; n++)
                    {
                        key[4] = 'A' + n;
                        CHECK
                        key[4] = 'a' + n;
                        CHECK
                    }

                    key[3] = 'a' + m;
                    for (n = 0; n < 26; n++)
                    {
                        key[4] = 'A' + n;
                        CHECK
                        key[4] = 'a' + n;
                        CHECK
                    }
                }
            }

            key[1] = 'a' + j;
            for (k = 0; k < 26; k++)
            {
                key[2] = 'A' + k;
                for (m = 0; m < 26; m++)
                {
                    key[3] = 'A' + m;
                    for (n = 0; n < 26; n++)
                    {
                        key[4] = 'A' + n;
                        CHECK
                        key[4] = 'a' + n;
                        CHECK
                    }

                    key[3] = 'a' + m;
                    for (n = 0; n < 26; n++)
                    {
                        key[4] = 'A' + n;
                        CHECK
                        key[4] = 'a' + n;
                        CHECK
                    }
                }
                key[2] = 'a' + k;
                for (m = 0; m < 26; m++)
                {
                    key[3] = 'A' + m;
                    for (n = 0; n < 26; n++)
                    {
                        key[4] = 'A' + n;
                        CHECK
                        key[4] = 'a' + n;
                        CHECK
                    }

                    key[3] = 'a' + m;
                    for (n = 0; n < 26; n++)
                    {
                        key[4] = 'A' + n;
                        CHECK
                        key[4] = 'a' + n;
                        CHECK
                    }
                }
            }
        }
        key[0] = 'a' + i;
        for (j = 0; j < 26; j++)
        {
            key[1] = 'A' + j;
            for (k = 0; k < 26; k++)
            {
                key[2] = 'A' + k;
                for (m = 0; m < 26; m++)
                {
                    key[3] = 'A' + m;
                    for (n = 0; n < 26; n++)
                    {
                        key[4] = 'A' + n;
                        CHECK
                        key[4] = 'a' + n;
                        CHECK
                    }

                    key[3] = 'a' + m;
                    for (n = 0; n < 26; n++)
                    {
                        key[4] = 'A' + n;
                        CHECK
                        key[4] = 'a' + n;
                        CHECK
                    }
                }
                key[2] = 'a' + k;
                for (m = 0; m < 26; m++)
                {
                    key[3] = 'A' + m;
                    for (n = 0; n < 26; n++)
                    {
                        key[4] = 'A' + n;
                        CHECK
                        key[4] = 'a' + n;
                        CHECK
                    }

                    key[3] = 'a' + m;
                    for (n = 0; n < 26; n++)
                    {
                        key[4] = 'A' + n;
                        CHECK
                        key[4] = 'a' + n;
                        CHECK
                    }
                }
            }

            key[1] = 'a' + j;
            for (k = 0; k < 26; k++)
            {
                key[2] = 'A' + k;
                for (m = 0; m < 26; m++)
                {
                    key[3] = 'A' + m;
                    for (n = 0; n < 26; n++)
                    {
                        key[4] = 'A' + n;
                        CHECK
                        key[4] = 'a' + n;
                        CHECK
                    }

                    key[3] = 'a' + m;
                    for (n = 0; n < 26; n++)
                    {
                        key[4] = 'A' + n;
                        CHECK
                        key[4] = 'a' + n;
                        CHECK
                    }
                }
                key[2] = 'a' + k;
                for (m = 0; m < 26; m++)
                {
                    key[3] = 'A' + m;
                    for (n = 0; n < 26; n++)
                    {
                        key[4] = 'A' + n;
                        CHECK
                        key[4] = 'a' + n;
                        CHECK
                    }

                    key[3] = 'a' + m;
                    for (n = 0; n < 26; n++)
                    {
                        key[4] = 'A' + n;
                        CHECK
                        key[4] = 'a' + n;
                        CHECK
                    }
                }
            }
        }
    }

    return 0;
}