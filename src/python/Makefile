test:
	pytest
.PHONY: test

clean:
	find . \( \
		-name '*.egg-info' -o \
		-name 'bdist.*' -o \
		-name 'dist' -o \
		-name '__pycache__' -o \
		-name '*.pyc' \) \
		-exec rm -rf {} +
.PHONY: clean
