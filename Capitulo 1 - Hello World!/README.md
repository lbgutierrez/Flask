# Tutorial Flask - Capitulo 1

En este tutorial, solo se pretende crear de forma práctica una aplicacion hello world, haciendo uso del framework Flask.

## Objetivo

Generar un "hello world" paso a paso para crear una aplicación web basado en lenguaje de programación Python sobre el Framework Flask.

## Pre-requisitos

- Tener instalado y consigurado git para usarlo por medio de linea de comando
- Tener instalado Python 3
- Tener configurado Python por medio de línea de comando
- Tutorial realizado sobre sistema operativo Windows 10

## Comencemos

Crear un nuevo repositorio en github y clonarlo en nuestro workspace de la siguiente manera

```
git clone <https://github.com/github-user/my-repository>
```

Creamos un ambiente virtual de Python con el siguiente comando.

```
>python -m venv myvenv  
``` 

Para activar este nuevo ambiente virtual, es necesario ejecutar el archivo activate.bat que se encuentra en la carpeta myvenv creada por Python.

```
>cd myvenv/Scripts
>activate.bat
```

Una vez que se activa el ambiente virtual, el prompt cambiará y quedará de la siguiente manera.

```
(myvenv) C:\workspace\flask-login>
```

Luego debemos instalar las dependencias de Flask dentro del ambiente virtual que hemos creado y para ello utilizamos el siguiente comando.

```
>pip install flask
``` 

Con un editor de texto, crear los siguientes tres archivos.

```
1. app.py
3. requirements.txt
4. .gitignore
```

Las dependencias que vayamos agregando, debemos configurarlas en nuestro archivo requirements.txt, para ello ejecutamos el comando pip freeze, cuya salida la volcaremos en el archivo requirements.txt.

```
>pip freeze > requirements.txt
```

Luego configuramos el archivo .gitignore para ignorar los archivos de Python que no formaran parte del proyecto, para ello agregamos el siguiente contenido en el archivo.

```
myvenv/

*.pyc
__pycache__/

instance/

.pytest_cache/
.coverage
htmlcov/

dist/
build/
*.egg-info/
```

Agregar el siguiente código fuente en el archivo app.py

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

En nuestra consola, configurar las siguientes variables de entorno

```
>set FLASK_APP=app.py
>set FLASK_ENV=development
```

Ejecutar nuestra aplicación con

```
>python -m flask run
```

Finalmente subimos nuestros fuentes al repositorio con el siguiente comando

```
>git add -A
>git commit -m "linea base"
>git push
```

## Conclusión
Con estos pasos tu habrás aprendido lo siguiente:

- Crear un ambiente virtual sobre Python para aislar completamente nuestro entorno de desarrollo respecto al entorno de ejecución
- Instalar dependencias por medio del comando pip
- Crear un archivo requirements.txt para poder configurar nuestra aplicación en otros ambientes
- Configurar archivo .gitignore para ignorar carpetas y archivos que no se desean subir al repositorio
- Arrancar la aplicación flask por medio de linea de comando en ambiente local
- Subir los fuentes a github

## Anexos

A1. Instrucciones para clonar, configurar y ejecutar esta aplicación.

```
1. Clonar el proyecto

    git clone https://github.com/lbgutierrez/tutorial-flask-cap1.git

2. Crear ambiente virtual de python

    python -m venv myvenv

3. Activar el ambiente
 
    .\myvenv\Scripts\activate.bat

4. Instalar las dependencias
    
    python -m pip install -r requirements.txt

5. Configurar variables
    
    set FLASK_APP=app.py
    set FLASK_ENV=development
    
6. Arrancar
 
    python -m flask run
```