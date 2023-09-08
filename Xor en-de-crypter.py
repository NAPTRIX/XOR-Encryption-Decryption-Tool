def xor_encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
    
    # Convert ciphertext to hexadecimal and enclose in double quotes
    hex_ciphertext = "".join([format(ord(c), '02x') for c in ciphertext])
    return f'"{hex_ciphertext}"'

def xor_decrypt(ciphertext, key):
    if len(key) == 0:
        return "Error: Key cannot be empty"
    
    # Remove double quotes if present and convert from hexadecimal
    ciphertext = ciphertext.strip('"')
    try:
        hex_ciphertext = bytes.fromhex(ciphertext).decode()
    except ValueError:
        return "Error: Invalid hexadecimal format"
    
    plaintext = ""
    for i in range(len(hex_ciphertext)):
        plaintext += chr(ord(hex_ciphertext[i]) ^ ord(key[i % len(key)]))
    return plaintext

def main():
    while True:
        print("\nChoose an option:")
        print("1. XOR Encrypt")
        print("2. XOR Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            key = input("Enter the key: ")
            encrypted_text = xor_encrypt(plaintext, key)
            print("Encrypted:", encrypted_text)
        
        elif choice == '2':
            ciphertext = input("Enter the ciphertext (enclosed in double quotes): ")
            key = input("Enter the key: ")
            decrypted_text = xor_decrypt(ciphertext, key)
            if "Error:" in decrypted_text:
                print(decrypted_text)
            else:
                print("Decrypted:", decrypted_text)
        
        elif choice == '3':
            print("Exiting the XOR encryption/decryption program.")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
