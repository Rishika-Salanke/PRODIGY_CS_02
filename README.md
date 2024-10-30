This project is a simple yet effective command-line tool for encrypting and decrypting images using the XOR bitwise operation.
It demonstrates how basic encryption techniques can be applied to image files without using external libraries, 
making it a beginner-friendly approach to understanding encryption algorithms and file manipulation in Python.

Project Overview
Features
- **XOR Encryption:** The tool manipulates image data at the byte level using the XOR operation with a user-provided key, showcasing a foundational cryptographic technique.
- **Two Modes:**
  - **Encryption Mode:** Encrypts a selected image and saves the output with a prefixed filename.
  - **Decryption Mode:** Decrypts an XOR-encrypted image using the same key, reverting the image to its original form.

Installation
Clone this repository and ensure Python is installed on your system.

```bash
git clone https://github.com/yourusername/xor-image-encryption.git
cd xor-image-encryption
