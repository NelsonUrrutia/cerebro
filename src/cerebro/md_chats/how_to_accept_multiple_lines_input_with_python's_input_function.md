You can use the `input()` function in Python with some modifications to accept multiple lines of input. Here are a few ways:

**1. Using `raw_input()` (Python 2.x)**

In Python 2.x, you can use `raw_input()` instead of `input()`. It will return a string that includes all the lines entered by the user.

```python
user_input = raw_input("Enter multiple lines: ")
print(user_input)
```

**2. Using `input()` with triple quotes (Python 3.x)**

In Python 3.x, you can use triple quotes (`"""..."""`) to enter multiple lines of input.

```python
user_input = """Enter multiple lines:
Line 1
Line 2
"""
print(user_input)
```

**3. Using `input()` with a loop**

You can also use a loop to continuously ask for user input until they are done entering text.

```python
lines = []
while True:
    line = input("Enter a line (or 'done' to finish): ")
    if line.lower() == 'done':
        break
    lines.append(line)

print("\n".join(lines))
```

**4. Using `input()` with a multiline string**

You can also use a multiline string with the `input()` function, but you need to press Enter twice to insert a newline character.

```python
user_input = input("Enter multiple lines:\n")
# Press Enter twice here
# This will result in a string like this:
# "Line 1\nLine 2"
print(user_input)
```

Remember that `input()` always returns a string, so you might need to use additional functions (like `splitlines()`) if you want to work with the input as separate lines.