setup:
	python3 -m venv ~/.wiki-app

install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

env:
	#Show information about environment
	which python3
	python3 --version
	which pytest
	which pylint

validate-circleci:
	circleci config process .circleci/config.yml

run-circleci-local:
    # See https://circleci.com/docs/2.0/local-cli/#running-a-job
	circleci local execute

test:
	python -m pytest -vv --cov=wiki_lambda-app wiki_api.py *.py

lint:
	# hadolint Dockerfile
	pylint --disable=R,C wiki_api app

all: install lint test 