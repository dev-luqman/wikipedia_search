setup:
	python3 -m venv ~/.wiki-app

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=wiki-app *.py


lint:
	pylint --disable=R,C wiki-app app lambda_app

all: install lint test 