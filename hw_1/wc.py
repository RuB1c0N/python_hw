import sys

def wc_stats(lines):
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    byte_count = sum(len(line.encode('utf-8')) for line in lines)
    return line_count, word_count, byte_count

def print_stats(filename, stats):
    print(f"{stats[0]:>7} {stats[1]:>7} {stats[2]:>7} {filename}")

if __name__ == "__main__":
    total_stats = [0, 0, 0]
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            try:
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    stats = wc_stats(lines)
                    print_stats(filename, stats)
                    total_stats = [sum(x) for x in zip(total_stats, stats)]
            except FileNotFoundError:
                print(f"wc: {filename}: No such file or directory", file=sys.stderr)
        if len(sys.argv) > 2:
            print_stats("total", total_stats)
    else:
        lines = sys.stdin.readlines()
        stats = wc_stats(lines)
        print_stats("", stats)