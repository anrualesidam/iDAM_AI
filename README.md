# Base_page_idam

Este repositorio esta diseñado para una pagina web service la cual es multiplataforma (responsive design). Cuenta con la carpeta proyecto (base_project) y la carpeta (base_app). En la primera de ellas se encuentra los archivos .py del proyecto, los cuales se conectan por medio de **urls.py** a la carpeta de aplicaciones (base_app) en donde se incluye todo lo referente al diseño del frontend y backend de la pagina. 

En la carpeta base_app se encuentra el archivo static donde se incluyen archivos de diseño **.css** y las imagenes utilizadas en el proyecto. Adicionalmente, se cuenta con una carpeta templates en donde se incluye el codigo ".html" referente a las diferentes pestañas del web service. Además, en el archivo **urls.py** se encuentran conectadas las diferentes pestañas del codigo y en views.py las respectivas funciones que renderizan el codigo **.html**. 

Este proyecto sirve como base de diseño para futuras paginas tipo web service.


**Guia de instalacion** 
1. **Clonar repositorio**
```bash 
    - git clone https://gitlab.com/SJuanOG/base_page_idam.git 
``` 
2. **Instalación**
    Creacion del entorno virtual 
```bash 
    - virtualenv venv
    - source venv/Scripts/activate
```
    Instalacion paquete de librerias
```bash 
    - pip install -r requirements.txt
```

3. **Verificar funcionamiento**
```bash
    - python manage.py runserver
```

