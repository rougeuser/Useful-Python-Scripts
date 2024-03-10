def vigenere_cipher(text, key, decrypt=False):
    key_len = len(key)
    encrypted_text = ''
    for i, char in enumerate(text):
        key_char = key[i % key_len]
        if char.isalpha():
            shift = ord(key_char.lower()) - ord('a')
            if decrypt:
                shift = -shift
            if char.islower():
                encrypted_text += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            elif char.isupper():
                encrypted_text += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

if __name__ == "__main__":
    text = input("Enter the text: ")
    key = input("Enter the key: ")
    choice = input("Encrypt or Decrypt? (e/d): ").lower()
    if choice == 'e':
        print("Encrypted Text:", vigenere_cipher(text, key))
    elif choice == 'd':
        print("Decrypted Text:", vigenere_cipher(text, key, decrypt=True))
    else:
        print("Invalid choice.")