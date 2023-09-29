Agustín Monsalve - Profesora Katherine Páez

#PRESUPUESTOS DEL IND DE 2019 AL 2022

Debido a que el tema central de nuestra investigación son los gastos y financiamiento destinados a los deportistas de elite chilenos, agrupados en sus propias federaciones, es que creímos que la expendidura efectivamente realizada que ejerce el Instituto Nacional de Deportes (IND) en ellos es muy relevante.

La entidad pública es la división del Ministerio del Deporte encargada de "ejecutar la política nacional de deportes del país".

Por tanto, por medio del Portal de Transparencia[https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=BA002], accedimos a sus presupuestos anuales desde 2019, centrándonos específicamente en los que contenían:

a) Una sección de gasto anual ejecutado, 

b) Gasto efectuado (no previsto) en deportistas profesionales 

c) Aquellos que fuesen lo más recientes posibles, es decir, en un rango de 4 años hacia el pasado. 

Esto último para que tuviesen mayor cercanía con la actualidad nacional, enfocándonos principalmente en el hecho de que se realizarán este año los Juegos Panamericanos en la capital de nuestro país, y que la última edición de esta competencia continental se realizó en 2019 (Lima), por lo que los deportistas nacionales tuvieron este período de tiempo para prepararse.

Lamentablemente, decidimos dejar afuera el presupuesto del año 2019, esto porque no cumplía o no especificaba el segundo requisito mencionado (b).

Tampoco quisimos centrarnos en los ingresos hacia el presupuesto por parte de privados, tributos o el Estado, pues en las tres bases de datos seleccionadas se utilizan todos (2020 y 2021) o casi todos (99,1% en 2022) los fondos disponibles. Por lo que descartamos irregularidades en ese aspecto.


Los links a estas bases de datos son los siguientes:

* 2019[https://transparencialobby.ind.cl/activa/presupuestoejecucion/ejecucion_de_ingresos_gastos_diciembre_2019/ing_gas_diciembre.pdf]

* 2020[https://transparencialobby.ind.cl/activa/presupuestoejecucion/ano2020/diciembre/diciembre2.pdf]

* 2021[https://transparencialobby.ind.cl/activa/presupuestoejecucion/2021/diciembre/01.pdf]

* 2022 [https://transparencialobby.ind.cl/activa/presupuestoejecucion/ejecucion_de_ingresos_gastos_diciembre_2019/ing_gas_diciembre.pdf]


#PROCESO DE LIMPIEZA

La filtración de información a estas bases de datos, que unifiqué en una, se realizó con el propopósito de responder principalmente a las siguientes tres preguntas:

- ¿Cuánto invierte el IND en nuestros deportistas nacionales anualmente?

- ¿Cuánto es esto en términos de proporciones (%) respecto al gasto total cada año efectuado por la institución?

- ¿Cómo han variado estas cifras desde los últimos Juegos Pánamericanos?

- Bonus: comparar con el gasto en deportes de un país mucho más pobre que Chile pero que siempre nos gana en los Panamericanos: Cuba.


Siguiendo estas preguntas guía, las bases de datos se limpiaron de la siguiente manera:

1) Previamente, las bases de datos fueron transformadas de formato Excel a CSV (proceso en que se vació la fila GASTOS TOTALES del presupuesto 2021, por lo que tuvieron que ser reañadidos), subidas a Colab de Google y ejecutadas:

* 2020:

import pandas as pd 

veinteveinte= pd.read_csv("/content/drive/MyDrive/Presupuesto y ejecución IND 2020.csv" , sep=";" , encoding="latin-1")

veinteviente


* 2021: 

import pandas as pd 

veinteveintiuno= pd.read_csv("/content/drive/MyDrive/Presupuesto y ejecución IND 2021.csv" , sep=";" , encoding="latin-1")

veinteveintiuno


* 2022:

import pandas as pd 

veinteveintidos= pd.read_csv("/content/drive/MyDrive/Presupuesto y ejecución IND 2022.csv" , sep=";" , encoding="latin-1")

veinteveintidos


2) Luego, las que requirieron la eliminación de columnas que entorpecieran la titulación de algunas filas fueron despejadas (solo la de 2020 en este caso), utilizando el código:


veinteveinte= veinteveinte.drop(columns=["PLANILLA DE DECRETOS POR PROGRAMA PERIODO 2020" , "Unnamed: 1" , "Unnamed: 2"])

veinteveinte


3) A continuación, con el método de selección de datos del código iloc, se cruzó información de las filas referentes a gastos totales y gastos en deportismo competitivo, con la columna que indicaba ejecución efectiva y no pronosticada en la ley de presupuestos para estas categorías, utilizando el código:

(variable de base de datos limpia)= (variable de base de datos).iloc[[números de filas],[números de columnas]]
(variable de base de datos limpia)


4) Una vez seleccionados estos datos por cada base de datos, hubo que crear una nueva dataframe para agruparlos, utilizando el código:


Gastos_IND = {"Año" : [2020 , 2021 , 2022],
             "Deporte competitivo" : [646579000 , 20521872000 , 22721155545],
             "Total" : [2653804000 , 129552031000 , 217638105467]}

Gastos_IND = pd.DataFrame(Gastos_IND, columns = ["Año" , "Deporte competitivo" , "Total"])
Gastos_IND

Esto de manera menos automática de lo esperado pues no existían filas o columnas con títulos uniformes entre sí, pese a que se referían a lo mismo (Filas: Deporte de Competición=FORTALECIMIENTO DEL DEPORTE DE RENDIMIENTO CONVENCIONAL Y PARALÍMPICO ; Columnas: Ejecutado=Vigente)

5) Luego, y una vez agrupados, para obtener el % de gasto del deporte competitivo que corresponde al gasto total se utilizó el código:

values ={"Año":[2020 , 2021 , 2022],"Deporte competitivo":[646579000 , 20521872000 , 22721155545],"Total":[2653804000 , 129552031000 , 217638105467]}

Gastos_IND = pd.DataFrame(values)
Gastos_IND["% del gasto total"]= Gastos_IND["Deporte competitivo"]/Gastos_IND["Total"]*100
print(Gastos_IND)


Finalmente, una base de datos limpia y lista para graficar.
