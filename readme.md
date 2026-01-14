# Caesar Cipher CLI 🔐

A simple command-line **Caesar Cipher** encoder/decoder written in Python.  
You can encrypt and decrypt messages by shifting letters in the alphabet.

---

## 🧠 What is a Caesar Cipher?

The **Caesar Cipher** is one of the oldest and simplest encryption techniques.  
Each letter in the message is shifted by a fixed number of positions in the alphabet.

For example, with a shift of `3`:

- `a` → `d`
- `b` → `e`
- `z` → `c` (it wraps around the alphabet)

This program lets you:
- **Encode** (encrypt) a message
- **Decode** (decrypt) a message
- Keep using the tool in a loop until you choose to exit

---

## 📁 Project Structure

```text
.
├── caesar_cipher.py   # Main Python script (your code)
└── README.md          # Project documentation
You can rename the Python file to whatever you like (e.g. main.py), just update the examples below accordingly.

⚙️ Requirements
Python 3.x

You can check your Python version with:

bash
Copy code
python --version
# or
python3 --version
🚀 How to Run
Clone or download this repository.

Open a terminal in the project folder.

Run the script:

bash
Copy code
python caesar_cipher.py
# or
python3 caesar_cipher.py
🕹️ Usage
When you run the program, it will:

Show an ASCII art logo.

Ask you whether you want to encode or decode:

text
Copy code
Type 'encode' to encrypt, type 'decode' to decrypt:
Ask for the message:

text
Copy code
Type your message:
Ask for the shift number:

text
Copy code
Type the shift number:
Print the result:

text
Copy code
The encoded text is: ...
Ask if you want to go again:

text
Copy code
Type 'yes' if you want to go again. Otherwise type 'no'.
💡 Example
text
Copy code
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
5
The encoded text is: mjqqt btwqi
Type 'yes' if you want to go again. Otherwise type 'no'.
no
🧩 How It Works (Logic Overview)
The alphabet is stored as a Python list:

python
Copy code
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
For each character in the input text:

If it’s in alphabet, the program:

Finds its index: position = alphabet.index(char)

Calculates a new position using modular arithmetic:

Encode: new_position = (position + shift) % len(alphabet)

Decode: new_position = (position - shift) % len(alphabet)

Adds the new letter to the result string.

If it’s not in alphabet (like spaces, numbers, punctuation), it is added unchanged.

The modulo (%) with len(alphabet) (which is 26) makes sure the index wraps around so z can go back to a when needed.

🛠️ Customization Ideas
You can extend this project by:

Allowing uppercase letters

Supporting Unicode / non-English alphabets

Automatically handling very large shift values

Adding unit tests for caser_cypher() function

Turning it into a simple GUI app or a web app

📜 License
This project is free to use, modify, and learn from.
You can add an official license (like MIT) here if you want.