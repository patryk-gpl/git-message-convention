from unittest.mock import mock_open, patch

import pytest

from hooks import git_convention as git

valid_messages = [
    ("feat: added new feature"),
    ("docs: correct spelling mistakes"),
    ("ci: fix pipeline configuration file"),
    ("chore(deps): bump dependency version"),
    ("fix: prevent null pointer exception"),
    ("refactor: extract method into separate function"),
    ("style: update code style based on code review"),
    ("test: add unit test for login functionality"),
    ("build: compile project for release build"),
    ("BREAKING CHANGE: new API will return null"),
    ("chore: Add commit message"),
    ("feat: Add new commit"),
]

invalid_messages = [
    ("wip"),
    ("feat: "),
    ("wip: add new feature"),
    ("rename variable"),
    ("BrEAKING CHANGE: new API will return null"),
    ("breaking change: new API will return null"),
]


class TestKarmaGitMessageConvention:
    @pytest.mark.parametrize("commit_message", valid_messages)
    def test_valid_messages(self, commit_message):
        with patch("hooks.git_convention.open", mock_open(read_data=commit_message)):
            exit_status_ok = 0
            assert git.verify_git_karma_message_convention() == exit_status_ok

    @pytest.mark.parametrize("commit_message", invalid_messages)
    def test_wrong_messages(self, commit_message):
        with patch("hooks.git_convention.open", mock_open(read_data=commit_message)):
            exit_status_non_zero = 1
            assert git.verify_git_karma_message_convention() == exit_status_non_zero

    def test_message_too_long(self):
        long_message = (
            "refactor: extract method into separate function, message is too long"
        )
        with patch("hooks.git_convention.open", mock_open(read_data=long_message)):
            exit_status_non_zero = 1
            assert git.verify_git_karma_message_convention() == exit_status_non_zero
