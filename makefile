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
	sudo apt-get install mysql-python
	sudo pip install --upgrade pip
	sudo pip install MySQL-python
	sudo pip install Flask
	sudo pip install nose
	sudo pip install -r requirements.txt
run:
	python runserver.py
