test:
	pytest -v

ship:
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing

dev:
	gulp --cwd election/staticapp/

database:
	dropdb election --if-exists
	createdb election
