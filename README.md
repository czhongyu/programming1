# programmeren

Programmeren 1 (50621PRP6Y) & 2 (50622PRP6Y), 2018/2019, 1

## CS50

* __[CS50x UvA](https://cs50x.mprog.nl)__
* __[CS50 Reference](https://reference.cs50.net/)__
* __[CS50 IDE](https://cs50.io/)__

## Feedback: Programmeren 1

Course : CS50x
Problem: scratch
`Correctness: 5`
`Grade: pass`

- :) project exists and is valid Scratch program
- :) project contains at least two sprites
- :) project contains a non-cat sprite
- :) project contains at least three scripts
- :) project uses at least one condition
- :) project uses at least one loop
- :) project uses at least one variable
- :) project uses at least one sound

------------------------------------------------------------------------------

Course : CS50x
Problem: resize_less
`Correctness: 5`
`Design: 3`
`Style: 5`
`Grade: 8.5`

- It works, well done! 👍
- For the `for` course, make sure that the names of the variables are correct. The loop for padding is in the loop with `i` and must therefore again be given the letter` j`.
- You always skip over the padding, and then return with `fseek`. It makes more sense to only skim the padding when you actually start reading a new line.
- You iterate over the scanlines of the infile, but use the `bi.biHeight` for that which has since been multiplied by the factor.
- Comment looks great!

------------------------------------------------------------------------------

Course : CS50x
Problem: recover
`Correctness: 5`
`Design: 3`
`Style: 5`
`Grade: 8.5`

- The program works!
- Always check whether a file has been successful when opening a file. If it fails and you just continue your program will crash.
- Avoid magic numbers where possible, for this you can often create better constants with for example `#define`.
- Your program now makes two calls to `fwrite ()` but by restructuring the logic this could also be one call.
- Good comments!

------------------------------------------------------------------------------

Course : CS50x
Problem: mario_more
`Correctness: 5`
`Design: 4`
`Style: 3`
`Grade: 8.5`

* Avoid using magic numbers (like `23`). Use `#define` instead.

------------------------------------------------------------------------------

Course : CS50x
Problem: credit
`Correctness: 5`
`Design: 4`
`Style: 3`
`Grade: 8.5`

* Given your level, it would be good to think about making your code more general. How can you make a stronger separation between data and algorithm? Think about lookup tables, `#define`'s, etc.

------------------------------------------------------------------------------

Course : CS50x
Problem: caesar
`Correctness: 5`
`Design: 4`
`Style: 5`
`Grade: 9.3`

* Good

------------------------------------------------------------------------------

Course : CS50x
Problem: crack
`Correctness: 5`
`Design: 2`
`Style: 5`
`Grade: 7.8`

* It is hard to do this problem with good design. But try to avoid replicating code. By creating separate cases for you key-length you create way to much repetition in your code. This makes your code very prone to bugs and hard to alter/extend.

------------------------------------------------------------------------------

Course : CS50x
Problem: music
`Correctness: 5`
`Design: 3`
`Style: 5`
`Grade: 8.5`

* Well written code!
* There is an easier way to test if `s` is an empty string: E.g., `return !s[0]`.
* You could have made the code much more elegant by using a lookup table for the conversion of `note[0]` to `n`.

------------------------------------------------------------------------------

Course : CS50x
Problem: find_more
`Correctness: 5`
`Design: 4`
`Style: 5`
`Grade: 9.3`

* Very good!
* Don't forget to mention which sort you're implementing (counting sort).
* Pro tip: It is convention to make upper bounds exclusive in computer science. So `high = n`, not `high = n - 1`.  Of course this would require some more adjustments to the code.

------------------------------------------------------------------------------

Course : CS50x
Problem: hello
`Correctness: 5`
`Grade: pass`

- Totally correct!

------------------------------------------------------------------------------

Course : CS50x
Problem: initials_more
`Correctness: 5`
`Grade: pass`

- Totally correct!

------------------------------------------------------------------------------

Course : CS50x
Problem: water
`Correctness: 5`
`Grade: pass`

- Totally correct!

------------------------------------------------------------------------------

Course : CS50x
Problem: whodunit
`Correctness: 5`
`Grade: 10.0`

- Totally correct!

------------------------------------------------------------------------------

Course : CS50x
Problem: quiz1
`Points : 37/37`
`Grade  : pass`

------------------------------------------------------------------------------

Course : CS50x
Problem: p1normal
`Grade  : 8.5`

## Feedback: Programmeren 2

Course : CS50x
Problem: speller
`Correctness: 5`
`Design: 3`
`Style: 5`
`Grade: 8.1`

* Do not put unnecessary stuff into the `dictionary.h`-file. Put in the `.h`-file only variables and functions that you need in `speller.c` outside `dictionary.c`.
* Good that you have created your own memory for the trie.
* Add a little more comment! Put in the header-comments also which data structure you use (hash table or trie).
* Take a good look at the style guide again. There is still room for improvement in this area. For example with your braces.
* Do not leave `TODOs` in your comment.

------------------------------------------------------------------------------

Course : CS50x
Problem: sentimental
`Correctness: 5`
`Design: 3`
`Style: 3`
`Grade: 7.8`

* Beautiful code for `mario.py` and `cash.py`. Good use of the modulo! And well that you've made a lot of repetition from `vigenere.py`.
* Good that you avoid some magic numbers. Unfortunately they are still in `cash.py`
* If you `key` of `vigenere` immediately confuse `toupper`, you do not need to check here for the for loop. That saves some code.
* Add a comment to each file!

------------------------------------------------------------------------------

Course : CS50x
Problem: adventure
`Correctness: 5`
`Design: 3`
`Style: 4`
`Grade: 8.1`

Neatly the commands classified into functions!
* Try to be a little more detailed in your comments
* do not forget to remove the TODO's and unused code from your code
* Take a good look at the style guide (or use the style50 for python!)

------------------------------------------------------------------------------

Course : CS50x
Problem: simil-less
`Correctness: 5`
`Design: 3`
`Style: 5`
`Grade: 8.5`

* Good use of a function, mainly because it contains (partial) repetition in the code.
* There is still some repetition in the `strings_in_both` function itself.
* You could use better sets for the functions.

------------------------------------------------------------------------------

Course: CS50x
Problem: finance
`Correctness: 5`
`Design: 4`
`Style: 5`
`Grade: 9.3`

* Do not leave your API key in the code! It is dangerous if everyone has access to it!
* You import datetime, but you do not use it anywhere. (Datetime functionality is already included in sql tables)
* Nice use of an error handler, but it is a pity that you only use it once.
* Very nice that there are so many personal touches!

------------------------------------------------------------------------------

Course : CS50x
Problem: quiz2
`Points: 24/24`
`Grade  : pass`

* Perfect score, great!

------------------------------------------------------------------------------

Course : CS50x
Problem: p2normal
`Grade  : 8.5`
