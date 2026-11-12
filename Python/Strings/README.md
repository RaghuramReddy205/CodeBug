# 🐍 Python Strings — The Complete Guide

![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white) ![Strings](https://img.shields.io/badge/Topic-Strings-orange) ![Beginner to Advanced](https://img.shields.io/badge/Level-Beginner%20to%20Advanced-success) ![Examples included](https://img.shields.io/badge/Examples-Included-brightgreen)

> 🚀 **Your complete Python string handbook** — learn how strings work, explore built-in functions and methods, practise common patterns, and solve 25 coding problems.
>
> 🧠 **Core idea:** A Python string (`str`) is an **immutable Unicode sequence**. String operations create new strings rather than changing the original one.

## ✨ What you'll learn

| 🧭 Section | 🎯 What you'll be able to do |
|---|---|
| 🧱 Fundamentals | Create strings, use quotes, escape characters, index and slice text |
| 🛠️ Built-ins & methods | Use Python's built-in functions and important `str` methods confidently |
| 🔎 Text processing | Search, count, validate, replace, split, join and format text |
| 🌍 Unicode & regex | Understand encoding and use regular expressions for pattern matching |
| 💻 Problem solving | Build logic for 25 practical string problems (Questions 51–75) |

## ⚡ Quick learning dashboard

Use this checklist to track your progress as you study. You can change `[ ]` to `[x]` in your copy of this README.

- [ ] 📘 Understand string creation, indexing and slicing
- [ ] 🔒 Understand immutability and string operators
- [ ] 🧰 Practise built-in functions such as `len()`, `ord()` and `chr()`
- [ ] 🧪 Learn the important string methods and their differences
- [ ] 🔍 Practise searching, splitting, joining and formatting
- [ ] 🌐 Understand Unicode, encoding and regular expressions
- [ ] 🏆 Solve all 25 practice problems (51–75)

## 🗺️ How to use this guide

1. **Learn the concept** — read the explanation and inspect the example.
2. **Predict the output** — pause before running each code block.
3. **Run and experiment** — change the input and observe what happens.
4. **Practise without looking** — solve the related problem yourself.
5. **Revise** — use the quick-reference tables whenever you get stuck.

> 💡 **Pro tip:** Don't memorise every method. Understand what it does, what it returns, and when to use it. Pay special attention to similar methods such as `find()` vs `index()` and `isdecimal()` vs `isdigit()` vs `isnumeric()`.

### 🧠 Your learning path

🧩 String basics → 🎯 Indexing and slicing → 🛠️ Built-ins and methods → 🔎 Text processing → 🌍 Unicode and regex → 🏆 25 coding challenges → 🚀 Confident string handling

> 🐍 **Python version:** Examples target modern Python 3 (Python 3.10+ unless stated otherwise).

---

## 🧭 Table of contents

Jump directly to a topic:

1. [🧩 What is a string?](#1-what-is-a-string)
2. [✍️ Creating strings](#2-creating-strings)
3. [🪄 Quotes, escaping, and raw strings](#3-quotes-escaping-and-raw-strings)
4. [📄 Multiline strings](#4-multiline-strings)
5. [🎯 Indexing and slicing](#5-indexing-and-slicing)
6. [🔒 Immutability](#6-immutability)
7. [➕ String operators](#7-string-operators)
8. [🛠️ Built-in functions](#8-built-in-functions-that-work-with-strings)
9. [📚 String methods reference](#9-string-methods-complete-reference)
10. [✅ Character checks and validation](#10-character-checks-and-validation)
11. [🔎 Searching and counting](#11-searching-and-counting)
12. [🔁 Replacing, splitting, and joining](#12-replacing-splitting-and-joining)
13. [🧹 Removing whitespace and trimming](#13-removing-whitespace-and-trimming)
14. [🎨 String formatting](#14-string-formatting)
15. [🌍 Unicode, characters, and encoding](#15-unicode-characters-and-encoding)
16. [⚖️ Comparing strings and sorting](#16-comparing-strings-and-sorting)
17. [🔄 Iterating through strings](#17-iterating-through-strings)
18. [💻 Common string programs](#18-common-string-programs-and-patterns)
19. [🧬 Regular expressions](#19-regular-expressions)
20. [⚠️ Common mistakes](#20-common-mistakes)
21. [⏱️ Time and space considerations](#21-time-and-space-considerations)
22. [📌 Quick reference](#22-quick-reference)
23. [🏆 Practice questions](#23-practice-questions)

------------------------------------------------------------------------

## 1. 🧩 What is a string?

A **string** is a sequence of characters used to store text.

```python
name = "Raghuram"
message = "Welcome to Python!"
city = "Hyderabad"

print(name)
print(message)
print(city)
```

Output:

```text
Raghuram
Welcome to Python!
Hyderabad
```

A string can contain letters, digits, spaces, punctuation, and Unicode
characters.

```python
text1 = "Python"
text2 = "Python 3"
text3 = "12345"
text4 = "Hello, world!"
text5 = "నమస్కారం"
text6 = "😊"
```

Even when a string contains only digits, it is still text:

```python
value = "123"
print(type(value))  # <class 'str'>
```

Convert it to an integer when you need arithmetic:

```python
value = "123"
number = int(value)
print(number + 10)  # 133
```

### Strings are sequences

A string stores characters in an ordered sequence. Each character has a
position called an **index**.

```python
word = "PYTHON"
# Index:  0 1 2 3 4 5
# Char:   P Y T H O N
```

Python's `str` type is a built-in sequence type.

------------------------------------------------------------------------

## 2. ✍️ Creating strings

### 2.1 Single quotes

```python
a = 'Hello'
```

### 2.2 Double quotes

```python
b = "Hello"
```

Both create the same string type. Choose the quote style that makes the
text easiest to read.

```python
sentence = "It's a beautiful day."
quote = 'He said, "Hello!"'
```

### 2.3 Triple quotes

Triple single or double quotes are useful for text that spans multiple
lines.

```python
paragraph = """Python is a programming language.
It is readable and beginner-friendly."""
```

### 2.4 The `str()` constructor

`str()` converts many values into their string representation.

```python
age = 18
price = 99.5
is_student = True

print(str(age))        # '18'
print(str(price))      # '99.5'
print(str(is_student)) # 'True'
```

`str()` is conversion, not validation. For example, `str(123)` creates
the text `"123"`; it does not preserve the number as an integer.

### 2.5 Empty string

```python
empty = ""
print(len(empty))  # 0
print(bool(empty)) # False
```

------------------------------------------------------------------------

## 3. 🪄 Quotes, escaping, and raw strings

### 3.1 Escape sequences

An escape sequence begins with a backslash (`\\`) and represents a
special character.

  Escape   Meaning               Example
  -------- --------------------- ----------------------
  `\\n`    New line              `"Hello\\nWorld"`
  `\\t`    Horizontal tab        `"A\\tB"`
  `\\\\`   A literal backslash   `"C:\\\\Users"`
  `\\'`    Single quote          `'It\\'s OK'`
  `\\"`    Double quote          `"He said \\"Hi\\""`
  `\\r`    Carriage return       `"A\\rB"`
  `\\b`    Backspace             `"AB\\bC"`
  `\\f`    Form feed             `"A\\fB"`
  `\\v`    Vertical tab          `"A\\vB"`
  `\\0`    Null character        `"A\\0B"`

Examples:

```python
print("Hello\nWorld")
print("Name:\tRaghuram")
print("C:\\Users\\Student")
print("It's Python")
```

### 3.2 Raw strings

Prefix a string with `r` or `R` to make it a raw string. Backslashes are
treated mostly as literal characters instead of starting escape
sequences.

```python
path = r"C:\Users\Student\Documents"
print(path)

pattern = r"\d+\.\d+"
print(pattern)
```

Raw strings are particularly useful for Windows paths and regular
expressions. A raw string cannot end in an odd number of backslashes
because the final backslash would escape the closing quote.

### 3.3 Unicode escapes

```python
print("\u0041")  # A
print("\U0001F600")  # 😀
```

------------------------------------------------------------------------

## 4. 📄 Multiline strings

Use triple quotes for paragraphs, SQL statements, or other multiline
text.

```python
message = """Hello,
Welcome to the Python strings guide.
Keep practising!"""

print(message)
```

Newlines and indentation inside the triple-quoted string are part of the
string. If exact whitespace matters, inspect it with `repr()`:

```python
text = """Line one
Line two"""
print(repr(text))
```

------------------------------------------------------------------------

## 5. 🎯 Indexing and slicing

### 5.1 Positive indexing

Indexing starts at `0`.

```python
word = "PYTHON"

print(word[0])  # P
print(word[1])  # Y
print(word[5])  # N
```

### 5.2 Negative indexing

Negative indexes count from the end. `-1` is the last character.

```python
word = "PYTHON"

print(word[-1])  # N
print(word[-2])  # O
print(word[-6])  # P
```

### 5.3 Slicing

General form:

```python
string[start:stop:step]
```

-   `start`: index to begin at; included.
-   `stop`: index to stop before; excluded.
-   `step`: how many positions to move each time.
-   An omitted start, stop, or step uses a default.

```python
word = "PYTHON"

print(word[0:3])   # PYT
print(word[2:5])   # THO
print(word[:4])    # PYTH
print(word[2:])    # THON
print(word[:])     # PYTHON
print(word[::2])   # PTO
print(word[1::2])  # YHN
print(word[::-1])  # NOHTYP
```

### 5.4 Important slicing examples

```python
text = "ABCDEFGHIJ"

print(text[1:8:2])  # BDFH
print(text[-5:-1])  # FGHI
print(text[::-2])   # JHFDB
print(text[100:])   # ''
```

Slicing beyond the string's boundaries is safe and is clipped to the
available range. Direct indexing outside the valid range raises
`IndexError`.

```python
text = "Python"
# print(text[10])  # IndexError
print(text[10:20])  # ''
```

------------------------------------------------------------------------

## 6. 🔒 Immutability

Strings cannot be changed in place.

```python
word = "Python"
# word[0] = "J"  # TypeError: 'str' object does not support item assignment
```

Create a new string instead:

```python
word = "Python"
word = "J" + word[1:]
print(word)  # Jython
```

Methods such as `upper()`, `replace()`, and `strip()` return new
strings. They do not alter the original string.

```python
text = "python"
result = text.upper()

print(text)    # python
print(result)  # PYTHON
```

------------------------------------------------------------------------

## 7. ➕ String operators

### 7.1 Concatenation (`+`)

Joins strings.

```python
first = "Hello"
second = "World"
print(first + " " + second)  # Hello World
```

Both operands must be strings:

```python
age = 18
# print("Age: " + age)  # TypeError
print("Age: " + str(age))
```

### 7.2 Repetition (`*`)

```python
print("Hi " * 3)  # Hi Hi Hi
print("-" * 20)
```

### 7.3 Membership (`in`, `not in`)

```python
text = "Python programming"

print("Python" in text)      # True
print("Java" in text)        # False
print("Java" not in text)    # True
```

Membership is case-sensitive:

```python
print("python" in "Python")  # False
```

### 7.4 Comparison operators

Strings are compared lexicographically using Unicode code points.

```python
print("apple" == "apple")  # True
print("apple" != "Apple")  # True
print("apple" < "banana")  # True
print("cat" > "car")       # True
```

Comparison is case-sensitive. For case-insensitive comparison, use
`casefold()`:

```python
print("PYTHON".casefold() == "Python".casefold())  # True
```

### 7.5 Length (`len`)

```python
text = "Hello World"
print(len(text))  # 11, including the space
```

------------------------------------------------------------------------

## 8. 🛠️ Built-in functions that work with strings

These are Python built-ins, not methods called with dot notation.

### 8.1 `len(value)`

Returns the number of Unicode code points in the string.

```python
print(len("Python"))  # 6
print(len(""))        # 0
```

### 8.2 `str(value)`

Converts a value to a string.

```python
print(str(250))     # '250'
print(str(3.14))    # '3.14'
print(str(True))    # 'True'
```

### 8.3 `print(*objects)`

Displays values. `sep` controls the separator and `end` controls what is
printed at the end.

```python
print("Python", "Java", "C", sep=" | ")
print("Hello", end=" ")
print("World")
```

### 8.4 `input(prompt)`

Reads a line from the user and returns it as a string.

```python
name = input("Enter your name: ")
print("Hello", name)
```

Convert the input when a number is required:

```python
age = int(input("Enter age: "))
```

### 8.5 `repr(value)`

Returns a representation useful for debugging. It shows quotes and
escape characters.

```python
text = "Hello\nWorld"
print(text)
print(repr(text))
```

### 8.6 `ascii(value)`

Returns a representation in which non-ASCII characters are escaped.

```python
print(ascii("café"))
```

### 8.7 `ord(character)`

Returns the Unicode code point of a single character.

```python
print(ord("A"))  # 65
print(ord("a"))  # 97
```

It expects a string containing exactly one Unicode code point.

### 8.8 `chr(number)`

Returns the character for a valid Unicode code point.

```python
print(chr(65))     # A
print(chr(128512)) # 😀
```

### 8.9 `sorted(iterable)`

Returns a **list** of sorted characters, not a string.

```python
text = "dcba"
characters = sorted(text)
print(characters)              # ['a', 'b', 'c', 'd']
print("".join(characters))     # abcd
```

### 8.10 `reversed(sequence)`

Returns a reverse iterator.

```python
text = "Python"
print("".join(reversed(text)))  # nohtyP
```

### 8.11 `min()` and `max()`

Return the smallest or largest character according to Unicode ordering.

```python
text = "python"
print(min(text))
print(max(text))
```

### 8.12 `all()` and `any()`

Useful with generator expressions and character checks.

```python
text = "12345"
print(all(ch.isdigit() for ch in text))  # True
print(any(ch.isupper() for ch in text))  # False
```

### 8.13 `enumerate()`

Provides each character together with its index.

```python
for index, character in enumerate("Python"):
    print(index, character)
```

### 8.14 `map()` and `filter()`

Apply a function to characters or keep characters that satisfy a
condition.

```python
text = "python"
upper_text = "".join(map(str.upper, text))
print(upper_text)  # PYTHON

digits = "".join(filter(str.isdigit, "a1b2c3"))
print(digits)  # 123
```

### 8.15 `format()`

Formats values using a format string.

```python
print("Name: {}".format("Raghuram"))
print("Score: {:.2f}".format(95.678))  # Score: 95.68
```

### 8.16 `iter()`

Creates an iterator over the characters.

```python
iterator = iter("ABC")
print(next(iterator))  # A
print(next(iterator))  # B
```

### 8.17 `type()` and `isinstance()`

Check the type of a value.

```python
text = "Python"
print(type(text))                 # <class 'str'>
print(isinstance(text, str))      # True
```

### 8.18 `bytes()` and `bytearray()`

These are related to text encoding; see the Unicode and encoding
section.

```python
encoded = "Hello".encode("utf-8")
print(encoded)  # b'Hello'
```

------------------------------------------------------------------------

## 9. 📚 String methods --- complete reference

Call a string method using dot notation:

```python
text = "python"
print(text.upper())
```

The following methods are grouped by purpose.

### 9.1 Case conversion methods

  -------------------------------------------------------------------------
  Method                  Purpose                 Example result
  ----------------------- ----------------------- -------------------------
  `upper()`               Convert letters to      `"python".upper()` →
                          uppercase               `"PYTHON"`

  `lower()`               Convert letters to      `"PYTHON".lower()` →
                          lowercase               `"python"`

  `capitalize()`          Uppercase first         `"hELLO".capitalize()` →
                          character; lowercase    `"Hello"`
                          the rest                

  `title()`               Title-case words        `"hello world".title()` →
                                                  `"Hello World"`

  `swapcase()`            Change uppercase to     `"PyThOn".swapcase()` →
                          lowercase and vice      `"pYtHoN"`
                          versa                   

  `casefold()`            Stronger case           `"Straße".casefold()` →
                          normalization for       `"strasse"`
                          caseless matching       
  -------------------------------------------------------------------------

```python
text = "pYTHON programming"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())
print("PYTHON".casefold())
```

`title()` is not a perfect natural-language title formatter. For
example, punctuation and apostrophes can produce results that may not
match editorial style.

### 9.2 Searching methods

  Method                 Purpose
  ---------------------- ----------------------------------------------------
  `find(sub)`            First index of substring; returns `-1` if missing
  `rfind(sub)`           Last index of substring; returns `-1` if missing
  `index(sub)`           Like `find()`, but raises `ValueError` if missing
  `rindex(sub)`          Like `rfind()`, but raises `ValueError` if missing
  `count(sub)`           Number of non-overlapping occurrences
  `startswith(prefix)`   Checks the beginning
  `endswith(suffix)`     Checks the ending

```python
text = "banana"

print(text.find("na"))       # 2
print(text.rfind("na"))      # 4
print(text.index("a"))       # 1
print(text.rindex("a"))      # 5
print(text.count("a"))       # 3
print(text.startswith("ban"))  # True
print(text.endswith("na"))     # True
```

`find()` versus `index()`:

```python
text = "Python"
print(text.find("z"))  # -1
# print(text.index("z"))  # ValueError
```

You can provide optional start and end positions:

```python
text = "banana"
print(text.find("a", 2))      # 3
print(text.count("a", 2, 5))  # 2
```

`startswith()` and `endswith()` also accept tuples:

```python
filename = "report.pdf"
print(filename.endswith((".pdf", ".txt")))  # True
```

### 9.3 Replacing and translating methods

  Method                       Purpose
  ---------------------------- ----------------------------------------------
  `replace(old, new)`          Replace occurrences
  `replace(old, new, count)`   Replace at most `count` occurrences
  `maketrans()`                Build a translation table
  `translate(table)`           Translate or delete characters using a table

```python
text = "I like Java"
print(text.replace("Java", "Python"))  # I like Python

text = "one one one"
print(text.replace("one", "two", 2))  # two two one
```

Character translation:

```python
table = str.maketrans("aeiou", "12345")
print("education".translate(table))
```

Delete selected characters:

```python
table = str.maketrans("", "", "aeiou")
print("education".translate(table))  # dctn
```

### 9.4 Splitting methods

  Method                            Purpose
  --------------------------------- ---------------------------------------
  `split(sep=None, maxsplit=-1)`    Split from the left
  `rsplit(sep=None, maxsplit=-1)`   Split from the right
  `splitlines(keepends=False)`      Split at line boundaries
  `partition(sep)`                  Split at first separator into 3 parts
  `rpartition(sep)`                 Split at last separator into 3 parts

```python
text = "red,green,blue"
print(text.split(","))  # ['red', 'green', 'blue']

text = "one two three four"
print(text.split(" ", 2))  # ['one', 'two', 'three four']
print(text.rsplit(" ", 2)) # ['one two', 'three', 'four']
```

When `sep` is omitted, `split()` treats runs of whitespace as one
separator and ignores leading/trailing whitespace:

```python
text = "  red   green blue  "
print(text.split())  # ['red', 'green', 'blue']
```

When a separator is explicitly supplied, empty fields can appear:

```python
print("a,,b,".split(","))  # ['a', '', 'b', '']
```

Split lines:

```python
text = "first\nsecond\r\nthird"
print(text.splitlines())
```

Keep line endings:

```python
print("A\nB\n".splitlines(keepends=True))  # ['A\n', 'B\n']
```

Partition:

```python
email = "student@example.com"
print(email.partition("@"))
# ('student', '@', 'example.com')
```

If the separator is absent, `partition()` still returns a 3-item tuple:

```python
print("hello".partition("@"))  # ('hello', '', '')
```

### 9.5 Joining

`join()` combines an iterable of strings using the string before the dot
as the separator.

```python
words = ["Python", "is", "easy"]
print(" ".join(words))   # Python is easy
print("-".join(words))   # Python-is-easy
print("".join(words))    # Pythoniseasy
```

All elements must be strings:

```python
values = ["Age", "18"]
print(": ".join(values))
```

Convert non-string values first:

```python
numbers = [10, 20, 30]
result = ", ".join(map(str, numbers))
print(result)  # 10, 20, 30
```

### 9.6 Removing whitespace and trimming

  Method                 Purpose
  ---------------------- -------------------------------------------
  `strip(chars=None)`    Remove matching characters from both ends
  `lstrip(chars=None)`   Remove matching characters from the left
  `rstrip(chars=None)`   Remove matching characters from the right

```python
text = "   Python   "
print(text.strip())   # 'Python'
print(text.lstrip())  # 'Python   '
print(text.rstrip())  # '   Python'
```

The optional argument is a **set of characters**, not a literal
substring:

```python
print("www.example.com".strip("w.com"))  # 'example'
```

To remove an exact prefix or suffix, use:

```python
filename = "unwanted_report.txt"
print(filename.removeprefix("unwanted_"))  # report.txt
print(filename.removesuffix(".txt"))       # unwanted_report
```

`removeprefix()` and `removesuffix()` were added in Python 3.9.

### 9.7 Character classification methods

These return `True` or `False`.

  -----------------------------------------------------------------------
  Method                              Returns `True` when...
  ----------------------------------- -----------------------------------
  `isalpha()`                         All characters are alphabetic and
                                      string is non-empty

  `isalnum()`                         All characters are letters or
                                      digits and string is non-empty

  `isdigit()`                         All characters are digits and
                                      string is non-empty

  `isdecimal()`                       All characters are decimal
                                      characters and string is non-empty

  `isnumeric()`                       All characters are numeric and
                                      string is non-empty

  `isascii()`                         All characters are ASCII; empty
                                      string also returns `True`

  `islower()`                         At least one cased character exists
                                      and all cased characters are
                                      lowercase

  `isupper()`                         At least one cased character exists
                                      and all cased characters are
                                      uppercase

  `istitle()`                         String follows title-case rules

  `isspace()`                         All characters are whitespace and
                                      string is non-empty

  `isidentifier()`                    String is a valid Python identifier

  `isprintable()`                     All characters are printable; empty
                                      string also returns `True`
  -----------------------------------------------------------------------

Examples:

```python
print("Python".isalpha())       # True
print("Python3".isalnum())      # True
print("12345".isdigit())        # True
print("123".isdecimal())        # True
print("½".isnumeric())          # True
print("Hello".isascii())        # True
print("python".islower())       # True
print("PYTHON".isupper())       # True
print("Hello World".istitle())  # True
print("   ".isspace())          # True
print("student_name".isidentifier())  # True
print("Hello\n".isprintable())  # False
```

#### `isdecimal()` vs `isdigit()` vs `isnumeric()`

These methods are not identical:

-   `isdecimal()` is the narrowest: decimal digits such as `0` to `9`
    and other Unicode decimal digits.
-   `isdigit()` includes decimal digits and some additional digit
    characters, such as superscript digits.
-   `isnumeric()` is broadest and includes numeric characters such as
    fractions.

```python
print("5".isdecimal(), "5".isdigit(), "5".isnumeric())
print("²".isdecimal(), "²".isdigit(), "²".isnumeric())
print("½".isdecimal(), "½".isdigit(), "½".isnumeric())
```

For ordinary user-entered base-10 integer text, `isdecimal()` is often a
useful check, but conversion with `int()` is the definitive test for
whether a string can be parsed as an integer.

### 9.8 Alignment and padding methods

  Method                          Purpose
  ------------------------------- --------------------------------------------------
  `center(width, fillchar=' ')`   Center text
  `ljust(width, fillchar=' ')`    Left-align text
  `rjust(width, fillchar=' ')`    Right-align text
  `zfill(width)`                  Pad numeric-looking text on the left with zeroes

```python
text = "Python"

print(text.center(12, "-"))  # ---Python---
print(text.ljust(10, "."))   # Python....
print(text.rjust(10, "."))   # ....Python
print("42".zfill(5))         # 00042
print("-42".zfill(5))        # -0042
```

The fill character must be exactly one character.

### 9.9 Tab expansion

`expandtabs(tabsize=8)` replaces tab characters with spaces.

```python
text = "Name\tAge"
print(text.expandtabs(4))
```

### 9.10 Formatting method

`format()` inserts values into replacement fields.

```python
print("My name is {} and I am {}.".format("Raghuram", 18))
print("{name} scored {mark}.".format(name="Raghu", mark=95))
print("{:.2f}".format(3.14159))  # 3.14
```

### 9.11 Encoding

`encode(encoding='utf-8', errors='strict')` converts a string to bytes.

```python
text = "Hello"
data = text.encode("utf-8")
print(data)          # b'Hello'
print(type(data))    # <class 'bytes'>
```

### 9.12 Method inventory

For quick lookup, the main built-in `str` methods are:

```text
capitalize       casefold         center
count            encode           endswith
expandtabs       find             format
format_map       index            isalnum
isalpha          isascii          isdecimal
isdigit          isidentifier     islower
isnumeric        isprintable      isspace
istitle          isupper          join
ljust            lower            lstrip
maketrans        partition        removeprefix
removesuffix     replace          rfind
rindex           rjust            rpartition
rsplit           rstrip           split
splitlines       startswith       strip
swapcase         title            translate
upper            zfill
```

------------------------------------------------------------------------

## 10. ✅ Character checks and validation

### Check whether a string contains only letters

```python
text = input("Enter text: ")

if text.isalpha():
    print("Only alphabetic characters")
else:
    print("Contains other characters or is empty")
```

Spaces make `isalpha()` return `False`:

```python
print("Hello World".isalpha())  # False
```

To allow spaces:

```python
text = "Hello World"
if all(ch.isalpha() or ch.isspace() for ch in text):
    print("Letters and spaces only")
```

### Check whether a string contains only digits

```python
text = input("Enter digits: ")

if text.isdecimal():
    print("Decimal digits only")
else:
    print("Not decimal digits only")
```

### Check for uppercase and lowercase

```python
text = "HelloPython"

has_upper = any(ch.isupper() for ch in text)
has_lower = any(ch.islower() for ch in text)

print(has_upper)
print(has_lower)
```

### Simple username validation

```python
username = input("Username: ")

if username.isidentifier() and not username[0].isdigit():
    print("Looks like a valid Python-style identifier")
else:
    print("Invalid identifier")
```

This checks Python identifier rules, not every website's username rules.
Real applications should define their own length and character
requirements.

------------------------------------------------------------------------

## 11. 🔎 Searching and counting

### Find a character

```python
text = "programming"
character = "g"

position = text.find(character)
print(position)  # 3
```

### Count a character

```python
text = "programming"
print(text.count("m"))  # 2
```

### Count vowels

```python
text = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Vowels:", count)
```

### Count each character

```python
text = "banana"

for ch in text:
    if text.index(ch) == text.find(ch):
        print(ch, text.count(ch))
```

The previous example is simple but repeats searches. A dictionary is
more efficient for larger strings:

```python
text = "banana"
frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print(frequency)  # {'b': 1, 'a': 3, 'n': 2}
```

------------------------------------------------------------------------

## 12. 🔁 Replacing, splitting, and joining

### Replace spaces with hyphens

```python
text = "Python is very useful"
result = text.replace(" ", "-")
print(result)  # Python-is-very-useful
```

### Split a sentence into words

```python
sentence = "Python is easy to learn"
words = sentence.split()

for word in words:
    print(word)
```

### Join words into a sentence

```python
words = ["Python", "is", "powerful"]
sentence = " ".join(words)
print(sentence)
```

### Extract filename extension

```python
filename = "notes.txt"
name, separator, extension = filename.rpartition(".")

print(name)       # notes
print(extension)  # txt
```

For robust filesystem path handling, prefer the `pathlib` module rather
than manually splitting paths.

------------------------------------------------------------------------

## 13. 🧹 Removing whitespace and trimming

Input often contains unwanted spaces or newlines.

```python
name = input("Enter your name: ").strip()
print("Hello", name)
```

Remove only newline characters:

```python
line = "Python\n"
print(line.rstrip("\n"))
```

Remove a known prefix and suffix:

```python
url = "https://example.com"
url = url.removeprefix("https://")
print(url)
```

Remember: `strip("abc")` removes any combination of `a`, `b`, and `c`
from both ends; it does not remove the exact text `"abc"` as a unit.

------------------------------------------------------------------------

## 14. 🎨 String formatting

Formatting makes it easier to insert values into text.

### 14.1 f-strings (recommended for most modern Python code)

```python
name = "Raghuram"
age = 18

print(f"My name is {name} and I am {age} years old.")
```

Expressions are allowed:

```python
a = 10
b = 20
print(f"Sum = {a + b}")
```

Number formatting:

```python
price = 1234.5678
print(f"{price:.2f}")       # 1234.57
print(f"{price:,.2f}")      # 1,234.57
print(f"{0.25:.1%}")        # 25.0%
print(f"{42:05d}")          # 00042
```

Alignment:

```python
name = "Python"
print(f"|{name:<10}|")  # left
print(f"|{name:>10}|")  # right
print(f"|{name:^10}|")  # center
```

Debug-style output:

```python
score = 95
print(f"{score=}")  # score=95
```

### 14.2 `str.format()`

```python
print("Hello, {}!".format("Raghuram"))
print("{0} studies {1}".format("Raghuram", "Python"))
print("{name} is {age}".format(name="Raghu", age=18))
```

### 14.3 Percent formatting (older style)

```python
name = "Raghuram"
score = 95.5

print("Name: %s, Score: %.1f" % (name, score))
```

Prefer f-strings for new code unless maintaining older code.

------------------------------------------------------------------------

## 15. 🌍 Unicode, characters, and encoding

Python strings are Unicode text. A `str` is not the same thing as a
sequence of raw bytes.

```python
text = "Hello 😊"
print(type(text))  # <class 'str'>
```

### 15.1 Character count is not always visual-character count

`len()` counts Unicode code points, not necessarily what a person
perceives as one displayed character. Some visible symbols are made from
multiple code points (for example, a letter plus a combining accent, or
a joined emoji sequence).

```python
print(len("é"))
print(len("e\u0301"))
```

These may look similar but have different underlying representations.

### 15.2 Normalize Unicode

The `unicodedata` module can normalize equivalent Unicode sequences.

```python
import unicodedata

text1 = "é"
text2 = "e\u0301"

print(text1 == text2)  # False in this example

normalized1 = unicodedata.normalize("NFC", text1)
normalized2 = unicodedata.normalize("NFC", text2)

print(normalized1 == normalized2)  # True
```

### 15.3 Encode: string to bytes

```python
text = "Hello 😊"
encoded = text.encode("utf-8")

print(encoded)
print(type(encoded))  # <class 'bytes'>
```

### 15.4 Decode: bytes to string

```python
encoded = b"Hello"
decoded = encoded.decode("utf-8")

print(decoded)
print(type(decoded))  # <class 'str'>
```

### 15.5 Encoding errors

```python
text = "café"
encoded = text.encode("ascii", errors="replace")
print(encoded)
```

Use UTF-8 for most modern text files and network data unless a format
specifies another encoding.

------------------------------------------------------------------------

## 16. ⚖️ Comparing strings and sorting

### Case-sensitive comparison

```python
print("Apple" == "apple")  # False
```

### Case-insensitive comparison

```python
a = "PYTHON"
b = "python"

print(a.casefold() == b.casefold())  # True
```

### Sort characters

```python
text = "dcba"
result = "".join(sorted(text))
print(result)  # abcd
```

### Sort words

```python
words = ["banana", "Apple", "cherry"]
print(sorted(words))
print(sorted(words, key=str.casefold))
```

Python's default ordering is based on Unicode code points, not
dictionary or language-specific alphabetical rules.

------------------------------------------------------------------------

## 17. 🔄 Iterating through strings

### Iterate over characters

```python
text = "Python"

for ch in text:
    print(ch)
```

### Iterate using indexes

```python
text = "Python"

for i in range(len(text)):
    print(i, text[i])
```

### Use `enumerate()` (usually cleaner)

```python
text = "Python"

for index, ch in enumerate(text):
    print(index, ch)
```

### Iterate backwards

```python
text = "Python"

for ch in reversed(text):
    print(ch)
```

------------------------------------------------------------------------

## 18. 💻 Common string programs and patterns

Each example includes a straightforward solution. Try to understand the
logic and trace the loop before memorizing code.

### 18.1 Reverse a string

Using slicing:

```python
text = input("Enter a string: ")
print(text[::-1])
```

Without slicing:

```python
text = input("Enter a string: ")
reversed_text = ""

for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

print(reversed_text)
```

### 18.2 Check palindrome

A palindrome reads the same forward and backward.

```python
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
```

Ignore spaces and letter case:

```python
text = input("Enter a string: ")
cleaned = "".join(ch.casefold() for ch in text if ch.isalnum())

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
```

### 18.3 Count vowels and consonants

```python
text = input("Enter a string: ").lower()
vowels = 0
consonants = 0

for ch in text:
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
```

### 18.4 Count letters, digits, spaces, and special characters

```python
text = input("Enter a string: ")

letters = digits = spaces = special = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdecimal():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

print("Letters:", letters)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)
```

### 18.5 Remove duplicate characters while preserving order

```python
text = input("Enter a string: ")
result = ""

for ch in text:
    if ch not in result:
        result += ch

print(result)
```

For better performance on longer strings:

```python
text = input("Enter a string: ")
seen = set()
result = []

for ch in text:
    if ch not in seen:
        seen.add(ch)
        result.append(ch)

print("".join(result))
```

### 18.6 Print duplicate characters

```python
text = input("Enter a string: ")
seen = set()
duplicates = set()

for ch in text:
    if ch in seen:
        duplicates.add(ch)
    else:
        seen.add(ch)

if duplicates:
    print("Duplicate characters:", "".join(sorted(duplicates)))
else:
    print("No duplicate characters")
```

### 18.7 First non-repeating character

```python
text = input("Enter a string: ")

for ch in text:
    if text.count(ch) == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No non-repeating character")
```

This direct version is easy to understand but can be slow for long
strings because `count()` scans the string repeatedly. A frequency
dictionary is more efficient:

```python
text = input("Enter a string: ")
frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in text:
    if frequency[ch] == 1:
        print(ch)
        break
else:
    print("No non-repeating character")
```

### 18.8 Character frequency

```python
text = input("Enter a string: ")
frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch, count in frequency.items():
    print(ch, ":", count)
```

### 18.9 Check whether two strings are anagrams

Anagrams contain the same characters with the same frequencies.

```python
a = input("First string: ").replace(" ", "").casefold()
b = input("Second string: ").replace(" ", "").casefold()

if sorted(a) == sorted(b):
    print("Anagrams")
else:
    print("Not anagrams")
```

### 18.10 Count words

```python
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Word count:", len(words))
```

### 18.11 Reverse each word

```python
sentence = input("Enter a sentence: ")
words = sentence.split()

result = []

for word in words:
    result.append(word[::-1])

print(" ".join(result))
```

### 18.12 Reverse word order

```python
sentence = input("Enter a sentence: ")
words = sentence.split()
print(" ".join(words[::-1]))
```

### 18.13 Find the longest word

```python
sentence = input("Enter a sentence: ")
words = sentence.split()

if words:
    longest = max(words, key=len)
    print("Longest word:", longest)
else:
    print("No words entered")
```

### 18.14 Check whether a string is a pangram

A pangram contains every English letter from `a` to `z` at least once.

```python
text = input("Enter a sentence: ").casefold()
alphabet = set("abcdefghijklmnopqrstuvwxyz")

if alphabet.issubset(set(text)):
    print("Pangram")
else:
    print("Not a pangram")
```

### 18.15 Toggle the case of each character

```python
text = input("Enter a string: ")
print(text.swapcase())
```

### 18.16 Remove all spaces

```python
text = input("Enter a string: ")
print(text.replace(" ", ""))
```

Remove all whitespace characters, including tabs and newlines:

```python
text = input("Enter a string: ")
result = "".join(ch for ch in text if not ch.isspace())
print(result)
```

### 18.17 Check whether a string contains only unique characters

```python
text = input("Enter a string: ")

if len(text) == len(set(text)):
    print("All characters are unique")
else:
    print("Repeated characters found")
```

### 18.18 Find the most frequent character

```python
text = input("Enter a string: ")

if text:
    frequency = {}

    for ch in text:
        frequency[ch] = frequency.get(ch, 0) + 1

    most_common = max(frequency, key=frequency.get)
    print(most_common, frequency[most_common])
else:
    print("Empty string")
```

If multiple characters tie for the highest frequency, `max()` returns
the first key encountered among tied values.

### 18.19 Check whether a string starts and ends with the same character

```python
text = input("Enter a string: ")

if len(text) > 0 and text[0] == text[-1]:
    print("Same starting and ending character")
else:
    print("Different characters or empty string")
```

### 18.20 Remove punctuation

```python
import string

text = "Hello, Python! How are you?"
result = ""

for ch in text:
    if ch not in string.punctuation:
        result += ch

print(result)
```

This uses the ASCII punctuation set from the `string` module. For
broader Unicode punctuation, use `unicodedata.category()`.

------------------------------------------------------------------------

## 19. 🧬 Regular expressions

The `re` module is not a string method, but it is commonly used for
searching, validating, and replacing text with patterns.

```python
import re
```

### 19.1 `re.search()`

Finds the first match anywhere in the string.

```python
text = "My number is 9876543210"
match = re.search(r"\d+", text)

if match:
    print(match.group())  # 9876543210
```

### 19.2 `re.findall()`

Returns all non-overlapping matches in a list.

```python
text = "I have 12 apples and 5 oranges"
print(re.findall(r"\d+", text))  # ['12', '5']
```

### 19.3 `re.sub()`

Replaces matches.

```python
text = "My phone is 9876543210"
print(re.sub(r"\d", "*", text))
```

### 19.4 `re.split()`

Splits using a regular-expression pattern.

```python
text = "apple, banana; orange"
print(re.split(r"[,;]\s*", text))
```

### 19.5 Common regex symbols

  Pattern    Meaning
  ---------- ---------------------------------------------
  `.`        Any character except newline by default
  `\\d`      Digit
  `\\D`      Non-digit
  `\\w`      Word character
  `\\W`      Non-word character
  `\\s`      Whitespace
  `\\S`      Non-whitespace
  `^`        Start of string (or line in multiline mode)
  `$`        End of string (or line in multiline mode)
  `*`        Zero or more repetitions
  `+`        One or more repetitions
  `?`        Zero or one repetition
  `{m,n}`    Between `m` and `n` repetitions
  `[abc]`    One character from the set
  `[^abc]`   One character not in the set
  `( )`      Capturing group
  `|`        Alternation (OR)

Use raw strings such as `r"\d+"` for regex patterns to avoid unnecessary
backslash escaping.

For complicated input validation, a regular expression may help, but it
should not replace proper parsing or application-specific validation.

------------------------------------------------------------------------

## 20. ⚠️ Common mistakes

### Mistake 1: Trying to modify a character by index

```python
text = "Python"
# text[0] = "J"  # TypeError
text = "J" + text[1:]
```

### Mistake 2: Forgetting that `input()` returns a string

```python
age = input("Age: ")
# print(age + 1)  # TypeError
age = int(age)
print(age + 1)
```

### Mistake 3: Using `find()` as if it raises an error

```python
position = "Python".find("z")
print(position)  # -1
```

Use `index()` if you specifically want a `ValueError` when the substring
is absent.

### Mistake 4: Confusing `strip()` with `replace()`

```python
text = "  hello  "
print(text.strip())  # hello
```

`strip()` only removes characters at the ends. It does not remove spaces
from the middle.

### Mistake 5: Confusing `split()` and `join()`

```python
"a b c".split()          # makes a list
" ".join(["a", "b", "c"])  # makes a string
```

### Mistake 6: Forgetting case sensitivity

```python
print("Python" == "python")  # False
```

Use `lower()` or `casefold()` when case-insensitive matching is
required.

### Mistake 7: Calling a method without parentheses

```python
text = "python"
print(text.upper)    # method object, not converted text
print(text.upper())  # PYTHON
```

### Mistake 8: Joining numbers directly

```python
numbers = [1, 2, 3]
print(", ".join(map(str, numbers)))
```

### Mistake 9: Assuming `len()` counts visible emoji as one

Some displayed symbols contain multiple Unicode code points. `len()`
counts code points, not grapheme clusters.

### Mistake 10: Repeated concatenation in a large loop

For many pieces, collect them in a list and call `"".join(parts)` rather
than repeatedly creating longer strings.

------------------------------------------------------------------------

## 21. ⏱️ Time and space considerations

Let `n` be the length of a string.

  -----------------------------------------------------------------------
  Operation                                                  Typical time
  ------------------------------ ----------------------------------------
  `len(text)`                                                        O(1)

  `text[i]`                                                          O(1)

  `text[a:b]`                            O(k), where `k` is result length

  `sub in text`                                           O(n) worst case

  `text.find(sub)`               O(n) worst case for a fixed-size pattern
                                        in a simple model; implementation
                                                             details vary

  `text.count(sub)`                                                  O(n)

  `text.lower()` / `upper()`                                         O(n)

  `text.replace(old, new)`                             O(n + output size)

  `text.split()`                              O(n) plus output allocation

  `"separator".join(parts)`                        O(total output length)

  `sorted(text)`                                               O(n log n)
  -----------------------------------------------------------------------

These are useful high-level expectations, not strict guarantees for
every implementation or input.

Because strings are immutable, concatenating repeatedly in a loop can
create many temporary strings. Prefer:

```python
parts = []

for i in range(5):
    parts.append(str(i))

result = "".join(parts)
print(result)  # 01234
```

------------------------------------------------------------------------

## 22. 📌 Quick reference

### Most-used built-ins

  Function         Example                      Result / purpose
  ---------------- ---------------------------- -----------------------
  `len(s)`         `len("Python")`              `6`
  `str(x)`         `str(123)`                   `"123"`
  `ord(c)`         `ord("A")`                   `65`
  `chr(n)`         `chr(65)`                    `"A"`
  `repr(s)`        `repr("a\nb")`               Debug representation
  `sorted(s)`      `sorted("cba")`              `['a', 'b', 'c']`
  `reversed(s)`    `"".join(reversed("abc"))`   `"cba"`
  `min(s)`         `min("cab")`                 `"a"`
  `max(s)`         `max("cab")`                 `"c"`
  `enumerate(s)`   `enumerate("abc")`           Index-character pairs

### Most-used string methods

  Need                        Use
  --------------------------- ---------------------------------
  Uppercase                   `s.upper()`
  Lowercase                   `s.lower()`
  Case-insensitive matching   `s.casefold()`
  Remove outside whitespace   `s.strip()`
  Search without exception    `s.find(sub)`
  Search with exception       `s.index(sub)`
  Count occurrences           `s.count(sub)`
  Replace text                `s.replace(old, new)`
  Split into words            `s.split()`
  Join a list                 `" ".join(items)`
  Check letters               `s.isalpha()`
  Check digits                `s.isdecimal()` / `s.isdigit()`
  Check letters or digits     `s.isalnum()`
  Check whitespace            `s.isspace()`
  Check prefix                `s.startswith(prefix)`
  Check suffix                `s.endswith(suffix)`
  Reverse                     `s[::-1]`
  Remove exact prefix         `s.removeprefix(prefix)`
  Remove exact suffix         `s.removesuffix(suffix)`
  Format values               `f"{value}"`

------------------------------------------------------------------------

## 23. 🏆 Practice questions

Complete the following 25 string problems in order. The question numbers continue from 51 to 75 in the learning tracker.

| Question No | Problem | Difficulty | Topic | Status | Completed On | Revision | Notes |
|---:|---|---|---|---|---|---|---|
| 51 | Reverse a string using a loop | Easy | Strings | Not Done | | | |
| 52 | Check string palindrome | Easy | Strings | Not Done | | | |
| 53 | Count vowels and consonants | Easy | Strings | Not Done | | | |
| 54 | Count uppercase and lowercase letters | Easy | Strings | Not Done | | | |
| 55 | Count words in a sentence | Easy | Strings | Not Done | | | |
| 56 | Toggle character case | Easy | Strings | Not Done | | | |
| 57 | Capitalize each word | Easy | Strings | Not Done | | | |
| 58 | Reverse word order in a sentence | Easy | Strings | Not Done | | | |
| 59 | Reverse each word | Easy | Strings | Not Done | | | |
| 60 | Frequency of each character | Easy | Strings | Not Done | | | |
| 61 | First non-repeating character | Easy | Strings | Not Done | | | |
| 62 | Remove duplicate characters preserving order | Easy | Strings | Not Done | | | |
| 63 | Find duplicate characters | Easy | Strings | Not Done | | | |
| 64 | Check anagrams | Easy | Strings | Not Done | | | |
| 65 | Check pangram | Easy | Strings | Not Done | | | |
| 66 | Longest word in a sentence | Easy | Strings | Not Done | | | |
| 67 | Most frequent character | Easy | Strings | Not Done | | | |
| 68 | Count substring occurrences | Easy | Strings | Not Done | | | |
| 69 | Check string rotation | Easy | Strings | Not Done | | | |
| 70 | Longest common prefix | Easy | Strings | Not Done | | | |
| 71 | Basic email validation | Easy | Strings | Not Done | | | |
| 72 | Run-length string compression | Easy | Strings | Not Done | | | |
| 73 | Caesar cipher encoder | Easy | Strings | Not Done | | | |
| 74 | Check balanced parentheses | Easy | Strings | Not Done | | | |
| 75 | Word-frequency counter | Easy | Strings | Not Done | | | |

### 🔧 Extra study tools — quick practice routine

- 🧪 **Experiment:** Change the input in every example and predict the output.
- 🐞 **Debug:** Use `print(repr(text))` to reveal hidden spaces, tabs and newline characters.
- ⏱️ **Improve:** Compare a simple loop solution with a solution using built-in methods.
- 🧠 **Explain:** For each method, describe its input, return value and whether it changes the original string.
- 🏁 **Review:** Revisit questions you found difficult and record the date in the practice table.

---

## 🎉 Final notes

-   A string is an immutable Unicode sequence.
-   Indexing gets one character; slicing gets a portion.
-   Built-in functions such as `len()`, `str()`, `ord()`, and `chr()`
    are called directly.
-   String methods such as `upper()`, `split()`, and `replace()` are
    called using dot notation.
-   `split()` creates a list; `join()` creates a string.
-   `find()` returns `-1` when it cannot find a substring; `index()`
    raises `ValueError`.
-   Use f-strings for readable modern formatting.
-   Use UTF-8 for most text encoding needs.
-   Practise writing loops and solving small problems to build strong
    string-handling skills.
