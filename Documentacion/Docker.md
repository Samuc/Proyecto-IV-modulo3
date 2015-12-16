## Entorno de pruebas: [Docker](https://www.docker.com/)
Se usa Docker como plataforma que automatiza el despliegue de la aplicación dentro de contenedores software, de manera que pueda probarse en un entorno aislado antes de desplegarla a producción.


Primero de todo, existe un script para realizar la instalación y uso de heroku rápidamente, el cual se encuentra al final de ésta documentación.

Para la creación de la imagen, Docker usa un fichero dentro del directorio de la aplicación llamado [Dockerfile](https://github.com/samuc/Proyecto-IV-modulo3//Dockerfile).

Éste archivo consta de lo siguiente:
```
FROM ubuntu:latest

#Autor
MAINTAINER Samuel Carmona Soria <samuelcarmona123@gmail.com>

#Actualizar Sistema Base
RUN sudo apt-get update
#Descargar aplicacion
RUN sudo apt-get install -y git
RUN sudo git clone https://github.com/Samuc/Proyecto-IV-modulo3

#Instalar paquetes necesarios
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo apt-get install -y libmysqlclient-dev
RUN sudo apt-get install -y python-dev
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip
RUN sudo pip install MySQL-python
RUN sudo pip install Flask
RUN sudo pip install nose

#Instalar la app
RUN cd Proyecto-IV-modulo3 && sudo pip install -r requirements.txt
```
Primero iniciamos Docker con el siguiente comando:
```docker con sudo docker -d &```.

Ahora, en la web de Docker Hub, vamos a creamos un "Automated Build" sobre el repositorio de nuestro proyecto, lo cual comenzará a crear la imagen.

En el directorio del repositorio, creamos una imagen con: (no olvidad el punto del final)
 ``` sudo  docker build -f Dockerfile -t samuel_iv .```
o
 ``` sudo  docker build -t samuel_iv .``` (cogerá por defecto el fichero con el nombre Dockerfile en caso de existir)
Como podemos ver en la siguiente captura:
![Ejercicio10_1]()


Podemos ver que se ha creado ejecutando el comando ```sudo docker images``` :
![ej10_2]()
(Las imagenes con nombre <none> son intentos fallidos, que borraré mas adelante)

Como podemos ver en la imagen anterior, la imagen se ha creado correctamente, y ocupa 466.1 MB.

Ahora, cargamos la imagen con:
 ```sudo docker run -t -i samuel_iv /bin/bash```

Una vez dentro, comprobamos la ip que tiene con **ifconfig** para después utilizarla:
![ej10_3]()

Dentro de la imagen ejecutamos la aplicación:
```
root@594b9484609a:/# cd Proyecto-IV-modulo3/
root@594b9484609a:/Proyecto-IV-modulo3# python runserver.py
```

Ahora vamos al navegador, y en la dirección   **http://172.17.0.2:5000/** nos encontraremos con la aplicación funcionando correctamente:
![ej10_4]()

Ahora vamos a crear nuestra imagen en la página web de [docker](https://www.docker.com/):

Primero me he registrado [Aqui](https://hub.docker.com/?utm_source=getting_started_guide&utm_medium=embedded_MacOSX&utm_campaign=create_docker_hub_account)
Tras verificar la cuenta, creamos un repositorio con visibilidad pública:
![ej10_5]()

Ahora, introduzco el siguiente comando:
```
sudo docker build -f Dockerfile -t samucs/proyecto-iv:latest --no-cache=true ./
```

Hago login con las credenciales de Docker:
```
sudo docker login
```

Y finalmente hago el push al repositorio de Docker:
```
sudo docker push samucs/proyecto-iv:latest
```
Se puede ver la imagen subida a Docker [aquí](https://hub.docker.com/r/samucs/proyecto-iv//)


Para agilizar el uso de docker he creado el siguiente [script](https://github.com/Samuc/Proyecto-IV-modulo3/script/docker.sh)

Para su ejecución realizaros:
```
sudo ./heroku.sh
```
