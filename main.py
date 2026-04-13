import argparse, sys, os, itertools

def crypt(data: bytes, key: str) -> bytes:
    """Apply XOR transformation using a cycling key iterator."""
    return bytes(b ^ k for b, k in zip(data, itertools.cycle(key.encode())))

def main():
    parser = argparse.ArgumentParser(description='EchoCrypt: Reversible XOR Tool')
    parser.add_argument('source', nargs='?', default='-', help='File path, string, or stdin (-)')
    parser.add_argument('-k', '--key', required=True, help='Transformation key')
    parser.add_argument('-o', '--output', help='Output file path')
    args = parser.parse_args()

    try:
        # Scrappy source resolution: Check file, then stdin, then raw string
        if os.path.isfile(args.source):
            content = open(args.source, 'rb').read()
        elif args.source == '-':
            content = sys.stdin.buffer.read()
        else:
            content = args.source.encode()

        result = crypt(content, args.key)

        # Direct binary output to avoid encoding artifacts
        out = open(args.output, 'wb') if args.output else sys.stdout.buffer
        out.write(result)
    except Exception as e:
        sys.stderr.write(f"[!] Error: {e}\n")
        sys.exit(1)

if __name__ == '__main__':
    main()