# En este pequeño proyecto se realizo la introduccion a los entornos virtuales y a lo que es la FASTAPI para lograr imprimir mediante un servidor local 'uvicorn' nuestro primer 'Hola mundo', donde los pasos a seguir fueron los siguientes:

*se creo un nuevo proyecto en nuestro pc, ejemplo: mkdir hello

*se creo el respectivo entrono virtual en el proyecto el cual estara realizado en el lenguaje python,
 ejemplo: py -m venv venv.

*se procese a activar dicho entorno, ejemplo: venv/scripts/activate.

*se procede a instalar las dependencias necesarias las cuales son la fastapi y uvicorn en nuestro entorno virtual, ejemplo: pip install fastapi uvicorn. 

*luego en nuestro proyecto creamos un modulo llamado app.py, en el cual vamos a importar las fastapi y mediante una ruta creada con el 'get' y una funcion vamos a lograr imprimir nuestro primer 'hola mundo', en este servidor local que nos proporciona uvicorn.

*por ultimo ejecutamos el siguiente comando en nuestra consola, ejemplo uvicorn app:app el cual nos va a permitir activar el servidor. 
