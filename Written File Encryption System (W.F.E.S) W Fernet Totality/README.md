# W.R.E.D - File Encryption System

**W.R.E.D** (Write, Read, Encrypt, Decrypt) is a simple Python-based command-line interface (CLI) tool for basic file encryption, decryption, reading, writing, and hash generation using Fernet symmetric encryption.

> ⚠️ This is a personal educational project and not intended for production use or securing highly sensitive data. It does **not** support filetypes other than `.txt` and cannot encrypt binaries or executables.

---

## Features

- 🔐 Encrypt and decrypt `.txt` files using a password-based Fernet key.
- 🧾 Read and write plaintext files directly from the CLI.
- 🗑️ Delete files securely.
- 🔁 Decrypt a file temporarily and re-encrypt it automatically after 10 seconds.
- 🔑 Generate secure base64 keys from passwords using PBKDF2.

---

## Requirements

- Python 3.7+
- `cryptography` library

You can install the required packages using:

```bash
pip install -r requirements.txt
