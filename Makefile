.PHONY: setup install freeze

PROJECT=sd-ussi-passage

all:
	@echo "make [setup|install|freeze]"

setup:
	python3 -m venv .${PROJECT}

install:
	@if [ "${VIRTUAL_ENV}" = "" ]; then echo Not inside venv; exit 2; fi
	-@[ ! -f requirements.txt ] && echo "pylint\npytest" > requirements.txt
#	@cat requirements.txt
	@pip install --upgrade pip
	@pip install -r requirements.txt

freeze:
	@if [ "${VIRTUAL_ENV}" = "" ]; then echo Not inside venv; exit 2; fi
	@pip install --upgrade pip
	@pip freeze | sort | tee requirements.txt
