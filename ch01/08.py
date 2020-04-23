def cipher(str):
    new_str = ''
    for char in str:
        if char.isalnum():
            char = chr(219 - ord(char))
        new_str += char
    return new_str

print(cipher("Hello there"))
