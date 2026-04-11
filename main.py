import argparse
import sys
import os

def xor_cipher(data, key):
    key_bytes = key.encode()
    return bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data)])

def main():
    parser = argparse.ArgumentParser(description='EchoCrypt: Reversible XOR Obfuscation Tool')
    parser.add_argument('source', help='The text string or file path to process')
    parser.add_argument('-k', '--key', required=True, help='Passphrase for the transformation')
    parser.add_argument('-f', '--file', action='store_true', help='Flag to treat source as a file path')
    parser.add_argument('-o', '--output', help='Output file path (optional)')
    
    args = parser.parse_args()

    try:
        if args.file:
            if not os.path.exists(args.source):
                print(f'Error: File {args.source} not found.')
                sys.exit(1)
            with open(args.source, 'rb') as f:
                content = f.read()
        else:
            content = args.source.encode()

        result = xor_cipher(content, args.key)

        if args.output:
            with open(args.output, 'wb') as f:
                f.write(result)
            print(f'Operation complete. Result saved to: {args.output}')
        else:
            if args.file:
                print(result)
            else:
                try:
                    # Try to decode for text output, otherwise print hex
                    print(result.decode('utf-8'))
                except UnicodeDecodeError:
                    print(result.hex())

    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()