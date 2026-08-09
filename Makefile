.PHONY: test check sandbox-image

test:
	python -m pytest -q

check:
	python -m compileall -q src tests
	ruff check src tests
	python -m pytest -q

sandbox-image:
	docker build -t vpi-cvm-sandbox:py313 sandbox/
