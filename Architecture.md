EchoCrypt Architecture Notes:
1. Core Logic: Implements a streaming XOR cipher using itertools.cycle for memory-efficient key repetition over arbitrary data lengths.
2. Unified I/O: Leverages binary streams (sys.stdin.buffer / sys.stdout.buffer) to ensure transparent handling of non-UTF8 binary data, preventing corruption during obfuscation.
3. Source Resolution: Employs a multi-modal ingestion strategy that treats the input positional argument dynamically as a file path, a stdin pipe, or a literal string.
4. Reversibility: Since (A ^ B) ^ B = A, the architecture utilizes the same logic path for both encryption and decryption, reducing codebase complexity.