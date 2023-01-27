from fastapi import FastAPI

app=FastAPI()

#aqui se especifica una ruta @app.get

@app.get('/')
def helloworld():
    return "Hello world"

# uvicorn app:app aqui lo que se hace es activar el servidor indicandole que muestre lo que contienene el archivo app