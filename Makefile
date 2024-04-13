PHONY: watch
watch:
	PYTHONPATH=${PWD}:${PYTHONPATH} ptw -c -v
test:
	PYTHONPATH=${PWD}:${PYTHONPATH} pytest -v
dev:
	PYTHONPATH=${PWD}:${PYTHONPATH} python3 -m src
