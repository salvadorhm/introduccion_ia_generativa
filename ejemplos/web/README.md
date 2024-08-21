# Interfaz de usuario con Ollama y Javascript

## 0. Introducción

Creación de una aplicaciones web que realizan consultas a modelos de lenguaje largo mediante la [API REST de Ollama](https://github.com/ollama/ollama/blob/main/docs/api.md).

## 1. Servidor web

Estas aplicaciones estan diseñadas con [HTML5](https://www.w3schools.com/html/default.asp), [Bootstrap 5)](https://getbootstrap.com/) y [Javascript](https://www.w3schools.com/js/default.asp), y funciona sobre cualquier servidor web que se tenga disponible, por ejemplo [Apache2](https://httpd.apache.org/), [nginx](https://nginx.org/en/), etc. Para este ejemplo se veran 2 opciones: 

1. El [servidor web intergrado de python3](https://docs.python.org/es/3/library/http.server.html).
2. Utilizando [twisted](https://twisted.org/).

## 2. Instalación de los servidores web

### 2.1 Servidor web de python

En el caso de http.server es un módulo define clases para implementar servidores HTTP y se encuentra presintalada.

````bash
$ python3 -m http.server 8080
````

### 2.2 Twistted de python

1.2.1 Instalación de twistted

````bash
$ python3 -m pip install twisted
````

1.2.2 Ejecución del servidor

````bash
$ python3 -m twisted web --path .
`````

