.PHONY: clean-pyc clean-build clean-test docs clean

help:
	@echo "clean - remove all build, test, coverage, doc and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "clean-doc - remove documentation artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "test-doc - run Sphinx documentation integrity check"
	@echo "coverage-html - check code coverage quickly with the default Python"
	@echo "coverage-codacy - check code coverage and upload to codacy"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "dist - package"
	@echo "install - install the package to the active Python's site-packages"
	@echo "db - create new collectr database"
	@echo "crawl - crawl sparkmodel.com and update collectr database"

clean: clean-build clean-pyc clean-test clean-doc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -f coverage.xml
	rm -fr htmlcov/

clean-doc:
	$(MAKE) -C docs clean
	rm -rf docs/collectr*.rst
	rm -rf docs/modules.rst

lint:
	flake8 --max-complexity 10 *.py collectr docs tests

test:
	python setup.py test

test-doc:
	sphinx-build -b html -d docs/_build/doctrees docs docs/_build/html

test-all:
	tox

coverage:
	coverage run --source collectr setup.py test
	coverage report -m

coverage-html: coverage
	coverage html

coverage-codacy: coverage
	coverage xml
	python-codacy-coverage -r coverage.xml

docs:
	rm -rf docs/collectr*.rst
	rm -rf docs/modules.rst
	sphinx-apidoc -o docs collectr
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

db:
	make -C collectr/crawler db

crawl:
	make -C collectr/crawler crawl
