#!/bin/bash

#Actualizamos e instalamos docker
sudo apt-get update
sudo apt-get install -y docker-engine

#Descargar la imagen
sudo docker pull samucs/proyecto-iv:latest
#Ejecuta la imagen
sudo docker run -i -t samucs/proyecto-iv:latest /bin/bash
