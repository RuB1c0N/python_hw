import sys

def number_lines(input_stream):
    for i, line in enumerate(input_stream, start=1):
        print(f"{i:6}  {line.rstrip()}")

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            filename = sys.argv[1]
            with open(filename, 'r') as file:
                number_lines(file)
        else:
            number_lines(sys.stdin)
    except FileNotFoundError:
        print(f"nl: {sys.argv[1]}: No such file or directory", file=sys.stderr)
