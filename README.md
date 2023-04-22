# pre-commit-hooks

[![Test with poetry](https://github.com/patryk-gpl/pre-commit-hooks/actions/workflows/test.yml/badge.svg)](https://github.com/patryk-gpl/pre-commit-hooks/actions/workflows/test.yml)
[![SonarCloud analysis](https://github.com/patryk-gpl/pre-commit-hooks/actions/workflows/sonar.yml/badge.svg)](https://github.com/patryk-gpl/pre-commit-hooks/actions/workflows/sonar.yml)

- [pre-commit-hooks](#pre-commit-hooks)
  - [verify-git-karma-commit-message](#verify-git-karma-commit-message)
  - [Local development setup](#local-development-setup)

Helper Git hooks to work with [pre-commit](https://pre-commit.com/) framework.

List of currently available hooks:

### verify-git-karma-commit-message

This hooks will verify Git commit is following Karma Git message convention documented [here]()

## Local development setup

Just run `make` command with available rules.

1. To install local development environment run:

```
    make install
```

2. To run unit tests:

```
    make test
```
