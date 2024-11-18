import sys

def number_lines(input_stream):
    for i, line in enumerate(input_stream, start=1):
        print(f"{i}\t{line.rstrip()}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            number_lines(file)
    else:
        number_lines(sys.stdin)
