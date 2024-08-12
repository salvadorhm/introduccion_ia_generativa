# Interfaz de usuario con Ollama y Javascript

## 0. Introducción

Creación de una aplicación web de tipo chat para realizar preguntas a un modelo de lenguaje largo sobre Ollama.

## 1. Servidor web

Esta aplicación esta diseñada con HTML5, Bootstrap 5 (CSS3) y Javascript, y funciona sobre cualquier servidor web que se tenga disponible, por ejemplo Apache2, NGNIX, etc. Para este ejemplo se veran 2 opciones, una con el servidor web intergrado de python3 y otra con twistted.

### 1.1 Servidor web de python

````bash
$ python3 -m http.server 8080
````

### 1.2 Twistted de python

1.2.1 Instalación de twistted

````bash
$ python3 -m pip install twisted  
````

1.2.2 Ejecución del servidor

````bash
$ python3 -m twisted web --path .
`````

