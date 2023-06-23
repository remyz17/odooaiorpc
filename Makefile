# Makefile

unit-tests:
	@pytest

unit-tests-cov:
	@pytest --cov=odooaiorpc --cov-report term-missing --cov-report=html

unit-tests-cov-fail:
	@pytest --cov=odooaiorpc --cov-report term-missing --cov-report=html --cov-fail-under=80 --junitxml=pytest.xml | tee pytest-coverage.txt

clean-cov:
	@rm -rf .coverage
	@rm -rf htmlcov
	@rm -rf pytest.xml
	@rm -rf pytest-coverage.txt

format-black:
	@black .

format-isort:
	@isort .

lint-black:
	@black . --check

lint-isort:
	@isort . --check

lint-bandit:
	@bandit .

lint-flake8:
	@flake8 .

lint-mypy:
	@mypy ./odooaiorpc

lint-mypy-report:
	@mypy ./odooaiorpc --html-report ./mypy_html

format: format-black format-isort

lint: lint-black lint-isort lint-bandit lint-flake8 lint-mypy
