# Work-in-out

<<<<<<< HEAD
=======
#PRIMER HITO#

>>>>>>> fb38f1860212f085b2894bfa939c0da0e7681a2b
### Plataforma enfocada a los deportistas, híbrido entre red social y tablón de eventos. Proyecto relacionado con la asignatura DAI.

## Descripción general

El proyecto consiste en una plataforma virtual pensada a modo de híbrido entre red social y tablón de eventos. La plataforma se centra en los deportistas y pretende abarcar todo su rango, desde principiantes a avanzados.
Entrando en detalle, la plataforma consistiría en un sitio web donde es necesario el registro, y en el cual se tiene acceso a un tablón de eventos donde los distintos usuarios puede tanto visualizar (y unirse) a los eventos ya creados por otros usuarios como también crear un evento nuevo, al cual los demás puedan unirse.

Cada evento especifica dentro de sí todos sus detalles y al tipo de público al que va dirigido, además de mostrar los participantes que asistirían y los comentarios que se han hecho al respecto sobre el mismo.
Debido a la naturaleza de la plataforma, orientada mayormente al campo abierto, se pretende hacer uso de integración con mapas, posibilitando así funcionalidades como ver rutas, compartirlas, etc...

Además , la plataforma actuará como una especia de red social, siendo capaz cada usuario de tener su red de amigos, así como de permanecer en contacto con estos por mensajería.

## Descripción del Módulo 3

Éste módulo se dedicará a los servicios que ofrece el servidor de nuestro sistema web.
Los servicios incluyen la conexión de la aplicación con las bases de datos, el despliegue/configuración de la misma, procesamiento de las peticiones de los usuarios etc.

Para éste módulo se usará el microfamework Flask basado en el lenguage Python.


#SEGUNDO HITO#
#Avances en el proyecto
Para un primer avance en el proyecto hemos creado una pantalla de login de usuario y de registro, con su hoja de estilo correspondiente.
Y además, un formulario de registro para registrar nuevos usuarios. También hemos añadido comprobación de campos al rellenar los formularios, como por ejemplo que no estén vacíos, que el formato del email tenga un formato correcto, etc.
![Login Work-in-out](http://i770.photobucket.com/albums/xx346/BkY_1234/captura_clienthtml_zpshnc3jzys.jpg)

Éstos ficheros creados se pueden ver en la carpeta static en éste repositorio.

También, he creado una clase básica sobre la que poder realizar test básicos con el fin de éste hito.
Ésta clase es "User", que contendrá funciones básicas como get_email, get_id, login, etc.


#Integración Continua
Para la automatización del proceso de pruebas y para desarrollar el proyecto bajo el concepto de Integración Contínua, hemos usado Travis-CI para la integración continua.
La configuración para Travis-CI se indica en el fichero .travis.yml.

![travis1](http://i.imgur.com/61PhAWG.png)

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
Para realizar los tests hemos realizado test básicos en la clase "User" nombrada añadido:
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


<<<<<<< HEAD
Al ejecutar nosetests sobre éste archivo, podemos comprobar que pasa los tests correctamente:
![Ejecutando nosetests](http://i770.photobucket.com/albums/xx346/BkY_1234/captura_nosetests_zpsvp3ybx0t.jpg)
=======
* **MySQL**, para bases de datos de usuarios y eventos.

## Módulos

* **[Módulo 1, Jesús García Godoy](https://github.com/jesmorc/Proyecto-IV-modulo1)**: Este módulo se centrará en el servidor de bases de datos, el cual necesitaremos para almacenar los datos de la aplicación, como los usuarios, eventos, comentarios, etc...

* **[Módulo 2, David Santiago Carrión](https://github.com/dscdac/Proyecto-IV-modulo2)**: Este módulo se enfocará del front-end de la aplicación.

* **[Módulo 3, Samuel Carmona Soria](https://github.com/Samuc/Proyecto-IV-modulo3)**: Por último, este módulo se encargará de gestionar el servidor web que alojará la aplicación.
>>>>>>> fb38f1860212f085b2894bfa939c0da0e7681a2b

Ahora, tras haber preparado los tests y el archivo ".travis.yml" procedemos a hacer un push, y comprobar qué es lo que ocurre en Travis.

Como vemos en la siguiente captura, el push se ha realizado correctamente, se han pasado los tests y han concluido sin problemas:
![travis2](http://i.imgur.com/0vSpiO8.png)

#SEGUNDO HITO#
#Avances en el proyecto
Para un primer avance en el proyecto hemos creado una pantalla de login de usuario y de registro, con su hoja de estilo correspondiente.
Y además, un formulario de registro para registrar nuevos usuarios. También hemos añadido comprobación de campos al rellenar los formularios, como por ejemplo que no estén vacíos, que el formato del email tenga un formato correcto, etc.
![Login Work-in-out](http://i770.photobucket.com/albums/xx346/BkY_1234/captura_clienthtml_zpshnc3jzys.jpg)

Éstos ficheros creados se pueden ver en la carpeta static en éste repositorio.

También, he creado una clase básica sobre la que poder realizar test básicos con el fin de éste hito.
Ésta clase es "User", que contendrá funciones básicas como get_email, get_id, login, etc.


#Integración Continua
Para la automatización del proceso de pruebas y para desarrollar el proyecto bajo el concepto de Integración Contínua, hemos usado Travis-CI para la integración continua.
La configuración para Travis-CI se indica en el fichero .travis.yml.

![travis1](http://i.imgur.com/61PhAWG.png)

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
Para realizar los tests hemos realizado test básicos en la clase "User" nombrada añadido:
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
![travis2](http://i.imgur.com/0vSpiO8.png)
