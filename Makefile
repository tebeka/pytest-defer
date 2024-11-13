all:
	$(error please pick a target)

test:
	uvx ruff check .
	uv run python -m pytest -v -rf tests

publish:
	test -n "$(UV_PUBLISH_TOKEN)" || (echo "UV_PUBLISH_TOKEN not set" && false)
	uv publish

install-tools:
	python -m pip install uv
