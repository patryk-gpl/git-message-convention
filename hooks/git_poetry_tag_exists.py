#!/usr/bin/env python3

import subprocess
import sys

import toml


def get_latest_git_tag():
    try:
        tags = (
            subprocess.check_output(["git", "tag", "--sort=-committerdate"])
            .decode()
            .splitlines()
        )
        return tags[0]
    except subprocess.CalledProcessError:
        return None


def get_version_from_pyproject_toml():
    try:
        with open("pyproject.toml", "r") as toml_file:
            pyproject = toml.load(toml_file)
            return pyproject.get("tool", {}).get("poetry", {}).get("version", None)
    except FileNotFoundError:
        return None


def main():
    version_from_toml = get_version_from_pyproject_toml()
    latest_git_tag = get_latest_git_tag()

    if version_from_toml != latest_git_tag:
        print(
            f"Error: Version in pyproject.toml ({version_from_toml}) does not match the latest Git tag ({latest_git_tag})."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
