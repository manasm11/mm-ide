#!/usr/bin/python3
import pretty_errors
from sys import argv
import os


def test():
    os.system(f"python3 -m pytest tests " + " ".join(argv[2:]))


def setup_():
    project_name = input("Enter project name (mm-dummy) >> ")
    short_description = input("Enter short description >> ")
    with open("README.md") as reader:
        new_readme = reader.read().replace("mm-dummy", project_name)
    with open("README.md", "w") as writer:
        writer.write(new_readme)

    setup_path = os.path.join("mm-dummy", "setup.py")
    with open(setup_path) as reader:
        new_setup = (
            reader.read()
            .replace("mm-dummy", project_name)
            .replace("dummy-description", short_description)
        )
    with open(setup_path, "w") as writer:
        writer.write(new_setup)

    inner_package = os.path.join("mm-dummy", "mm-dummy")
    new_inner_package = os.path.join("mm-dummy", project_name)
    os.rename(inner_package, new_inner_package)
    os.rename("mm-dummy", project_name)


def help_():
    print(
        f"""
    USAGE: {argv[0]} [test|help|setup]
    """
    )


if __name__ == "__main__":
    if len(argv) > 1:
        {"test": test, "help": help_, "setup": setup_}.get(argv[1], help_)()
    else:
        help_()
