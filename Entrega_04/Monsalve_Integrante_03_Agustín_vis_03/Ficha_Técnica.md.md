# Ficha Técnica

1) El primer código utilizado sirve para importar la database y depositarla en la variable "IND" (Instituto Nacional de Deportes), código que, para funcionar al 100%, tuve que añadirle la especificación "encoding="latin-1"", debido al origen de una hoja Excel en español latino de la base de datos.


import pandas as pd
nRowsRead = None 
IND = pd.read_csv('/content/drive/MyDrive/Variación anual de ingresos al presupuesto del IND.csv', delimiter=',', nrows = nRowsRead, encoding="latin-1")
IND.dataframeName = 'Variación anual de ingresos al presupuesto del IND'
nRow, nCol = IND.shape
print(f'There are {nRow} rows and {nCol} columns')


2) Una vez importada la base de datos, está se ejecutará al escribir la variable "IND".

3) Ya visualizables y listos los datos, procedo a elaborar un gráfico de líneas con la simple, y fácil de usar, función "matplotlib.pyplot", rellenando las casillas para definir que valores quiero que se muestren en el eje X (valoresX) e Y (valoresAY, valoresBY)

En el eje Y se graficaron dos variables comparativamente. Primero, el "Presupuesto IND (miles de $US)", que corresponde a los fondos totales por año con los que contó y cuenta el Instituto Nacional de Deportes. Y segundo, la dimensión "Ejecución o gasto (miles de $US)", correspondiente a la fracción de ese presupuesto que se invirtió o gastó. Ambas en miles de dólares, o sea, multiplicables por 1.000 y en términos del valor de cambio del país norteamericano EE.UU.

En el eje X, en tanto, se graficó la variable "Años", correspondiente, como bien dice, a los años en los que se sitúan temporalmente estos fondos y gastos, en un período que va desde 2015 hasta agosto de 2023 (último balance mensual del IND).

Finalmente, añado los títulos a las líneas del gráfico para identificar que representa cada una {plt.legend(["Presupuesto IND (miles de $US)", "Ejecución o gasto (miles de $US)"])}


import matplotlib.pyplot as plt

valoresAY = [156471,141443,149352,132558,136003,4873,152650,261005,528688]
valoresBY = [27248,28766,38861,28053,20926,2912,142177,258068,103504]
valoresX = [2015,2016,2017,2018,2019,2020,2021,2022,2023]
fig, ax = plt.subplots()
plt.plot(valoresX, valoresAY, "o--g" )
plt.plot(valoresX, valoresBY, "s:b" )
plt.legend(["Presupuesto IND (miles de $US)", "Ejecución o gasto (miles de $US)"])
plt.show()


## Observaciones

La base de datos fue elaborada en base a diversas fuentes ([un estudio publicado en septiembre sobre los presupuestos del IND](https://acrobat.adobe.com/id/urn:aaid:sc:US:22870d75-5f48-408b-b38b-5148ce5ed4fa), [el Portal de Transparencia](https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=BA002), la [Biblioteca Nacional del Congreso](https://www.bcn.cl/presupuesto/periodo/2023/partida/26) para conocer el presupuesto del IND de 2023, y [la página web de la Dirección de Presupuestos](https://www.dipres.gob.cl/597/w3-multipropertyvalues-22291-35324.html)).