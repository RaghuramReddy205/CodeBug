
s = input("Enter parentheses: ")

stack = []
balanced = True

for ch in s:

    if ch == '(' or ch == '{' or ch == '[':
        stack.append(ch)

    elif ch == ')' or ch == '}' or ch == ']':

        if len(stack) == 0:
            balanced = False
            break

        top = stack.pop()

        if (ch == ')' and top != '(') or \
           (ch == '}' and top != '{') or \
           (ch == ']' and top != '['):

            balanced = False
            break

if len(stack) != 0:
    balanced = False

if balanced:
    print("Balanced Parentheses")
else:
    print("Not Balanced")
