# API Dj Template

<p align="center"> 
    <img src="src/static/img/python.jpg" alt="octodex">
 </p>


[![Language](https://img.shields.io/badge/Python-3.5%20%7C%203.6%20%7C%203.7-blue.svg)](https://www.python.org/)


Este repositorio cuenta con una implemtacion de django rest framework para el levantamiento de una api, de manera rapida y eficaz. 

### Dependencias

Para hacer funcionar este template es necesario tener las siguientes herramientas instaladas en su maquina. Este template fue generado en un pc Linux, pero gracias al uso de Docker, su funcionamiento debe ser el mismo en maquinas Windows o Mac.

* [Docker] - version 19+
* [Docker Compose] - version 1.18+
* [Python] - version 3.5+

Si deseas conectar la aplicacion con una base de datos mysql sera necesario tener instalado algunos paquetes para el correcto funcionamiento con versiones python 3 en adelante, para instalarlas es necesario el siguiente comando :
```sh
$ sudo apt-get install python3-dev libmysqlclient-dev
```

### Como usar

- Primero debes clonar el repositorio, una vez en tu maquina situarte en la raiz de este.
- La primera modificacion que debes hacer es copiar el archivo .env.example donde se encuentran las variables de entorno, como .env para que puedan ser accesibles por docker.
```sh
$ cp .env.example .env
```

- Luego contruir las imagenes de docker con docker compose, para esto utilizaremos el siguiente comando .

```sh
$ docker-compose -f local.yml build
```
- Finalmente levantar los servicios, una vez lanzado el comando podras revisar en el puerto 8034 de tu local el sistema funcionando 
```sh
$ docker-compose -f local.yml up
```
- Para ambientes productivos debes hacer la misma rutina anterior, pero levantar los servicios con el archivo production.yml en vez de local.yml.

## Good luck for you !!!

<p align="center"> 
    <img src="https://octodex.github.com/images/nyantocat.gif" alt="octodex">
 </p>

