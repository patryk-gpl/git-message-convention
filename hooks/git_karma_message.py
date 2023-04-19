#!/usr/bin/env python3

import re
import sys

regex = r"^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)(\([a-z0-9 \-]+\))?: .{1,50}$"

commit_message_file = sys.argv[1]
with open(commit_message_file, encoding="utf-8") as f:
    commit_message = f.read().strip()

if re.match(regex, commit_message):
    sys.exit(0)
print(f"Invalid commit message: {commit_message}")
print("Please follow the Karma Git commit message convention.")
sys.exit(1)
