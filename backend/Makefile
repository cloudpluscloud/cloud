install-python:
	pip3 install -r requirements.txt

# test:
# 	npm test

format-python:
	black *.py

lint:
	pylint --disable= R,C *.py


all: install-python format-python lint