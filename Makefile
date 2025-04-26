install:
	pip install -e .
	pip install -r requirements.txt
	pip install black flake8 pytest

test:
	pytest

lint:
	flake8 src tests

format:
	black src tests

all: install test lint format
