
s = input("Enter a string: ")
shift = int(input("Enter shift value: "))

result = ""

shift = shift % 26

for i in range(len(s)):
    ch = s[i]

    if 'A' <= ch <= 'Z':
        new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        result += new_char

    elif 'a' <= ch <= 'z':
        new_char = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        result += new_char

    else:
        result += ch

print("Encrypted string:", result)
