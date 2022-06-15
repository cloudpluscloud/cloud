install-python:
	pip3 install -r requirements.txt

test:
	python3 -m pytest -vv test.py


format-python:
	black *.py

lint:
	pylint --disable= R,C *.py


all: install-python test format-python lint