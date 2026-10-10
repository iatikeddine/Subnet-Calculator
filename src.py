from parsing import valid_cidr
import sys

if __name__ == "__main__":
    try:
        cidr = valid_cidr(sys.argv)
    except Exception as e:
        sys.exit(f"{e}")