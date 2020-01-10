# API User Template

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Django_logo.svg/650px-Django_logo.svg.png)]()

[![Language](https://img.shields.io/badge/Python-3.5%20%7C%203.6%20%7C%203.7-blue.svg)](https://www.python.org/)


API User Template, es un template de codigo abierto, para facilitar el levantamiento de una api con Django, ademas de tener una implementacion de un modelo de usuarios personalizado.

  - Facil despliegue en enternos de desarrollo.
  - Un gran numero de herramientas a dispocision.
  - Paso a produccion rapido y sin problemas.

### Dependencias

Para que el entorno funcione correctamente es necesario:

* [Docker] - version 19+
* [Docker Compose] - version 1.18+
* [Python] - version 3.5+

### Installation

Es necesario copiar el archivo .env.example como .env, modificar las variables de entorno a gusto del usuario. Luego construir las imagenes con docker-compose.
```sh
$ cp .env.example .env
$ docker-compose -f local.yml build
$ docker-compose -f local.yml up -d
```

Para un entorno de producción

```sh
$ docker-compose -f production.yml build
$ docker-compose -f production.yml up -d
```

<p align="center"> 
    <img src="https://octodex.github.com/images/nyantocat.gif" alt="octodex">
 </p>


