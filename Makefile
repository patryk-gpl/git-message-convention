.PHONY: help bootstrap tags init-hooks update-hooks run-hooks setup

.DEFAULT_GOAL := help

help:
	@echo "Usage: make <target>"
	@echo -e "Available targets:\n"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort
	@echo ""


# Git hooks
install: ## Setup local development environment
	@poetry install

validate: install ## Validate the pre-commit configuration
	@poetry run pre-commit validate-manifest

update-hooks:
	@poetry run pre-commit autoupdate

test:	## Run tests
	@poetry run pytest
