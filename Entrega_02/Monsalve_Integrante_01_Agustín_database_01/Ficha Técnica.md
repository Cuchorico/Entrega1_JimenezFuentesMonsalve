
# veinteveinte= base de datos veinteveinte sin sus primeras tres columnas, las cuales no permitían agregarle títulos a las filas seleccionadas para la dataframe limpia, ya que estos se encontraban en la tercera columna.

veinteveinte= veinteveinte.drop(columns=["PLANILLA DE DECRETOS POR PROGRAMA PERIODO 2020" , "Unnamed: 1" , "Unnamed: 2"])
veinteveinte


#  a, b y c fueron códigos iloc para seleccionar información que encontramos útil en la base de datos, la cual correspondiá a cifras numéricas enteras correspondientes a gastos ($) del IND.

variable= variable base_de_datos.iloc[[x,y],[x, y]]
variable

a= veinteveinte.iloc[[16,22],[0, -1]]
a

b= veinteveintiuno.iloc[[28,36],[3, -1]] 
b

c= veinteveintidos.iloc[[0,42,3],[0,3,5]] 
c


# Gastos_IND corresponde a los datos numéricos, tipo int(), ya limpios y agrupados en una tabla.

Gastos_IND = {"Año" : [2020 , 2021 , 2022],
             "Deporte competitivo" : [646579000 , 20521872000 , 22721155545],
             "Total" : [2653804000 , 129552031000 , 217638105467]}

Gastos_IND = pd.DataFrame(Gastos_IND, columns = ["Año" , "Deporte competitivo" , "Total"])
Gastos_IND


# pd.DataFrame(values) se utilizó para realizar una operación de división entre los datos de dos columnas de la tabla formada previamente (Deporte Competitivo y Total) y a los resultados multiplicarles por 100, para generar una columna de porcentajes indicativos de la proporción de gasto en deportistas deportivos con respecto al presupuesto ejecutado total del IND.

values ={"Año":[2020 , 2021 , 2022],"Deporte competitivo":[646579000 , 20521872000 , 22721155545],"Total":[2653804000 , 129552031000 , 217638105467]}

Gastos_IND = pd.DataFrame(values)
Gastos_IND["% del gasto total"]= Gastos_IND["Deporte competitivo"]/Gastos_IND["Total"]*100
Gastos_IND


## Todo esto permitió obtener datos enteros (gastos monetarios) y continous (%'s) relativos a las tarifas deportivas competitivas, la inversión total de la institución encargada de ejecutar la política deportiva (IND) y la proporcionalidad entre estas, para compararlas con cifras homólogas de otros países, y así saber cuál ejemplo hay que seguir y cuál no.