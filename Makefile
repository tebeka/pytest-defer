test:
	flake8 .
	python -m pytest -v -rf tests
