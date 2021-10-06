#API cotizacion 
Esta API recibe como parametros el codigo ISO de una moneda, la cantidad de pesos argentinos y devuelve la cantidad de
la moneda seleccionada a la que equivale la cantidad de pesos indicada.
## Pasos para ejecutar el proyecto de forma local.  
1- Ejecutar el comando: `pip install -r requirements.txt` para instalar los paquetes necesarios  
2- Para iniciar la aplicacion ejecutar:```uvicorn --port 5000 --host 127.0.0.1 main:app --reload```  
Esto inciara la aplicacion en el la direccion 127.0.0.1:5000

##Hacer una consulta desde el navegador
`127.0.0.1:5000/cotizacion/{currency}/{quantity}`

currency = El código ISO de la moneda que se quiere cotizar. ej. ('BGN', 'BRL', 'USD', 'EUR')  
quantity = la cantidad que se quiere cotizar.

##Documentacion 
Disponible en `127.0.0.1:5000/docs`