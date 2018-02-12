.PHONY: clean-pyc clean-build clean-test clean

help:
	@echo "clean - remove all build, test, coverage, doc and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage-html - check code coverage quickly with the default Python"
	@echo "coverage-codacy - check code coverage and upload to codacy"
	@echo "db - create new collectr database"
	@echo "crawl - crawl sparkmodel.com and update collectr database"
	@echo "run - launch development web server"

clean: clean-build clean-pyc clean-test

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

lint:
	flake8 --max-complexity 10 *.py collectr docs tests

test:
	nose2 -v

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

crawl:
	make -C collectr/service crawl

run:
	python manage.py runserver -h 0.0.0.0 -p 5000 -d

db:
	python collectr/db/create.py
