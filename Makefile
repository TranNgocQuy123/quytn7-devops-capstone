setup:
	python3 -m venv ~/.devops

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:

lint:
	hadolint Dockerfile

all: install lint test

