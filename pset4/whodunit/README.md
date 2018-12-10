# Questions

## What's `stdint.h`?

In different system environments, the same data types may have different sizes.
For example, the size of int may be 16 bits or 32 bits depending on the environment.
<stdint.h> is a header file that provides data types with custom sizes that are universal and stay the same in different environments.
For example, it provides the data type int32_t, which is an integer with a fixed length of 32 bits in any environments.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

To make sure the data types are universal and has the same size and type in different system environments.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE: 1 byte
DWORD: 4 bytes
LONG: 4 bytes
WORD: 2 bytes

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

The first two bytes are bfType, which is the file type and must be BM.

## What's the difference between `bfSize` and `biSize`?

bfSize is the size of the bitmap file in bytes.
biSize is the size of the struct BITMAPINFOHEADER in bytes.

## What does it mean if `biHeight` is negative?

It indicates a top-down DIB, which can't be compressed and biCompression must be either BI_RGB or BI_BITFIELDS.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

It's biBitCount.

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

When it can't find the file, it returns NULL.

## Why is the third argument to `fread` always `1` in our code?

The third argument indicates how many elements you want to read and we only need 1 struct.

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

padding would be 3.

## What does `fseek` do?

It would move to a specific location of a file.

## What is `SEEK_CUR`?

It's an integer constant which specifies that the offset provided is relative to the current file position.
