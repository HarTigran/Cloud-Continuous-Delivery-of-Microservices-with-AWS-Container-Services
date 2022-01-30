install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

# test:
# 	python -m pytest -vv test_UI_app.py

format:
	black *.py

run:
	python UI_app.py

lint:
	pylint --disable=R,C,W0622,E0401 UI_app.py

all: install lint test
