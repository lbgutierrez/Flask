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