all:
	$(error please pick a target)

test:
	uvx ruff check .
	uv run python -m pytest -v -rf tests

publish:
	uv build

install-tools:
	python -m pip install uv
