# wordcount.py
import sys
from collections import Counter

def main():
    if len(sys.argv) < 2:
        print("Usage: python wordcount.py <filename>", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: file '{filepath}' not found.", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: permission denied for '{filepath}'.", file=sys.stderr)
        sys.exit(1)

    lines = text.splitlines()
    words = text.split()
    characters = len(text)

    print(f"Lines:      {len(lines)}")
    print(f"Words:      {len(words)}")
    print(f"Characters: {characters}")

    if words:
        lower_words = [w.lower().strip(".,;:!?\"'()[]{}") for w in words]
        lower_words = [w for w in lower_words if w]
        counter = Counter(lower_words)
        print("\nTop 5 most common words:")
        for word, count in counter.most_common(5):
            print(f"  {word}: {count}")

if __name__ == "__main__":
    main()
