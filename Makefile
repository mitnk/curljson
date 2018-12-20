clean:
	find . -name '*.pyc' | xargs rm -f | cat
	rm -rf dist/
	rm -rf *.egg-info/
