#include <stdio.h>
#include <cs50.h>

int main()
{
    int height, i, j;

    //get integer
    do
    {
        height = get_int("Height: ");
    } while(height < 0 || height > 23);

    //draw pyramid
    for(i = 1; i <= height; i++)
    {
        //left half
        for(j = height - i; j > 0; j--)
            printf(" ");
        for(j = i; j > 0; j--)
            printf("#");
        //seperation
        printf("  ");
        //right half
        for(j = i; j > 0; j--)
            printf("#");
        //new line
        printf("\n");
    }

    return 0;
}