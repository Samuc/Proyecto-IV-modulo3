# Despliegue en un PaaS: [Heroku](https://www.heroku.com/)
La Plataforma como servicio (PaaS) por la que nos hemos decantado a sido Heroku, debido a que es fácil de usar, gratuito hasta cierto punto y es totalmente compatible con el lenguaje Python.
Además tiene fácil integración con GitHub, despliegue automático al hacer cada "push" al repositorio en Git y se espera a que Travis-CI pase los tests satisfactoriamente.

Primero de todo, existe un script para realizar la instalación y uso de heroku rápidamente, el cual se encuentra al final de ésta documentación.

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
###Integración con Heroku
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


Para agilizar el uso de docker he creado el siguiente [script](https://github.com/Samuc/Proyecto-IV-modulo3/blob/master/scripts/heroku.sh)

Para su ejecución realizaros:
```
sudo ./docker.sh
```
