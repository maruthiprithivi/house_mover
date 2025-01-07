# Makefile for house_mover project

.PHONY: format check build setup install-editable help

# Format the code using black
format:
	ruff format src

# Check the code using ruff
check:
	ruff check src

# Build the package
build:
	python -m build

# Setup the project by installing dependencies for development or local build and usage
setup:
	pip install -e .[dev]

# Install the package in editable mode without dev dependencies
install-editable:
	pip install -e .

# Display help information
help:
	@echo "Makefile commands for house_mover:"
	@echo "  make format           Format the code using ruff"
	@echo "  make check            Check the code using ruff"
	@echo "  make build            Build the package"
	@echo "  make setup            Setup the development environment"
	@echo "  make install-editable Install the package in editable mode"
