# Work-in-out

Samuel Carmona Soria [![Build Status](https://travis-ci.org/Samuc/Proyecto-IV-modulo3.svg)](https://travis-ci.org/Samuc/Proyecto-IV-modulo3)  [![Snap-CI](https://snap-ci.com/Samuc/Proyecto-IV-modulo3/branch/master/build_image)](https://snap-ci.com/Samuc/Proyecto-IV-modulo3/branch/master) [![Heroku](https://www.herokucdn.com/deploy/button.png)](https://work-in-out-samuc.herokuapp.com/)


### Plataforma enfocada a los deportistas, híbrido entre red social y tablón de eventos. Proyecto relacionado con la asignatura DAI.
## Descripción
El proyecto consiste en una plataforma virtual pensada a modo de híbrido entre red social y tablón de eventos. La plataforma se centra en los deportistas y pretende abarcar todo su rango, desde principiantes a avanzados.
Entrando en detalle, la plataforma consistiría en un sitio web donde es necesario el registro, y en el cual se tiene acceso a un tablón de eventos donde los distintos usuarios puede tanto visualizar (y unirse) a los eventos ya creados por otros usuarios como también crear un evento nuevo, al cual los demás puedan unirse.

Cada evento especifica dentro de sí todos sus detalles y al tipo de público al que va dirigido, además de mostrar los participantes que asistirían y los comentarios que se han hecho al respecto sobre el mismo.
Debido a la naturaleza de la plataforma, orientada mayormente al campo abierto, se pretende hacer uso de integración con mapas, posibilitando así funcionalidades como ver rutas, compartirlas, etc...

Además , la plataforma actuará como una especia de red social, siendo capaz cada usuario de tener su red de amigos, así como de permanecer en contacto con estos por mensajería.

## Requisitos básicos

* Registro de usuarios

* Tablón de eventos

* Funciones propias de una red social(mensajería, comentarios, etc...)

* Gestión de rutas

* Organización por deportes

## Trabajo futuro

- Chat

- Versión móvil

- Creación de grupos

## Herramientas a usar

* Usaremos **Flask** como framework para la aplicación.

* **Python**, para la parte del servidor, así como funcionalidades de la web.

* **HTML5** y **CSS3** para la interfaz web.

* **MySQL**, para bases de datos de usuarios y eventos.

## Descripción de la inmplicación en el proyecto conjunto
Éste módulo se dedicará a los servicios que ofrece el servidor de nuestro sistema web.
Los servicios incluyen la conexión de la aplicación con las bases de datos, el despliegue/configuración de la misma, procesamiento de las peticiones de los usuarios etc.

Para éste módulo se usará el microfamework Flask basado en el lenguage Python.


## Participación en el certamen de proyectos de libres organizado por la Oficina de Software Libre de la UGR
El proyecto ha sido inscrito en el certamen de proyectos libres de la UGR.

#Desarrollo basado en pruebas
Hemos creado una clase básica sobre la que poder realizar test básicos.
Ésta clase es "User", que contendrá funciones básicas como get_email, get_id, login, etc.

#Makefile
He creado un makefile para automatizar la instalación de los paquetes necesarios, y ejecución del programa, añadiendo la opción para hacer limpieza y test con la herramienta nose:
```
#Makefile autor: Samuel Carmona Soria
all: test install run
clean:
	rm *~*
	rm '*.pyc'
test:
	nosetests runserver.py
install:
	sudo apt-get install libmysqlclient-
	sudo apt-get install python-dev
	pip install --upgrade pip
	pip install MySQL-python
	pip install Flask
	pip install nose
run:
	python runserver.py

```

#Integración Continua
Para la automatización del proceso de pruebas y para desarrollar el proyecto bajo el concepto de Integración Contínua, he usado Travis-CI para la integración continua.
La configuración para Travis-CI se indica en el fichero .travis.yml.

![travis1](http://i770.photobucket.com/albums/xx346/BkY_1234/integracioncontinua_zps7wakrtul.jpg)

#Fichero .travis.yml
Hemos especificado en el fichero **.travis-yml** las dependencias a instalar así como indicar que *nose* debe ejecutar los tests que existan.
```
language: python

python:
  - "2.7"

install:
   - sudo apt-get install libmysqlclient-dev
   - sudo apt-get install python-dev
   - pip install --upgrade pip
   - pip install MySQL-python
   - pip install Flask
   - pip install nose

script:       # script para tests
   - nosetests runserver.py

```

#Tests
Para realizar los tests hemos realizado test básicos en la clase "User" nombrada añadido, que serán ejecutados por la herramienta nosetests.
```
import unittest
class User (unittest.TestCase):
    name =  "Prueba_test"
    id = "123_test"
    email = "test@gmail.es"

    def get_name_test(self):
        self.assertEqual(self.name, "Prueba_test")

        return self.name

    def get_id_test(self):
        self.assertEqual(self.id, "123_test")

        return self.id

    def get_email_test(self):
        self.assertEqual(self.email,"test@gmail.es")

        return self.email

    def login_test(self,id="123_test",password="123456"):
        self.assertEqual(id,"123_test")
        self.assertEqual(password,"123456")

        return True

    def get_gender_test(self):
        gender = "male"

        self.assertEqual(gender,"male")

        return gender

```

Al ejecutar nosetests sobre éste archivo, podemos comprobar que pasa los tests correctamente:
![Ejecutando nosetests](http://i770.photobucket.com/albums/xx346/BkY_1234/captura_nosetests_zpsvp3ybx0t.jpg)

Ahora, tras haber preparado los tests y el archivo ".travis.yml" procedemos a hacer un push, y comprobar qué es lo que ocurre en Travis.

Como vemos en la siguiente captura, el push se ha realizado correctamente, se han pasado los tests y han concluido sin problemas:
![travis2](http://i770.photobucket.com/albums/xx346/BkY_1234/capturaTravis_zpsljyursje.jpg)




# Despliegue en un PaaS: [Heroku](https://www.heroku.com/)
La Plataforma como servicio (PaaS) por la que nos hemos decantado a sido Heroku, debido a que es fácil de usar, gratuito hasta cierto punto y es totalmente compatible con el lenguaje Python.
Además tiene fácil integración con GitHub, despliegue automático al hacer cada "push" al repositorio en Git y se espera a que Travis-CI pase los tests satisfactoriamente.

Creamos el  fichero "Procfile" el cual contiene la orden necesaria para ejecutar la aplicación web.
[Procfile](https://github.com/Samuc/Proyecto-IV-modulo3/blob/master/Procfile)
```
web: python runserver.py
```

También, hemos creado el fichero "requirements.txt", en el que indica las dependencias y su versión en concreto. Este fichero sería neceasria aunque la aplicación no tuviese ninguna dependencia. (estaría vacío)

[requirements.txt](https://github.com/Samuc/Proyecto-IV-modulo3/blob/master/requirements.txt):

```Flask==0.10.1
Flask-WTF==0.12
Jinja2==2.8
MarkupSafe==0.23
WTForms==2.0.2
MySQL-python==1.2.3
```

Una vez instalado el cliente de heroku, y registrado en su web ejecutamos el siguiente comando para para identificarnos:
```
heroku login
```

Ahora en el directorio de la aplicación ejecutamos:
```
heroku create
```
La ejecución nos dice que la aplicación estará disponible en un link con un nombre por defecto.
Para modificar dicho nombre, entramos en la configuración de la aplicación y le llamamos por ejemplo "work-in-out-samuc".
![work-in-out-samuc](http://i770.photobucket.com/albums/xx346/BkY_1234/capturah1_zpsuhzgqnka.jpg)

Ahora, para hacer uso de la integración contínua con GitHub, que podemos hacerla desde Heroku o con Snap-CI.
Primero vamos a realizarla la primera opción, configuramos la sección correspondiente en la web de heroku.
Conectamos la app con éste repositorio, activamos la opción de que espere a que pase satisfactoriamente los tests y activamos el despliegue automático.
![Configuración integración contínua](http://i770.photobucket.com/albums/xx346/BkY_1234/capturah2_zpswbsolwpy.jpg)

Ahora, podemos realizar un commit cualquiera (modificando por ejemplo éste mismo README.md) para realizar el despliegue en heroku, con los siguientes comandos tras haber realizado lo dicho anteriormente (login y create):
```
git add README.md
git commit -m "Desplegando en Heroku"
git push heroku master
```

Ahora con el siguiente comando comprobamos que está funcionando actualmente:
```
samu@samu: ~/Facultad/IV/Proyecto-IV-modulo3
>  heroku ps:scale web=1
Scaling dynos... done, now running web at 1:Free.
```

Y con el siguiente comando se nos abre en una nueva pestaña del navegador:

```
samu@samu: ~/Facultad/IV/Proyecto-IV-modulo3
> heroku open
```

En el siguiente link se encuentra la aplicación ya desplegada en Heroku: [Aquí](https://work-in-out-samuc.herokuapp.com/) ó https://work-in-out-samuc.herokuapp.com/


Para la integración con SNAP-CI, en su web se nos identifica con los datos de GitHub, nos muestra automáticamente nuestros repositorios y añadimos el repositorio actual de la aplicación.

Y ahora configuramos el pipeline tal cual muestra las siguientes imágenes:
![GitHub information](http://i770.photobucket.com/albums/xx346/BkY_1234/capturah3_zpse9qhlqgn.jpg)
![Tests configuration](http://i770.photobucket.com/albums/xx346/BkY_1234/capturah5_zps23ln3cir.jpg)
![Deploy Configuration](http://i770.photobucket.com/albums/xx346/BkY_1234/capturah4_zpsbxrmb8sv.jpg)

Finalmente, guardamos la configuración, hacemos un commit modificando éste readme y hacemos un push a git, esperamos y obtenemos en SNAP que se ha realizado el deployment correctamente:
![Deployment SNAP-CI passed](http://i770.photobucket.com/albums/xx346/BkY_1234/capturah6_zpstyll3hv9.jpg)


#Avances en el proyecto
Hemos creado una pantalla de login de usuario y de registro, con su hoja de estilo correspondiente.
Y además, un formulario de registro para registrar nuevos usuarios. También hemos añadido comprobación de campos al rellenar los formularios, como por ejemplo que no estén vacíos, que el formato del email tenga un formato correcto, etc.
![Login Work-in-out](http://i770.photobucket.com/albums/xx346/BkY_1234/captura_clienthtml_zpshnc3jzys.jpg)

Éstos ficheros creados se pueden ver en la carpeta static en éste repositorio.
