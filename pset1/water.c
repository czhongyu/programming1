#include <stdio.h>
#include <cs50.h>

int main()
{
    int minutes, bottles;

    minutes = get_int("Minutes: ");
    bottles = minutes * 12;

    printf("Bottles: %d\n", bottles);

    return 0;
}