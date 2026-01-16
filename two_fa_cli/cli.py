import argparse
import getpass
import sys

from .storage import load_db, save_db
from .totp import generate_totp
from . import __version__


def main():
    parser = argparse.ArgumentParser(
        prog="2fa-cli", description="Secure, offline 2FA TOTP CLI tool"
    )

    subparsers = parser.add_subparsers(dest="command")

    # add
    add = subparsers.add_parser("add", help="Add a new 2FA secret")
    add.add_argument("--name", required=True, help="Alias name")
    add.add_argument("--key", required=True, help="Base32 secret key")

    # code
    code = subparsers.add_parser("code", help="Generate OTP")
    code.add_argument("name", help="Alias name")

    # list
    subparsers.add_parser("list", help="List saved aliases")

    # remove
    remove = subparsers.add_parser("remove", help="Remove a secret")
    remove.add_argument("name", help="Alias name")
    # version
    subparsers.add_parser("version", help="Show version")

    args = parser.parse_args()

    if args.command == "version":
        print(__version__)
        sys.exit(0)

    if not args.command:
        parser.print_help()
        sys.exit(0)

    from getpass import getpass
    password = getpass("Master password: ")

    try:
        db = load_db(password)
    except Exception:
        print("❌ Invalid password or corrupted database")
        sys.exit(1)

    if args.command == "add":
        if args.name in db:
            print("❌ Name already exists")
            sys.exit(1)
        db[args.name] = args.key
        save_db(db, password)
        print("✅ Added successfully")

    elif args.command == "code":
        if args.name not in db:
            print("❌ No such entry")
            sys.exit(1)
        print(generate_totp(db[args.name]))

    elif args.command == "list":
        if not db:
            print("No entries found")
        for name in db:
            print(name)

    elif args.command == "remove":
        if args.name not in db:
            print("❌ No such entry")
            sys.exit(1)
        db.pop(args.name)
        save_db(db, password)
        print("✅ Removed")


if __name__ == "__main__":
    main()
