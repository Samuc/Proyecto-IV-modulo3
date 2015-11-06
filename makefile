#Makefile autor: Samuel Carmona Soria
all: test install run
clean:
	rm *~*
	rm '*.pyc'
test:
	nosetests
install:
	sudo apt-get install libmysqlclient-
	sudo apt-get install python-dev
	pip install --upgrade pip
	pip install MySQL-python
	pip install Flask
	pip install nose
run:
	python runserver.py
