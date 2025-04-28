import argparse

def main():
    # Capture a command-line argument and print it out to the console
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str, help="Name of the person to greet")
    args = parser.parse_args()

    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()
