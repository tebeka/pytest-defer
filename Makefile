all:
	$(error please pick a target)

test:
	flake8 .
	python -m pytest -v -rf tests

publish:
	rm -rf dist
	python setup.py sdist
	python -m twine upload dist/*.tar.gz
	git tag $(shell python setup.py --version)
