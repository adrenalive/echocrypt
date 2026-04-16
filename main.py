import argparse, sys, itertools, io, pathlib

def crypt_gen(stream, key, chunk_size=65536):
    """Generator that yields XOR-transformed chunks while preserving key alignment."""
    k_cycle = itertools.cycle(key.encode())
    while (chunk := stream.read(chunk_size)):
        yield bytes(b ^ next(k_cycle) for b in chunk)

def main():
    parser = argparse.ArgumentParser(description='EchoCrypt: Streaming XOR')
    parser.add_argument('src', nargs='?', default='-', help='File, string, or stdin')
    parser.add_argument('-k', '--key', required=True)
    parser.add_argument('-o', '--out')
    args = parser.parse_args()

    try:
        # Polymorphic source resolution
        if args.src == '-':
            src_stream = sys.stdin.buffer
        elif pathlib.Path(args.src).is_file():
            src_stream = open(args.src, 'rb')
        else:
            src_stream = io.BytesIO(args.src.encode())

        # Efficient output routing
        with (open(args.out, 'wb') if args.out else sys.stdout.buffer) as out_f:
            for chunk in crypt_gen(src_stream, args.key):
                out_f.write(chunk)
                
    except Exception as e:
        sys.stderr.write(f"[!] Fatal: {e}\n")
        sys.exit(1)

if __name__ == '__main__':
    main()