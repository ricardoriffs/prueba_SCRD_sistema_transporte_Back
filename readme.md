

## Contexto
Para esta prueba se uso django rest framework implementando 3 aplicaciones para cada uno de los modelos diseñados en el diagrama e-r 
También se uso psycopg2 para la implementación de postgresql 
Y de orm se uso qureysets y modelos para realizar las consultas por medio de las apiview de django y los modelos para generar la estructura de datos en la base de datos.



## Instalación de la prueba 

### Script para crear la bd en postgresql: 
-- Database: prueba_tecnica

-- DROP DATABASE IF EXISTS prueba_tecnica;

CREATE DATABASE prueba_tecnica
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

Pasos para configurar postgresql en el proyecto
pip install psycopg2  

Luego de instalarlo configuramos la conexión en el archivo local.py en la carpeta settings alojada en la carpeta sistema_transporte

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prueba_tecnica',
        'USER': 'postgres',
        'PASSWORD': 'wilson2001',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
nota: tener en cuenta la contraseña de su usuario local
esta es la parte de código que se cambia, toca poner el usuario de postgresql que se tiene localmente por lo general es postgres o root , la contraseña de ese usuario y ya el resto se deja normal

para inicializar el proyecto es recomendado iniciar el virtual env, se ubican en la carpeta prueba_tecnica_cortex_soluciones y ejecutan el comando "py -m venv venv", y después activan el entorno virtual con el script ".\venv\Scripts\activate"

### instalar dependencias
para instalar las dependencias del proyecto ejecutan el siguiente comando

- pip install -r requirements.txt

Por ultimo creamos las migraciones con el comando
- python3 manage.py makemigrations

Y luego realizamos las migraciones en la base de datos
- python3 manage.py migrate

Por ultimo se levanta el servidor con el comando
- python3 manage.py runserver


Adicionalmente si se quiere interactuar con el administrador de django toca antes de levantar el servidor, correr este comando: 
- python3 manage.py createsuperuser

se ingresan los datos que se solicita y se levanta el servidor para acceder al djando admin

Por ultimo, las versiones de todas las herramientas utilizadas en el proyecto se encuentran en el archivo requirements.txt

### nota: Python3 se usa para el OS MacOS, en caso de tener window debe usar py