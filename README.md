# Tutorial Flask - Apuntes

Los siguientes apuntes tienen como objetivo explicar conceptos relacionados con el Framework Flask, donde podrás acudir de forma inmediata si necesitas aclarar alguna duda. 

Cabe señalar que estos apuntes no son equivalentes a la documentación oficial de Flask, por lo que siempre podrás acudir a ella desde su sitio oficial.

## Capitulo 1 - Hello World!

### Rutas

```
Permiten asociar una URL con la lógica de presentación de la página solicitada.

la forma más clásica de definir una ruta, es por medio del decorador app.route, donde app corresponde a la instancia de la aplicación.
	
	Ej: 
		@app.route( '/' )
		def index():
			return '<h1>Hello World!</h1>'
			
Otra forma de definir una ruta es por medio del método app.add_url_rule, que en su forma básica requiere tres argumentos: la URL, el endpoint de la ruta y el nombre de la función.
	
	Ej:
		def index():
			return '<h1>Hello World!</h1>'
			
		app.add_url_rule( '/', 'index', index )
```

### Rutas dinámicas

```
Tienen el mismo propósito que una ruta convencional, sin embargo se diferencia de esta debido a que cuenta con secciones variables que pueden ser recibidas como parámetros en la función de la vista, por ejemplo la página de facebook https://www.facebook.com/<user-name>, donde <user-name> corresponde al nombre de usuario del perfil que se quiere ver.
	
	Ej:
		@app.route('/user/<name>')
		def user(name):
			return '<h1>Hello, {}!</h1>'.format(name)
			
Por defecto las variables de la URL dinámica son de tipo string, pero también podemos cambiar el tipo, definiendo en la ruta la siguiente url /user/<int:id>
```

### Servidor de desarrollo

```
Por defecto, Flask incorpora un servidor de desarrollo para arrancar nuestra aplicación, para ello, el framework provee el comando <b>flask run</b> para su ejecución. Este comando buscará el script de python que contiene la aplicación y para poder encontrarlo, utiliza la variable de entorno FLASK_APP para encontrarla.

	Ej:
		> set FLASK_APP = hello.py
		> flask run

Para ver la aplicación en funcionamiento, debes ingresar a la URL http://localhost:5000/ y para detener el servidor, basta con presionar CTRL + C en la consola.
```

### Modo depuración

```
Cuando activamos el modo de depuración, se activan dos factores útiles para el desarrollador, el primero consiste en el Reloader, encargado de monitorear si ocurren cambios en los archivos, de esta manera reinicia el servidor de forma automática. Por otra parte, el Debug permite visualizar una excepción no controlada a través del navegador web.

Como por defecto, el Debug se encuentra desactivado, para activarlo debes setear la variable de entorno FLASK_DEBUG en 1 antes de ejecutar el comando flask run.

Ej:
	> set FLASK_APP = hello.py
	> set FLASK_DEBUG = 1
	> flask run
```

### Contextos de aplicación y solicitud

```
1. Contexto de aplicación

	- current_app: Instancia de aplicación para la aplicación activa
	- g: Objeto que la aplicación puede utilizar para almacenar datos temporales durante un Request, esta variable se reestablece por cada solicitud
	
2. Contexto de solicitud
	
	- request: Objeto de solicitud, que almacena una petición HTTP enviada por el cliente
	- session: Corresponde a un diccionario que almacena valores que persisten en cada request.
```

### Revisar rutas de la aplicación
```
Si queremos ver el mapa de rutas que se elabora en la aplicación, debemos ingresar a la consola de Python y ejecutar la siguiente:

	(venv) > python
	>>> from hello import app
	>>> app.url_map
```

### Atributos del objeto request

```
	- form: Un diccionario con todos los campos de formulario enviados con la solicitud.

	- args: Un diccionario con todos los argumentos pasados en la cadena de consulta de la URL.

	- values: Un diccionario que combina los valores en formy args.

	- cookies: Un diccionario con todas las cookies incluidas en la solicitud.

	- headers: Un diccionario con todos los encabezados HTTP incluidos en la solicitud.

	- files: Un diccionario con todas las cargas de archivos incluidas con la solicitud.

	- get_data(): Devuelve los datos almacenados en el búfer del cuerpo de la solicitud.

	- get_json(): Devuelve un diccionario de Python con el JSON analizado incluido en el cuerpo de la solicitud.

	- blueprint: El nombre del plano del Frasco que maneja la solicitud.

	- endpoint: El nombre del punto final de Flask que maneja la solicitud. Flask usa el nombre de la función de vista como el nombre del punto final para una ruta.

	- method: El método de solicitud HTTP, como GET o POST.

	- scheme: El esquema de URL (http o https).

	- is_secure(): Devuelve True si la solicitud se realizó a través de una conexión segura (HTTPS).

	- host: El host definido en la solicitud, incluido el número de puerto si lo proporciona el cliente.

	- path: La porción de ruta de la URL.

	- query_string: La parte de la cadena de consulta de la URL, como un valor binario sin procesar.

	- full_path: La ruta y las porciones de cadena de consulta de la URL.

	- url: La URL completa solicitada por el cliente.

	- base_url: Igual que URL, pero sin el componente de cadena de consulta.

	- remote_addr: La dirección IP del cliente.

	- environ: El diccionario de entorno WSGI sin procesar para la solicitud.
```

