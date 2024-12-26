<div align="center">

# ChatApp con Reflex

</div>

<div style="font-size: 20px;">

- [**Introducción**](#introducción)
- [**Manual**](#manual)
    - [**Instalación**](#instalación)
    - [**Uso**](#uso)

</div>

# Introducción
Bardia Rajab Rajabi - [@Valwraek](https://github.com/Valwraek)  
Gabriel Suárez Domínguez - [@GabrielgsdCIUwU](https://github.com/GabrielgsdCIUwU)

Somos alumnos de Desarrollo de Aplicaciones Multiplataforma en el IES de Teis.  
Este proyecto se ha realizado siguiendo el tutorial de reflex para comprender como funciona este framework.

# Manual
## Instalación
### Entorno Virtual - Windows

1. El primer paso es descargar el proyecto y descomprimirlo.

![Imagen de instalación del primer paso](/assets/img-readme/instalacion-primer-paso.png)

2. El segundo paso es abrirlo con nuestro editor e ir al terminal para escribir lo siguiente:

 - **``py -m venv venv``** esto nos va crear un entorno virtual llamado venv

 ![Imagen de instalación del segundo paso](/assets/img-readme/instalacion-segundo-paso.png)

 3. Ahora toca activar el entorno virtual y para ello hacemos lo siguiente:
    - En la terminal escribimos lo siguiente **``cmd``**.
    - Luego se escribirá **``.\venv\Scripts\activate.bat``**.

Se sabrá que estamos en el entrono virtual porque en el terminal podremos observar un (venv) entre paréntesis

![Imagen de instalación del tercer paso](/assets/img-readme/instalacion-tercer-paso.png)

4. Ahora instalaremos todas las dependencias necesarias para nuestro proyecto.  
    - **``pip install -r requirements.txt``**

### Entorno virtual - Linux

El paso 2 y el paso 3 difieren en Linux. Los comandos para crear un entorno virtual y activarlo son:  

- **``python3 -m venv .venv``** con este comando se crea el entorno virtual.  
- **``source .venv/bin/activate``** con este se activará el entorno virtual.  

## Uso
### Ejecutar la aplicación

Para los dos sistemas operativos es igual. 

- **``reflex run``** es el comando a utilizar para esta tarea.

![Imagen de puerto donde se puede ver el proyecto](/assets/img-readme/puerto.png)

Si vamos a nuestro navegador y vamos al localhost:3000 podremos ver nuestro proyecto

![Imagen de web en uso](/assets/img-readme/web-funcionando.png)