# Function to encrypt an image using XOR
def xor_encrypt(image_path, key):
    try:
        # Open the image file in binary read mode
        with open(image_path, 'rb') as f:
            image_data = bytearray(f.read())  # Read the image as bytes and convert to bytearray

        # Perform XOR encryption on each byte
        for index in range(len(image_data)):
            image_data[index] ^= key  # XOR operation with the key

        # Save the encrypted image
        encrypted_path = "encrypted_" + image_path
        with open(encrypted_path, 'wb') as f:
            f.write(image_data)
        
        print(f"Encryption Completed. Encrypted file saved as: {encrypted_path}")
    
    except Exception as e:
        print(f"Error occurred during encryption: {e}")

# Function to decrypt an image using XOR
def xor_decrypt(encrypted_image_path, key):
    try:
        # Open the encrypted image file in binary read mode
        with open(encrypted_image_path, 'rb') as f:
            encrypted_data = bytearray(f.read())  # Read the encrypted image as bytes and convert to bytearray

        # Perform XOR decryption (same as encryption process)
        for index in range(len(encrypted_data)):
            encrypted_data[index] ^= key  # XOR operation with the same key to decrypt

        # Save the decrypted image
        decrypted_path = "decrypted_" + encrypted_image_path
        with open(decrypted_path, 'wb') as f:
            f.write(encrypted_data)
        
        print(f"Decryption Completed. Decrypted file saved as: {decrypted_path}")
    
    except Exception as e:
        print(f"Error occurred during decryption: {e}")

# Main function to let the user choose encryption or decryption
def main():
    # Ask the user if they want to encrypt or decrypt
    choice = input("Do you want to encrypt or decrypt an image? (E/D): ").lower()

    if choice == 'e':
        # Encrypt mode
        image_path = input("Enter the path of the image to encrypt: ")
        key = int(input("Enter the XOR key for encryption: "))

        xor_encrypt(image_path, key)

    elif choice == 'd':
        # Decrypt mode
        encrypted_image_path = input("Enter the path of the image to decrypt: ")
        key = int(input("Enter the XOR key for decryption (must be the same as encryption key): "))

        xor_decrypt(encrypted_image_path, key)

    else:
        print("Invalid choice. Please choose 'E' for encryption or 'D' for decryption.")

# Run the program
if __name__ == "__main__":
    main()
