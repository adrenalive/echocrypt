# EchoCrypt

EchoCrypt is a minimalist command-line utility for fast, reversible data obfuscation. It uses a cyclic XOR cipher keyed to a user-provided passphrase. It is perfect for "quick-look" privacy to hide sensitive strings or files from casual observation without the overhead of enterprise-grade encryption like GPG or AES.

## Features
- Obfuscate raw strings directly from the shell.
- Process binary or text files.
- Reversible: Applying the same key twice restores the original data.

## Installation
No dependencies required beyond Python 3.x standard library.

## Usage

### Obfuscate a string:
`python echocrypt.py "MySecretPassword123" -k "BlueMonkey"`

### Obfuscate a file:
`python echocrypt.py sensitive_data.pdf -f -k "MySecureKey" -o sensitive_data.crypt`

### De-obfuscate a file:
`python echocrypt.py sensitive_data.crypt -f -k "MySecureKey" -o restored_data.pdf`