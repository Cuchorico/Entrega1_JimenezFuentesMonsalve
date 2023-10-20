La elección de esta base de datos tiene como objetivo mostrara la inversión de Cuba en deporte, para posteriormente realizar una comparación con la invención realiza por Chile. 
En primera instancia la base de datos tenía montos de educación, seguridad, cultura y deporte, ciencias de innovación, salud pública y gastos en administración pública. Todos los datos mostrados son del año 2018 hasta el 2022.
Para limpiar la base de datos, la primera modificación fue  la conversión del dinero que estaba en un principio, debido a que, este, estaba en pesos Cubanos, específicamente en miles de millones. El procedimiento de limpieza comenzó en el Excel, multiplicando las cantidades por 1.000.000 esto, por el hecho de estar en miles de millones. Luego  cuando el dinero ya estaba en millones, el resultado fue multiplicado por 37.73 que es el valor del cambio oficial del peso cubano por el chileno.
Posterior a los antes mencionado, subí la base de datos a Colab, una vez ya estando allí, separe la columna donde aparecen los montos designados a deporte. Para realizar este procedimiento, asigne los siguientes códigos: 

import pandas as pd

cuba = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Presupuesto Estatal de Cuba anual.csv" , sep=";" , encoding="latin-1")

print (cuba["Unnamed: 3"][20:26])
print (cuba["Unnamed: 8"][-2:])
