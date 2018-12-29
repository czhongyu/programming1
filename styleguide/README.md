# styleguide

There’s no one, right way to stylize code. But there are definitely a lot of wrong (or, at least, bad ways). Even so, CS50 does ask that you adhere to the conventions below so that we can reliably analyze your code’s style. Similarly do companies typically adopt their own, company-wide conventions for style.

## Comments

Comments make code more readable, not only for others (e.g., your TF) but also for you, especially when hours, days, weeks, months, or years pass between writing and reading your own code. Commenting too little is bad. Commenting too much is bad. Where’s the sweet spot? Commenting every few lines of code (i.e., interesting blocks) is a decent rule of thumb. Try to write comments that address one or both of these questions:

1. What does this block do?
1. Why did I implement this block in this way?

Within functions, use “inline comments” and keep them short (e.g., one line), else it becomes difficult to distinguish comments from code, even with __[syntax highlighting](http://en.wikipedia.org/wiki/Syntax_highlighting)__. No need to write in full sentences, but do leave one space between the // and your comment’s first character, as in:

```
// convert Fahrenheit to Celsius
float c = 5.0 / 9.0 * (f - 32.0);
```

In other words, don’t do this:

```
//convert Fahrenheit to Celsius
float c = 5.0 / 9.0 * (f - 32.0);
```

Or this:

```
// Convert Fahrenheit to Celsius.
float c = 5.0 / 9.0 * (f - 32.0);
```

Atop your .c and .h files should be multi-line comments that summarize what your program (or that particular file) does, as in:

```
/**
 * Says hello to the world.
 */
```

Notice how:

1. the first line starts with /**;
1. the last line ends with */; and
1. all of the asterisks (*) between those lines line up perfectly in a column.

Atop each of your functions (except, perhaps, main), meanwhile, should be multi-line comments that summarize what your function, as in:

```
/**
 * Returns n^2 (n squared).
 */
int square(int n)
{
    return n * n;
}
```

## Conditions

Conditions should be styled as follows:

```
if (x > 0)
{
    printf("x is positive\n");
}
else if (x < 0)
{
    printf("x is negative\n");
}
else
{
    printf("x is zero\n");
}
```

Notice how:

1. the curly braces line up nicely, each on its own line, making perfectly clear what’s inside the branch;
1. there’s a single space after each if;
1. each call to printf is indented with 4 spaces;
1. there are single spaces around the > and around the >; and
1. there isn’t any space immediately after each ( or immediately before each ).

To save space, some programmers like to keep the first curly brace on the same line as the condition itself, but we don’t recommend, as it’s harder to read, so don’t do this:

```
if (x < 0) {
    printf("x is negative\n");
} else if (x < 0) {
    printf("x is negative\n");
}
```

And definitely don’t do this:

```
if (x < 0)
    {
    printf("x is negative\n");
    }
else
    {
    printf("x is negative\n");
    }
```

## Switches

Declare a switch as follows:

```
switch (n)
{
    case -1:
        printf("n is -1\n");
        break;

    case 1:
        printf("n is 1\n");
        break;

    default:
        printf("n is neither -1 nor 1\n");
        break;
}
```

Notice how:

1. each curly brace is on its own line;
1. there’s a single space after switch;
1. there isn’t any space immediately after each ( or immediately before each );
1. the switch’s cases are indented with 4 spaces;
1. the cases' bodies are indented further with 4 spaces; and
1. each case (including default) ends with a break.
 
