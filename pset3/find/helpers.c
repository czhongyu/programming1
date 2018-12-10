// Helper functions

#include <cs50.h>

#include "helpers.h"

// Returns true if value is in array of n values, else false
bool search(int value, int values[], int n)
{
    // TODO: implement a searching algorithm
    int low, high, mid;

    if (n <= 0) // n is non-positive
    {
        return false;
    }

    low = 0;
    high = n - 1;
    while (low <= high)
    {
        mid = (low + high) / 2;
        if (values[mid] > value)
        {
            high = mid - 1;
        }
        else if (values[mid] < value)
        {
            low = mid + 1;
        }
        else
        {
            return true; //found
        }
    }

    return false; //not found
}

// Sorts array of n values
void sort(int values[], int n)
{
    // TODO: implement an O(n^2) sorting algorithm
    int temp[65536];
    int i, j;

    for (i = 0; i < 65536; i++)
    {
        temp[i] = 0;
    }

    for (i = 0; i < n; i++) //O(n)
    {
        temp[values[i]]++;
    }

    for (i = 0, j = 0; i < 65536; i++)
    {
        for (; temp[i] > 0; temp[i]--)
        {
            values[j++] = i;
        }
    }

    return;
}
