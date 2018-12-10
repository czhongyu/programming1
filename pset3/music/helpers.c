// Helper functions for music

#include <cs50.h>

#include "helpers.h"
#include <math.h>
#include <string.h>

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    // TODO
    return (fraction[0] - '0') * 8 / (fraction[2] - '0');
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    // TODO
    int n;
    int f;
    switch (note[0]) //XY
    {
        case 'C':
            n = -9;
            break;
        case 'D':
            n = -7;
            break;
        case 'E':
            n = -5;
            break;
        case 'F':
            n = -4;
            break;
        case 'G':
            n = -2;
            break;
        case 'A':
            n = 0;
            break;
        case 'B':
            n = 2;
            break;
        default:
            n = 0;
    }
    if (note[1] == '#') //X#Y
    {
        n += 1;
        n += (note[2] - '4') * 12;
    }
    else if (note[1] == 'b') //XbY
    {
        n -= 1;
        n += (note[2] - '4') * 12;
    }
    else //XY
    {
        n += (note[1] - '4') * 12;
    }

    f = round(pow(2.0, n / 12.0) * 440);

    return f;
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    // TODO
    return !strcmp(s, "");
}
