#!/usr/bin/env python3

import re
import os
import sys


def verify_git_karma_message_convention() -> int:
    """Check commit message against Karma's commit message convention."""
    regex = r"^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)(\([a-z0-9 \-]+\))?: .{1,50}|(^BREAKING CHANGE: .+){1,50}$"
    karma_url = "http://karma-runner.github.io/6.4/dev/git-commit-msg.html"
    error_msg = f"Commit message does not match Karma's commit message convention. Please see: {karma_url}"

    commit_msg_file = "/".join([os.getenv("GIT_DIR", ".git"), "COMMIT_EDITMSG"])
    with open(commit_msg_file, "r") as f:
        commit_msg_first_line = f.readline().strip()

    if len(commit_msg_first_line) > 50:
        print("Commit message too long. Max 50 characters allowed.")
        return 1

    print(f"{commit_msg_first_line=}")
    if re.match(regex, commit_msg_first_line):
        return 0
    print(error_msg)
    return 1


def main() -> int:
    """Main function."""
    sys.exit(verify_git_karma_message_convention())


if __name__ == "__main__":
    main()
