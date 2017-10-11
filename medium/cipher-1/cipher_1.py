text = input()
key = int(input())
cipher = ''

for char in text:
    if not char.isalnum():
        cipher += char
    elif char.isdigit():
        cipher += str((int(char) + key) % 10)
    elif char.isupper():
        char_num = ord(char) - 65 + key
        char_num = 65 + char_num % 26
        cipher += chr(char_num)
    elif char.islower():
        char_num = ord(char) - 97 + key
        char_num = 97 + char_num % 26
        cipher += chr(char_num)

print(cipher)
