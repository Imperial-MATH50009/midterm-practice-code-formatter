# Principles of Programming mid-term test practice

The instructions are similar those that will be on the test. This exercise
won't be manually marked, but there are tests and the autograder, and you can
ask questions on Piazza about this problem.

## Instructions

1. Ensure your Principles of Programming venv is active.
2. Clone this repository.
3. Complete the programming tasks. Tests are provided for parts 2 and 3.
   Parts 1 and 4.1 are tested by the autograder when you push.
4. Commit and push as you go. **Do not** rely on one big commit and push at the
   end of the test. Only commits timestamped before the end of the test
   will count.

The tests and autograder are a guide, the test will be manually marked in order
to ensure that your code doesn`t produce the right output for the wrong reasons,
and in order to allocate the part 4.2 style marks.

## The task

We consider a fictional programming language "brak". We don't need to consider
ourselves with most of the rules of the language, but we will be concerned with
brackets. The language will use square (`[]`), round (`()`), and curly brackets
(`{}`). Brackets can contain other code, but pairs of brackets must always
match. That is to say, a closing bracket must always be of the same sort as it's
matching opening bracket. The following would be valid:
```
something(foo[
    x{}
])
```
but this would be invalid:
```
something(foo[
    x{}
))
```
because the opening square bracket is matched by a closing round bracket. The
following would also be invalid:
```
(({[]})
```
because the outermost round bracket is never closed. Similarly, an unmatched
opening bracket is invalid:
```
foo)
```

Your challenge is to make a syntax checker for this language.

### Part 1 (2 marks)

Create a package `brak` containing a module `brak.py`. Make the package installable.

### Part 2 (3 marks)

In the `brak.brak` module, create a class `Program`. The constructor of this
class should take in a single string containing a Brak program. In storing the
program in the class instance, you will want to split it into lines using the
[split method](https://docs.python.org/3/library/stdtypes.html#str.split). It
will be helpful to know that lines are separated by the newline character,
`"\n"`. (2 marks)

Implement a method `line()` which takes a single integer parameter whose value
is a line number (starting from 0). `line()` should return the corresponding
line of the program. (1 mark)

### Part 3 (11 marks)

Implement a method `verify()`, which should take no parameters (other than the
object itself, obviously). This method should verify whether the brackets in the
program are balanced in accordance with the language rules given above. If the
brackets in the code are properly balanced then the method should return `True`.
(2 marks)

There are three erroneous cases which should be handled:

1. If an open bracket of one sort is matched by a closing bracket of a different
   sort then the method should raise `ValueError` with an error message of the
   following format. For example if an opening round bracket which is the first
   (position 0) character on line 0 is matched by a closing square bracket on
   line 4, position 10 then the message would be:
   "( on line 0 position 0 matched by ] on line 4 position 10." (3 marks)
2. If one or more open brackets is not matched by a closing bracket at all, then
   the method should raise `ValueError` with an error message of the following
   format. The error message should report the innermost unmatched bracket. For
   example if the program were:
   ```
    ([ foo wibble{
    } bar 
    baz
   ```
    then the square bracket is the innermost unmatched bracket, and the error
    would read "[ at line 0 position 1 unmatched." (3 marks)
3. If a closing bracket is encountered when no bracket is currently open then
   the method should raise `ValueError` with an error message of the following
   format. The error message should report the first unmatched closing bracket
   encountered. For example if the program was:
   ```
    foo()
    }
   ```  
   then the error message would read "} at line 1 position 0 unmatched." (3 marks)

In order to implement this method, you will want to loop through the characters
of each line and record any open brackets you find on a stack. As you encounter
matching closing brackets you will remove the corresponding open bracket from
the stack. Think carefully about what information you will need to store in
each stack item in order to implement the exercise.

### Part 4 (4 marks)

1. Ensure that your code passes Flake8 (2 marks); and 
2. otherwise conforms to good programming style as we have learned in this
   course (2 marks).

There is no need to write any docstrings for this test.
