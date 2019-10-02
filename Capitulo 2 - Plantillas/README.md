# Tutorial Flask - Capitulo 2

En este capitulo, veremos de forma practica, como hacer uso de plantillas haciendo uso del framework Flask.

## Objetivo

    - Renderizar una plantilla en Flask
    - Pasar variables a una plantilla
    - estructuras de control

## Pre-requisitos

    - Entorno virtual configurado.
    - Proyecto base del capitulo 1

## Renderizado de plantillas

Crear una nueva carpeta dentro de la raíz del proyecto denominada templates y dentro de ella crear el archivo index.html. Por defecto Flask buscará las plantillas dentro de dicha carpeta.

	- aplicacion
		- templates
			- index.html

Abrimos y Editamos el archivo index.html y agregamos el siguiente código.

```
<h1>Hello World!</h1>
```

Luego, para poder renderizar el contenido de la pagina index.html, debemos importar la funcion render_template (encargada de integrar Flask con el motor de plantillas Jinja2) e implementarla en el metodo index() que mapea la raíz de la página.

```
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
```

Finalmente arrancamos el servidor y accedemos a la pagina http://127.0.0.1:5000/ para visualizar los cambios. 

## Variables

Para ver como pasar variables a una plantilla, crearemos una nueva pagina que reciba el nombre de un usuario desde una nueva url y la muestre por pantalla.

Para ello, creamos una nueva plantilla en la carpeta templates llamada hello.html y agregamos el siguiente contenido.

```
<h1>Hello {{name}}</h1>
```

Para poder renderizar la pagina, agregamos un nuevo metodo de pagina que recibirá el nombre por url y se lo pasaremos por parametro al render_template.

```
@app.route('/hello/<nombre>')
def hello_name( nombre ):
	return render_template( 'hello.html', name=nombre )
```

Como podrás ver, la variable "nombre" es recibida por desde la url y mapeada al parámetro de la funcion hello_name(). Por otra parte, como la variable que se espera en la plantilla se llama "{{name}}", es necesario especificarla en la funcion render_template como "name=nombre" para pasar el valor.

otras formas de pasar parametros son las siguientes:

```
<p>desde un diccionario: {{ mydict['key'] }}.</p>
<p>desde una lista: {{ mylist[3] }}.</p>
<p>desde una lista, con una variable como indice: {{ mylist[myintvar] }}.</p>
<p>desde un metodo de un objeto: {{ myobj.somemethod() }}.</p>
```

Finalmente arrancamos el servidor y accedemos a la página http://127.0.0.1:5000/hello/nombre para visualizar los cambios.

## Filtros de variables

Las variables se pueden modificar con filtros, que se agregan despues de la variable, separados por un caracter pipe (|), por ejemplo:

```
<h1>Hello {{name | capitalize}}</h1>
```

Lista de filtros disponibles en Jinja2

```
- safe: Representa el valor sin aplicar escape

- capitalize: Convierte el primer carácter del valor en mayúsculas y el resto en minúsculas.

- lower: Convierte el valor en minúsculas

- upper: Convierte el valor en mayúsculas

- title: Capitaliza cada palabra en el valor

- trim: Elimina los espacios en blanco iniciales y finales del valor

- striptags: Elimina cualquier etiqueta HTML del valor antes de renderizar
```

Jinja2 escapa todas las variables por motivo de seguridad, esto quiere decir que si la variable tiene como valor un extracto de codigo html como por ejemplo <h1>Hello World!</h1>, Jinja2 lo trasformará como &lt;h1&gt;Hello World!&lt;/h1&gt;. Es por esto que el filtro safe es de utilidad cuando queremos que Jinja2 no escape el valor de una variable.

```
Nota: nunca utilices safe en variables que sean ingresadas por medio de formularios de usuarios.
```

## Sentencias para control de flujo
inja2 ofrece varias estructuras de control que pueden usarse para alterar el flujo de la plantilla, dentro de ellas encontramos los siguientes ejemplos:

### Condiciones
```
Permite condicionar un segmento del html, ver ejemplo:

{% if user %}
    Hello, {{ user }}!
{% else %}
    Hello, Stranger!
{% endif %}
```

### Ciclos
```
Permite iterar un arreglo de datos, tal como se muestra en este ejemplo:

<ul>
    {% for comment in comments %}
        <li>{{ comment }}</li>
    {% endfor %}
</ul>
```

### Macros
```
Son similares a una función, que genera código HTML reutilizable.

{% macro render_comment(comment) %}
    <li>{{ comment }}</li>
{% endmacro %}

<ul>
    {% for comment in comments %}
        {{ render_comment(comment) }}
    {% endfor %}
</ul>

Las macros pueden ser mas reutilizables si los incorporamos dentro de un archivo separado, como por ejemplo:

{% import 'macros.html' as macros %}
<ul>
    {% for comment in comments %}
        {{ macros.render_comment(comment) }}
    {% endfor %}
</ul>
```

### Herencia
```
Podemos crear la estructura general de nuestra pagina en un archivo denominado base.html, que contendrá algo como lo siguiente:

<html>
<head>
    {% block head %}
    <title>{% block title %}{% endblock %} - My Application</title>
    {% endblock %}
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>

Luego podemos extender el archivo base.html e implementarlo de la siguiente forma:

{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
    {{ super() }}
    <style>
    </style>
{% endblock %}
{% block body %}
<h1>Hello, World!</h1>
{% endblock %}

En esta implementacion, podrás ver la sentencia {% extends "base.html" %} que indica cual es la plantilla/template padre. Por otra parte se hace llamada a {{ super() }} para hacer referencia a los contenidos del bloque de la plantilla base.html
```

## Páginas de error personalizadas

Para poder capturar los errores producidos por el servidor, puedes implementar el decorador @app.errorhandler de la siguiente manera

```
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
```

## Enlaces

Flask proporciona la url_for()función auxiliar, que genera URL a partir de la información almacenada en el mapa de URL de la aplicación. La forma de implementar esta funcion es de la siguiente manera:

```
url_for('index')
    devuelve: /

url_for('index', _external=True)
    devuelve: http://localhost:5000/

url_for('hello_name', name='luis', _external=True)
    devuelve: http://localhost:5000/user/luis

url_for('hello_name', name='luis', page=2, version=1)
    devuelve: /user/luis?page=2&version=1
```
