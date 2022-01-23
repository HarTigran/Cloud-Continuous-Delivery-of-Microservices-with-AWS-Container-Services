install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

# test:
# 	python -m pytest -vv test_main.py

format:
	black *.py

run:
	python main.py

run-uvicorn:
	uvicorn main:app --reload

killweb:
	sudo killall uvicorn

lint:
	python -m pylint --errors-only main.py

all: install lint test
