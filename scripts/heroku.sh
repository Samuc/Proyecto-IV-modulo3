#!/bin/bash
sudo apt-get install wget wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh   # descargar herramienta heroku CLI
cd ..
sudo heroku login
sudo heroku create
sudo git add .
sudo git commit -m "desplegando en heroku"
sudo git push heroku master
sudo heroku open
