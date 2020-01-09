# Django Rest Framework Template

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Django_logo.svg/1200px-Django_logo.svg.png)](https://nodesource.com/products/nsolid)

[![Language](https://img.shields.io/badge/Python-3.5%20%7C%203.6%20%7C%203.7-blue.svg)](https://www.python.org/)


Django Rest Framework Template, es un template de codigo abierto, para facilitar el desarrollo de programadores.

  - Facil despliegue en enternos de desarrollo.
  - Un gran numero de herramientas a dispocision.
  - Paso a produccion rapido y sin problemas.

### Dependencias

Para que el entorno funcione correctamente es necesario:

* [Docker] - El mejor contenedor!
* [Docker Compose] - Simplifica el uso de Docker.
* [Python] - Python 3.6 en adelante.

### Installation

Es necesario copiar el archivo .env.example como .env, modificar las variables de entorno a gusto del usuario. Despues simplemente construir las imagenes con docker-compose.
```sh
$ cp .env.example
$ docker-compose -f local.yml build
$ docker-compose -f local.yml up -d
```

Para un entorno de producción

```sh
$ docker-compose -f production.yml build
$ docker-compose -f production.yml up -d
```

