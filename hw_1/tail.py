import sys

def tail_lines(lines, count):
    return lines[-count:]

def process_file(filename, count):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in tail_lines(lines, count):
                print(line.rstrip())
    except FileNotFoundError:
        print(f"tail: cannot open '{filename}' for reading: No such file", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        count = 10
        if len(sys.argv) > 2 and sys.argv[1].startswith('--lines='):
            count = int(sys.argv[1].split('=')[1])
            filenames = sys.argv[2:]
        else:
            filenames = sys.argv[1:]
        for i, filename in enumerate(filenames):
            if i > 0:
                print()
            if len(filenames) > 1:
                print(f"==> {filename} <==")
            process_file(filename, count)
    else:
        lines = sys.stdin.readlines()
        for line in tail_lines(lines, 17):
            print(line.rstrip())
