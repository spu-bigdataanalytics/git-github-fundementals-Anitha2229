# Cryptography Techniques App

This is a Streamlit app that demonstrates simple text and file cryptography techniques.

## Features

The app provides two types of encryption and decryption techniques:

1. **Text Cryptography:** This includes simple methods like Caesar Cipher and ASCII conversion. Users can input a text, select an encryption method, and get the encrypted text. They can also decrypt the text by providing the encrypted text and the encryption method.

2. **File Cryptography:** This uses Fernet encryption provided by the cryptography library in Python. Users can upload an image, which the app will encrypt and provide the encrypted image along with a key for decryption. Users can also decrypt the image by providing the encrypted image and the key.

## Usage

1. Clone the repository:

   ```bash
   git clone (repo URL)
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```
   
