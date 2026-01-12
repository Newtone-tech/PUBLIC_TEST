# Simple workflow smoke test: prints output then fails intentionally.

def main():
    print("workflow check: starting")
    # Intentional error to test error-handling paths.
    return 1 / 0


if __name__ == "__main__":
    main()
