#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char buffer[1024];
    char filename[10];
    int count = 0;
    FILE *img = NULL;

    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    // open input file
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", argv[1]);
        return 2;
    }

    // recover imgs
    while (fread(buffer, 1, 512, file) == 512)
    {
        if ((buffer[0] & 0xff) == 0xff &&
            (buffer[1] & 0xff) == 0xd8 &&
            (buffer[2] & 0xff) == 0xff &&
            (buffer[3] & 0xf0) == 0xe0) // found a new img
        {
            if (img != NULL) // close the last img
            {
                fclose(img);
            }
            // new img
            sprintf(filename, "%03i.jpg", count++);
            img = fopen(filename, "w");
            fwrite(buffer, 1, 512, img);
        }
        else if (img != NULL) // continue writing the img
        {
            fwrite(buffer, 1, 512, img);
        }
    }

    // close img
    fclose(img);

    // success
    return 0;
}