### Request Hooks

```
Los hooks permiten ejecutar codigo antes y despues de que se realiza una peticion, esto es util cuando queremos registrar informacion en un log, abrir y cerrar una conexion de base de datos, etc.

Flask provee cuatro hooks compatibles:

	- before_request: Registra una función para ejecutar antes de cada solicitud.

	- before_first_request: Registra una función para ejecutarse solo antes de que se maneje la primera solicitud. Esta puede ser una forma conveniente de agregar tareas de inicialización del servidor.

	- after_request: Registra una función para ejecutar después de cada solicitud, pero solo si no se produjeron excepciones no controladas.

	- teardown_request: Registra una función para ejecutar después de cada solicitud, incluso si se produjeron excepciones no controladas.
```

### Response

```
Como se ha visto en ejemplos anteriores, las respuestas se han basado en cadenas de texto (String), sin embargo, podemos devolver tuplas en la cual devolvamos un codigo de respuesta distinto al estado 200 (estado ok).
	
	Ej:
		@app.route('/')
		def index():
			return '<h1>Bad Request</h1>', 400
			
Sin embargo, Flask proporciona la funcion make_response() que puede recibir hasta 3 argumentos y devuelve un objeto response. Este metodo es util si queremos customizar la respuesta para modificar cookie por ejemplo.

	Ej:
		from flask import make_response

		@app.route('/')
		def index():
			response = make_response('<h1>This document carries a cookie!</h1>')
			response.set_cookie('answer', '42')
			return response
			
Los atributos del objeto response, son los siguientes:

	- status_code: El código numérico de estado HTTP

	- headers: Un objeto tipo diccionario con todos los encabezados que se enviarán con la respuesta.

	- set_cookie(): Agrega una cookie a la respuesta.

	- delete_cookie(): Elimina una cookie

	- content_length: La longitud del cuerpo de respuesta.

	- content_type: El tipo de medio del cuerpo de respuesta

	- set_data(): Establece el cuerpo de la respuesta como un valor de cadena o bytes

	- get_data(): Obtiene el cuerpo de respuesta
```

### Redirect

```
Un redirect es un tipo especial de respuesta, que se utiliza por lo general al recibir peticiones de formulario. El código de estado de respuesta es el 302, sin embargo el Framework Flask proporciona una función redirect() para este propósito.

	Ej:
		from flask import redirect

		@app.route('/')
		def index():
			return redirect('http://www.example.com')
```
		
### Abort

```
Es otra respuesta especial es la generada por la función abort(), que se utiliza para el manejo de errores.
	
	Ej:
		from flask import abort

		@app.route('/user/<id>')
		def get_user(id):
			user = load_user(id)
			if not user:
				abort(404)
			return '<h1>Hello, {}</h1>'.format(user.name)

Ten en cuenta que abort()no devuelve el control a la función porque genera una excepción.
```

## Capitulo 2 - Plantillas

### Renderizado de plantillas

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

### Variables

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

### Filtros de variables

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

```
Nota: 

Jinja2 escapa todas las variables por motivo de seguridad, esto quiere decir que si la variable tiene como valor un extracto de codigo html como por ejemplo <h1>Hello World!</h1>, Jinja2 lo trasformará como &lt;h1&gt;Hello World!&lt;/h1&gt;. Es por esto que el filtro safe es de utilidad cuando queremos que Jinja2 no escape el valor de una variable.

nunca utilices safe en variables que sean ingresadas por medio de formularios de usuarios.
```

### Sentencias para control de flujo
inja2 ofrece varias estructuras de control que pueden usarse para alterar el flujo de la plantilla, dentro de ellas encontramos los siguientes ejemplos:

#### Condiciones
```
Permite condicionar un segmento del html, ver ejemplo:

{% if user %}
    Hello, {{ user }}!
{% else %}
    Hello, Stranger!
{% endif %}
```

#### Ciclos
```
Permite iterar un arreglo de datos, tal como se muestra en este ejemplo:

<ul>
    {% for comment in comments %}
        <li>{{ comment }}</li>
    {% endfor %}
</ul>
```

#### Macros
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

#### Herencia
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

### Páginas de error personalizadas

Para poder capturar los errores producidos por el servidor, puedes implementar el decorador @app.errorhandler de la siguiente manera

```
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
```

### Enlaces

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
