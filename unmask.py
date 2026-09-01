#!/usr/bin/env python3
import argparse
import os
import subprocess
from os import mkdir


## SIDENOTE : YOU SHOULD RUN THIS AS ROOT.




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
    parser.add_argument(
        "-d",
        "--directory",
        required=False,
        help="To change unmask file directory. Default: '/etc/portage/package.unmask'"
    )

    return parser.parse_args()

def unmask_package(package,file_path:str="/etc/portage/package.unmask"):
    print(f"Starting unmasking process for: {package}")
    args=user_input()
    UNMASK_FILE ="/etc/portage/package.unmask" or  str(args.directory)
    if os.geteuid() != 0:
        print("Error: this script must be run as root.")
        return False
    try:
        parent_directory = os.path.dirname(file_path)
        if parent_directory:
            os.makedirs(parent_directory, exist_ok=True)
        with open(file_path, "a") as file:
            file.write(f"{package}\n")
        print(f"Successfully added {package} to {file_path}")
        return True
    except OSError as error:
        print(f"Error writing to {file_path}: {error}")
        return False

def main():
    args = user_input()
    unmask_package(args.package,args.directory)


if __name__ == "__main__":
    main()
