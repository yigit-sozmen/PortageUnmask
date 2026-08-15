#!/usr/bin/env python3
import argparse
import os
import subprocess
## SIDENOTE : YOU SHOULD RUN THIS AS ROOT.

UNMASK_FILE = "/etc/portage/package.unmask"


def user_input():
    parser = argparse.ArgumentParser(
        description="Automated Unmasking Tool for Gentoo Linux"
    )

    parser.add_argument(
        "-p",
        "--package",
        required=True,
        help="Package atom to unmask, e.g. =dev-python/foo-1.2.3"
    )

    return parser.parse_args()


def unmask_package(package):
    print(f"Starting unmasking process for: {package}")

    
    if os.geteuid() != 0:
        print("Error: this script must be run as root.")
        return False

    try:
        with open(UNMASK_FILE, "a") as file:
            file.write(f"{package}\n")

        print(f"Successfully added {package} to {UNMASK_FILE}")
        return True

    except OSError as error:
        print(f"Error writing to {UNMASK_FILE}: {error}")
        return False


def main():
    args = user_input()
    unmask_package(args.package)


if __name__ == "__main__":
    main()
